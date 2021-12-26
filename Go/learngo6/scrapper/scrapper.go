package scrapper

import (
	"encoding/csv"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/PuerkitoBio/goquery"
	ccsv "github.com/tsak/concurrent-csv-writer"
)

type extractedJob struct {
	id       string
	title    string
	company  string
	salary   string
	location string
	summary  string
}

func Scrape(query string) {
	var baseURL string = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=" + query
	var jobs []extractedJob
	mainC := make(chan []extractedJob)
	page_nums := GetPages(baseURL)
	for i := 0; i < page_nums; i++ {
		go GetPage(i, baseURL, mainC)
		// ...는 extractedJob의 내용물(content)만 가져와서 합칠 때 사용
		// ex) 현재, extractedJob은 [{}, {}, ... ,{}] 임. 그리고 main함수의 배열 jobs와 그냥 합치면
		// [ [{}, ..., {}], [{}, ..., {}], [{}, ..., {}], ...] 이런식임. 이것을 [{}, {}, ... ,{}] 이런식으로 합칠 때 사용!
	}

	// page_nums 수 만큼 channel 통해 데이터 전송받기
	for i := 0; i < page_nums; i++ {
		extracedJob := <-mainC
		jobs = append(jobs, extracedJob...)
	}
	// WriteCSV(jobs)

	NewWriteCSV(jobs)
}

// go routine 이용해서 csv 파일에 데이터 동시에 입력시키기(써드파티 라이브러리 이용)
func NewWriteCSV(jobs []extractedJob) { // 여기서 job은 하나의 struct를 가리킴! 그러므로 for loop 돌 필요 없음
	csv, err := ccsv.NewCsvWriter("./jobs.csv")
	if err != nil {
		panic("Could not open 'jobs.csv' for writing")
	}
	defer csv.Close() // 해당 함수 끝나고 마지막에 호출되어야 실질적으로 입력!

	// header 삽입
	header := []string{"link", "title", "company", "salary", "location", "summary"}
	csv.Write(header)

	done := make(chan bool)
	for _, job := range jobs {
		go func(job extractedJob) {
			record := []string{"https://kr.indeed.com/jobs?q=python&l&vjk=" + job.id, job.title, job.company, job.salary, job.location, job.summary}
			csv.Write(record)
			done <- true
		}(job)
	}

	for i := 0; i < len(jobs); i++ {
		fmt.Println("데이터 입력 상태:", <-done)
	}
}

// csv 파일로 write 하기
func WriteCSV(jobs []extractedJob) {
	file, err := os.Create("./jobs.csv") // 파일 만들기. err != nil 이면 파일 만드는 데 에러가 발생한 것임
	checkRequest(err)

	w := csv.NewWriter(file)
	defer w.Flush() // Flush 할 때 실질적으로 파일에 데이터가 입력됨. 마지막에 Flush!

	// csv header 생성
	header := []string{"link", "title", "company", "salary", "location", "summary"}
	wErr := w.Write(header) // Write할 때 record는 []string 타입이어야 함! 그리고 반환할 때 잘 삽입되었는지 error를 반환(err == nil 이면 잘 입력된 것을 의미)
	checkRequest(wErr)

	// csv에 데이터 입력
	for _, job := range jobs {
		record := []string{"https://kr.indeed.com/jobs?q=python&l&vjk=" + job.id, job.title, job.company, job.salary, job.location, job.summary}
		wErr := w.Write(record)
		checkRequest(wErr)
	}
}

// 각 페이지 넘버에 해당하는 URL에 request 요청
func GetPage(page int, url string, mainC chan []extractedJob) {
	var jobs []extractedJob      // []extractedJob 의미: struct인 extractedJob이 [](array)안에 들어있는 dtype임을 의미
	c := make(chan extractedJob) // go routine 하기 위한 channel 정의

	// Go언어도 문자열끼리 concat이 가능함. 그래서 string convert 내장 패키지 아용 Itoa = Int to 문자열 즉, 숫자를 문자열로
	pageURL := url + "&start=" + strconv.Itoa(page*10)
	fmt.Println("Requesting ... ", pageURL)
	// Request 요청 및 에러 핸들링
	resp, err := http.Get(pageURL)
	checkRequest(err)
	checkStatus(resp)

	defer resp.Body.Close()
	doc, err := goquery.NewDocumentFromReader(resp.Body)
	checkRequest(err)
	mosaic_zone := doc.Find(".tapItem")
	mosaic_zone.Each(func(i int, card *goquery.Selection) {
		go extractJob(card, c)
	})

	// channel 로부터 데이터 전송받기
	for i := 0; i < mosaic_zone.Length(); i++ {
		job := <-c
		jobs = append(jobs, job)
	}

	// main으로 channel 통해 데이터 전송
	mainC <- jobs
}

// 텍스트 추출하는 함수 분리
func extractJob(card *goquery.Selection, c chan<- extractedJob) {
	id, _ := card.Attr("data-jk")
	title := CleanString(card.Find(".jobTitle > span").Text())
	company := CleanString(card.Find(".companyName").Text())
	salary := CleanString(card.Find(".salary-snippet").Text())
	location := CleanString(card.Find(".companyLocation").Text())
	summary := CleanString(card.Find(".job-snippet").Text())
	c <- extractedJob{
		id:       id,
		title:    title,
		company:  company,
		salary:   salary,
		location: location,
		summary:  summary}
}

// 문자열 clean하게 만들기
func CleanString(str string) string {
	// TrimSpace: 문자열 양끝 공백 삭제
	// Fields : 문자열의 단어 단위를 원소로 하는 array로 반환(문자열 사이의 공백들 모두 삭제 가능)
	// Join([]string(array), sep): array를 sep 기준으로 분할 후 하나의 문자열로 반환
	return strings.Join(strings.Fields(strings.TrimSpace(str)), " ")
}

// page 숫자 얻기
func GetPages(url string) int {
	var page_nums int
	resp, err := http.Get(url)
	checkRequest(err)
	checkStatus(resp)

	defer resp.Body.Close() // GetPages 함수가 끝나고 난 뒤 도큐먼트 닫아주어야 메모리가 새어나가지 않음!
	// response body 가져오기위해 go query 도큐먼트 만들기
	doc, err := goquery.NewDocumentFromReader(resp.Body)
	checkRequest(err)
	doc.Find(".pagination").Each(func(i int, s *goquery.Selection) {
		page_nums = s.Find("a").Length()
	})
	return page_nums
}

// 에러 핸들링
func checkRequest(err error) {
	if err != nil {
		// 프로그램 종료
		log.Fatalln(err)
	}
}

func checkStatus(res *http.Response) {
	if res.StatusCode != 200 {
		log.Fatalln("Request failed with Status:", res.StatusCode)
	}
}

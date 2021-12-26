package main

import (
	"os"
	"strings"

	"github.com/labstack/echo"
	"github.com/younghun-jo/learngo6/scrapper"
)

const fileName = "jobs.csv"

func handleHome(c echo.Context) error {
	// 웹 페이지에 문자열 출력하고 싶을 때 return c.String(http.StatusOK, "Heelo World!")
	return c.File("./home.html")
}

func handleScrape(c echo.Context) error {
	defer os.Remove(fileName) // 클라이언트에게 첨부파일로 보낸 뒤 웹 서버(현재는 로컬)에서는 csv 파일 삭제
	query := c.FormValue("query")
	query = strings.ToLower(scrapper.CleanString(query))
	// Scrapper 수행!
	scrapper.Scrape(query)
	return c.Attachment(fileName, query+"_jobs.csv") // 클라이언트에게 csv 파일 첨부파일로 전송
}

func main() {
	e := echo.New()
	e.GET("/", handleHome)
	e.POST("/scrape", handleScrape)
	e.Logger.Fatal(e.Start(":1330"))
}

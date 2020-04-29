#지마켓 검색창에 iphone 검색 후 제품 데이터 Selenium 이용해서 가져오기

# import 할 것들
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
#chrome_options.add_argument("--Headless")   #=> 헤드리스 모드

# webdriver 설정(chrome) 
browser = webdriver.Chrome("C:/webdriver/chrome/chromedriver.exe")  # 추가인자로 options에 위에서 정의한 chrome_options 넣을 수 있음

# 웹브라우저 내부 대기
browser.implicitly_wait(50)

# 웹브라우저 사이즈 설정
browser.set_window_size(1920,1280)

# 웹페이지 이동
browser.get("http://www.gmarket.co.kr/")

# 지마켓 홈페이지 검색어 input 설정
element = browser.find_element_by_css_selector("span.box__search-input > input.form__input")

# 검색어 입력 
element.send_keys("iphone")

# 엔터키 눌러주는 거(form submit!)
element.submit()

# 스크린 샷 저장(for 잘 진행되고 있는지)
#browser.save_screenshot("C:/gmarket.png")

# 타임 슬립
time.sleep(10)

#현재 페이지
cur_page = 1
# 크롤링 할 페이지 수 
target_page = 3

# browser 속성 확인
#print(dir(browser))

# browser 내용 확인
#print(browser.page_source)

while cur_page <= target_page:


    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # iphone 리스트 선택
    i_list = soup.select("a.link__item > span.text__item")

   # 페이지 번호 출력
    print('****** Current Page : {}'.format(cur_page), '******')
    print()

    for v in i_list:
        # 어떻게 구성되있는지 출력
        #print(v)
        print(v.text)

    print()

    # 페이지 이동시 스크린샷 
    browser.save_screenshot("C:/cur_page{}.png".format(cur_page))

    # 페이지 증가
    cur_page += 1

    # 추가 조건문 삽입
    if cur_page > target_page:
        print("Crawling Succeed.")
        break

    # 페이지 이동버튼 클릭
    WebDriverWait(browser, 50) \
        .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.box__component box__component-pagination > a:nth-child({})'.format(cur_page)))).click()

    # 페이지 이동 시 랜더링 시간 대기
    time.sleep(10)

    # 참고) BeautifulSoup 인스턴트 삭제
    #del soup

# 브라우저 종료
browser.close()

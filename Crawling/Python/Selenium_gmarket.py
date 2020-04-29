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
browser.implicitly_wait(5)

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
browser.save_screenshot("C:/gmarket.png")

# 타임 슬립
#time.sleep(3)

# browser 속성 확인
#print(dir(browser))

# browser 내용 확인
#print(browser.page_source)

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# iphone 리스트 선택
i_list = soup.select("a.link__item > span.text__item")

# i_list 내용 맞는지 출력
#print(i_list)

for v in i_list:
    # 어떻게 구성되있는지 출력
    #print(v)
    print(v.text)
    
# 사람인 채용 정보 사이트에서 데이터 엔지니어 채용정보와 회사 갖고오기

# import 할 것들
from selenium import webdriver
import time
from selenium.webdriver.common.by import By # 언제까지 브라우저 접속 기다려주겠다
from selenium.webdriver.support.ui import WebDriverWait # By 모듈과 같이 자주스임 
from selenium.webdriver.support import expected_conditions as EC # 어떤 상태까지 기다리겠다(페이지 클릭이나 커서 이동 클릭시)
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우저가 화면에 뜨지 않고 내부적으로 실행

# webdriver 설정                                                     # 헤드리스로 실행하겠다는 옵션 추가
browser = webdriver.Chrome("C:/webdriver/chrome/chromedriver.exe", options=chrome_options) 

# 크롬 브라우저 내부 대기
browser.implicitly_wait(6)

# 브라우저 사이즈 설정 -> headless 모드일땐 굳이 작성안해도 될 거 같음
#browser.set_window_size(1980, 1240)

# 페이지 이동
browser.get("http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4")

# browser 내용이 무엇인지 한번 봐보자
#print(browser.page_source)

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 1페이지 채용정보 갖고오기
cru_list = soup.select('div.area_job')

# 채용정보 리스트 출력해보기 -> a태그의 모든 내용 다 출력
#print(cru_list)

# 채용정보 반복문으로 정렬
for v in cru_list:
    if v.find('h2', class_='job_tit') and v.find('div', class_='job_date') :
        print('채용정보: ', v.select('a')[0]['title'])
        print('채용마감시간: ', v.select('span.date')[0].text.strip())
        print()
        print()
  
# 웹 브라우저 종료
browser.close()


        
        

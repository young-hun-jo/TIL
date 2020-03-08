
# selenium 임포트

from selenium import webdriver
import time
from selenium.webdriver.common.by import By  # 웹드라이버가 언제동안까지 기다려주겠다
from selenium.webdriver.support.ui import WebDriverWait # 위의 By임포트와 비슷한 의미이며 자주 같이쓰임
from selenium.webdriver.support import expected_conditions as EC # 웹드라이버가 어떤 상태까지 기다려주겠다며 By와 같이 자주쓰임
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--Headless") # 웹브라우저를 화면에 띄우지 않고 내부적으로 실행

# webdriver 활성화
browser = webdriver.Chrome("C:/webdriver/chrome/chromedriver.exe", options=chrome_options)

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈 설정
browser.set_window_size(1920, 1280)    # 참고로 maximize(), minimize() 도 가능

# 페이지 이동
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# 1차 페이지 내용
#print("Before contents : {}".format(browser.page_source))   # 성공!

# 제조사별 더보기 클릭 1
# Explicitly wait
WebDriverWait(browser, 5) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
#참고로 Copy XPATH, CSS selector 할때는 특정 하나만 지정할 때 유용!

# 제조사별 더보기 클릭 2 -> 권장은 x 
# Implicitly wait
#time.sleep(2)  ----> 파이썬 인터프리터의 동작도 멈춰버리게 하기 때문에 별로 권장 x
#browser.find_element_by_xpath('').click()

# 원하는 모델 카테고리 출력
WebDriverWait(browser, 3) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[20]/label'))).click()

# 2차 페이지 내용
#print("After contents : {}".format(browser.page_source))

time.sleep(2)   # 쉬어주기같은 개념..

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 소스코드 정리
#print(soup.prettify())

# 메인 상품 리스트 선택
hp_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

# 상품 리스트 확인
#print(hp_list)

# 필요 정보 추출
for v in hp_list:
    if not v.find('div', class_='ad_caster.ad_section'):
        # 태그정보 출력
        # 상품명, 이미지, 가격
        print(v.select('p.prod_name > a')[0].text.strip())
        print(v.select('a.thumb_link > img')[0]['data-original'])
        print(v.select('p.price_sect > a')[0].text.strip())
    
    print()

# 브라우저 종료
browser.close()
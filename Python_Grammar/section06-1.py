# Selenium 사용 실습(1) - 설정 및 기본 테스트
# 웹드라이버 지속적으로 업데이트 되니 지속 다운로드 필요!

# selenium 임포트
from selenium import webdriver     # 참고로 프로젝트명 = selenium으로 하면 import 에러가 뜬다..!

# webdriver 설정(크롬, 파이어 폭스 등)
browser = webdriver.Chrome('C:/webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기 - 왜? 컴퓨터마다 사양이 다르기 때문에 사양이 느릴경우에는 시간이 필요..보통 관행적으로 작성
browser.implicitly_wait(5)  # 5 -> 5초 대기

# 속성 확인
print(dir(browser))

# 브라우저 사이즈 설정
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window() 사용가능

# 페이지 이동
browser.get("https://www.daum.net")

# 페이지 내용
print('Page contents : {}'.format(browser.page_source))
print()

# 세션 값 출력
print('Session ID : {}'.format(browser.session_id))

# 타이틀 출력
print('title : {}'.format(browser.title))

# 현재 URL출력 
print('URL : {}'.format(browser.current_url))

# 현재 쿠키 정보 출력
print('Cookies : {}'.format(browser.get_cookies))

# 검색장 input 선택
element = browser.find_element_by_css_selector("div.inner_search > input.tf_keyword")

# 검색어 입력
element.send_keys("bts")

#검색(Form submit) - 엔터키 쳐주는거!
element.submit()

#스크린 샷 저장1 - 중간 점검용으로도 잘 진행되고 있는지 확인용
browser.save_screenshot("C:/bts1.png")

#스크린 샷 저장2
browser.get_screenshot_as_file("C:/bts2.png")

#브라우저 종료
browser.quit()














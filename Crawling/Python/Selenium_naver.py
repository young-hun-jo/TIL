'''
네이버 검색어 사용자 정의해서 정보 갖고오기
'''

# selenium import
from selenium import webdriver 

# webdriver 활성화
browser = webdriver.Chrome('C:/webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(6)

# 브라우저 사이즈 설정
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get("https://www.naver.com")

# 검색창 input 설정
element = browser.find_element_by_css_selector('span.green_window > input.input_text')
# 검색어 입력
element.send_keys("아이유")

# form submit 쳐주기(엔터키 쳐주기)
element.submit()

# 스크린샷
browser.save_screenshot("C:/아이유1.png")
browser.get_screenshot_as_file("C:/아이유2.png")

# 브라우저 종료
browser.quit()



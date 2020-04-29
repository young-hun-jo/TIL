"""
인터넷 포털 ZUM 페이지 검색어 사용자 정의해서 갖고오기
"""

# Selenium import
from selenium import webdriver

# 웹드라이버 활성화
browse = webdriver.Chrome("C:/webdriver/chrome/chromedriver.exe")

# 웹드라이버 접속 대기
browse.implicitly_wait(5)  # 5초 대기

# 속성확인
print(dir(browse))

# 웹 페이지 이동
browse.get("http://zum.com/")

# 검색어 input 설정
element = browse.find_element_by_css_selector("div.bg_box > input")

# 검색어 입력!
element.send_keys("낭만닥터김사부2")

# 엔터키 쳐주기 (form submit)
element.submit()

# 잘 진행되고 있는지 스크린샷 찍기
browse.save_screenshot("C:/낭만닥터1.png")
browse.get_screenshot_as_file("C:/낭만닥터2.png")

# 브라우저 종료
browse.quit()





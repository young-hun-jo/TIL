# Section05-3
# BeautifulSoup
# BeautifulSoup 사용 스크랩핑(3) - 로그인 처리

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Login 정보(개발자 도구)
login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': '',
    'password': ''
}

# Headers 정보
headers = {
    'User-Agent': UserAgent().chrome,
    'Referer': 'https://auth.danawa.com/login?url=http%3A%2F%2Fcws.danawa.com%2Fpoint%2Findex.php'
}

with req.session() as s:
    # Request(로그인 시도)
    res = s.post('https://auth.danawa.com/login', login_info, headers=headers)
    
    # 로그인 시도 실패시 예외
    if res.status_code != 200:
        raise Exception('Login failed.')
    
    # 본문 수신 데이터 확인
    # print(res.content.decode('UTF-8'))

    # 로그인 성공 후 세션 정보를 가지고 페이지 이동
    res = s.get('https://buyer.danawa.com/order/Order/orderList', headers=headers)

    # EUC-KR (한글 깨질 경우)
    # res.encoding = 'euc-kr'

    # 페이지 이동 수신 데이터 확인
    # print(res.text)

    # bs4 초기화
    soup = BeautifulSoup(res.text, "html.parser")

    # 로그인 성공 체크
    check_name = soup.find('p', class_="user")
    # print(check_name)
    
    if check_name is None:
        raise Exception('Login failed. Wrong Password.')
    
    # 선택자 사용
    info_list = soup.select("div.my_info > div.sub_info > ul.info_list > li")
    
    # 확인
    # print(info_list)

    # 이부분에서 재요청, 파일다운로드, DB 저장 등의 작업

    # 제목
    print()
    print('***** My info *****')

    for v in info_list:
        # 속성 메소드 확인
        # print(dir(v))
        
        # 필요한 텍스트 추출
        proc, val = v.find('span').string.strip(), v.find('strong').string.strip()
        
        # 최종 출력
        print('{} : {}'.format(proc, val))
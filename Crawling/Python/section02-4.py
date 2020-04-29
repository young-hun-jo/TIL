#파이썬 크롤링 기초
#lxml 사용 기초 스크래핑(2)

import requests 
from lxml.html import fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """
    #세션이란 : 세션정보를 갖고 흐름이 끊기지 않도록(로그인이 계속되어있는)
    session = requests.Session()  
    #스크랩핑 대상 URL   urlopen써서 넘겨도되긴함  get방식과 post방식이 있는데 기밀성이 있어야하는걸 긁어올땐 post를쓰긴함
    response = session.get("https://naver.com")

    #신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    #딕녀서리확인  
    print(urls)
    #결과 출력
    for name, url in urls.items():
        #url 출력
        print(name, url)
        #파일 쓰기
        
def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}

    #태그 정보 문자열 저장
    root = fromstring(response.content)
    
    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
                           # // : 전체문서에서, / :하위의 ##항상 상위의 부모태그를가져오자
        # a 구조 확인
        #print(a)

        # a 문자열 출력
        #print(tostring(a, pretty_print=True))
        name, url = extract_contents(a)
        #딕셔너리 삽입
        urls[name] = url

    return urls

def extract_contents(dom):
    #링크 주소
    link = dom.get("href")

    #신문사 명
    name = dom.xpath('./img')[0].get('alt')
    # xpath('./img') 출력해서 [0]을 왜붙였는가? 리스트로 반환됨
    return name, link

  


# cssselect() 안에 . = 클래스, # = id를 의미함
# 그리고 ' '=띄어쓰기면 하위관계나타냄 
# 예를들어서 '.A .B' = A클래스 하위의 B클래스
# 'a.api_link' => a태그의 api_link클래스뜻함!


#스크래핑 시작
if __name__ == "__main__":
    main()
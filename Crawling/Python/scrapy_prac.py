import requests
import lxml.html

def main():
    # url 긁어올 주소 get
    response = requests.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=age&subType=20')

    # 가져올 신문 기사 리스트 
    urls = top_10_news(response)

    #결과 출력
    for url in urls:
        print(url)

# top_10_news 함수 만들기
def top_10_news(response):
    
    # url 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    tag = lxml.html.fromstring(response.content)

    # css 선택자 이용해서 필요한 태그 정보만 추출
    for a in tag.cssselect('.ranking_list .ranking_thumb > a'):
        url = a.get('title')
        urls.append(url)

    return urls
    
#스크래핑 시작
if __name__ == '__main__':
    main()

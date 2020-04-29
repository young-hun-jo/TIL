import requests
import lxml.html

def main():
    #스크래핑할 대상 url 작성
    response = requests.get('https://www.naver.com/')

    #정치 인기 top10 뉴스 
    urls = politic_top_10_news(response)

    for url in urls:
        print(url)

def politic_top_10_news(response):
    urls = []

    root = lxml.html.fromstring(response.content)

    for a in root.cssselect('.an_l'):
        url = a.get('href')
        urls.append(url)
    return urls

if __name__ == "__main__":
    main()
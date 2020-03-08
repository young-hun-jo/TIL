# 토트넘 홈페이지 NEWS 제목 스크래핑해오기

from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.tottenhamhotspur.com/tags/newstadium/").text

soup = BeautifulSoup(html, 'html.parser')

link1 = soup.select('div.ArticleLink__info > a')

for t in link1:
    print(t.text)
print()
print()
# 네이버 정치뉴스 top10 뉴스 제목 스크래핑 해오기

html_1 = requests.get("https://news.naver.com/").text

soup = BeautifulSoup(html_1, 'html.parser')

link2 = soup.select('ul.section_list_ranking > li > a')

for v in link2:
    print(v.text)











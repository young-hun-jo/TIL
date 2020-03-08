# 연습- 네이버 주식 정보 가져오기

import json
import urllib.request as req
from fake_useragent import UserAgent

# fake user-agent 정보
ua = UserAgent()
# headers 정보
headers = {
    'User-agent': ua.chrome,
    'referer':'http://finance.daum.net/'
}

# 내가뽑을 url 요청
url = 'http://finance.daum.net/content/news/news_top'

res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

#print('res',res)

#응답 데이터 str -> json변환 및 data값 출력
rank_json = json.loads(res)

#중간확인
#print(rank_json)

for elm in rank_json:
    print('contents : {}, title :{}'.format(elm['content'], elm['title']))


import requests
# 세션 활성화

with requests.Session() as s:
    r = s.get("https://www.daum.net")
    print(r.ok)

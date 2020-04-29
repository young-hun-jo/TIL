# 기본 스크래핑 실습
# Get 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청1(encar)
url = 'http://www.encar.com'

mem = urllib.request.urlopen(url)

# 여러 정보
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers: {}'.format(mem.getheaders()))
print('getcode:{}'.format(mem.getcode()))
print('read {}'.format(mem.read(100).decode('utf-8')))
                    #읽어올 바이트 수! 입력
print('parse:{}'.format(urlparse('http://www.encar.com?test=test').query))

# 기본 요청2(ipify)
Api = 'https://api.ipify.org'

# Get 방식 Parameter
values = {
    'format' : 'text' #text나 jsonp로 시도해보기
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

# 요청 URL 생성
URL = Api + '?' + params
print('Call URL : {}'.format(URL))

#수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신 데이터 티코딩
text = data.decode('UTF-8')
print('response : {}'.format(text))

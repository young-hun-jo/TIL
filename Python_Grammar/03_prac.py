import urllib.request
from urllib.parse import urlparse

API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

param = []

for num in [1012, 1013, 1014]:
    param.append(dict(ctxCd=num))
#print(param)


for x in param:
    # url 인코딩
    parameter = urllib.parse.urlencode(x)
    #print(parameter)

    # url 완성
    url = API + '?' + parameter
    print(url)

    # url 요청
    res_data = urllib.request.urlopen(url).read()
    #print(res_data)

    # url 디코딩
    content = res_data.decode('UTF-8')
    print('-' * 100)
    print(content)


# RSS = 사이트에서 보내주는 소식지라고 생각!
# # Get 방식 데이터 통신(2) - RSS
 
import urllib.request
import urllib.parse

#행정 안전부 
#행정 안전부 RSS API URL
API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

params = []

for num in [1001, 1007, 1012, 1013]:
    params.append(dict(ctxCd=num))

# 뭐가 출력되고 있는지 확인
#print(params)

# 연속해서 4번 요청
for c in params:
    #URL 인코딩
    parameter = urllib.parse.urlencode(c)

    #URL 완성
    url = API +"?"+parameter
    #URL 출력
    print('url :',url)

    #요청
    res_data = urllib.request.urlopen(url).read()
    #print(res_data)

    #URL 디코딩
    contents = res_data.decode('UTF-8')
    print('*' * 100)
    print('*' * 100)
    print('*' * 100)
    print('*' * 100)
    print(contents)

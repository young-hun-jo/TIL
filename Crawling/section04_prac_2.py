import json
import requests

s = requests.Session()

r = s.get("https://httpbin.org/stream/60")

# json 데이터 출력!
# print(r.text)

# 해당 데이터 인코딩 확인
print(r.encoding)

if r.encoding is None:
    r.encoding = 'UTF-8'

print('modified encoding : {}'.format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    #print(line)
    #print(type(line))  str로 출력됨... 이걸 dict형태로 바꾸기 위해선 json.loads() 사용
    line_j = json.loads(line)
    print(line_j)
    print(type(line_j))

for k, v in line_j.items():
    print('Key : {}, Value : {}'.format(k, v))

s.close()

# 200개 갖고오기
r = s.get("https://jsonplaceholder.typicode.com/todos")

#print(r.headers)

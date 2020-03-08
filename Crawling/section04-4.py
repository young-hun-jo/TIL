# chpater 4 requests 꼭 알기!
# Requests 
# requests 사용 스크래핑(3) - Rest API

# Rest API : GET, POST(로그인정보, 게시판에 작성할 긴내용), DELETE, PUT:UPDATE,REPLACE(FETCH : UPDATE, MODIFY)
# 왜쓸까? : URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET : www.movies.com/movies : 영화를 전부 조회
# GET : www.movies.com/movies/:id   : 아이디인 영화를 조회
# POST : www.movies.com/movies/ : 영화를 생성
# PUT : www.movies.com/movies/ : 영화를 수정
# DELETE : www.movies.com/movies/ : 영화를 삭제

### REST API 구글링 해서 개념 찾아보기!!!

import requests
# 세션 활성화
s = requests.Session()

# 예제1
r = s.get("https://api.github.com/events")

# 수신상태 체크 ( status 나 ok 방법 말고)
r.raise_for_status()  # 해당 url 없으면 예외처리 해줌!

#출력
# print(r.text)

#예제2
#쿠키설정(그동안 한 방법과 다른 정석의 방법)
jar = requests.cookies.RequestsCookieJar()
#쿠키 삽입
jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')
          #딕셔너리 형태
#요청
r = s.get('https://httpbin.org/cookies', cookies=jar)

#출력
print(r.text)

#예제3
r = s.get("https://github.com",timeout=5)
                                # 5초간 서버를 기다림
# 출력
#print(r.text)



#예제4
r = s.post("https://httpbin.org/post", data={'id':'test777','pw':'ddddd'}, cookies=jar)

#출력
print(r.text)


#예제5
# 요청(post)
payload1 = {'id':'test777','pw':'ddddd'}
payload2 = (('id','test777'),('pw','ddddd'))

r = s.post("https://httpbin.org/post", data=payload1)

#출력
print(r.text)


#예제6(PUT)

r = s.put("https://httpbin.org/put", data=payload1)

print(r.text)

#예제7(DELETE)
r = s.delete("https://httpbin.org/delete", data={'id' : 1})
                                        # id가 1인 걸 삭제해줘

#출력
print(r.text)

#예제7-2(DELETE)
r = s.delete("https://jsonplaceholder.typicode.com/posts/1")
print(r.text) #출력시 빈리스트로 출력 = 삭제된 거임!

s.close()









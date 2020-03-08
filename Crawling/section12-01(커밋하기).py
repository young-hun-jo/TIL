# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

#삽입 날짜 생성
now = datetime.datetime.now()
print('now :', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# sqlite3
print('sqlite3_version :',sqlite3.version)
print('sqlite3.sqite_version:',sqlite3.sqlite_version)

# DB생성 & Auto commit 설정  cf) Rollback
conn = sqlite3.connect('C://database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Curosr type:', type(c))

# 테이블 생성(데이터타입: TEXT, NUMERIC, INTEGER, REAL, BLOB)
                                                  #소수  #저장
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMIARY KEY, \
    username text, email text, phone text, website text, regdate text)")

#데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'JO', 'joyh1021@naver.com','010-1234-5678', \
    'jo.com', ?)", (nowDatetime,))
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?) ",
#(2,'PARK','park.daum.net','010-1111-2222','daum.net',nowDatetime))

#Many 삽입(튜플, 리스트)
userlist = (
    (2, 'lee','lee@kakao.com','010-3333-3333','kakao.com',nowDatetime),
    (3, 'choi','choi@zum.com','010-4444-4444','zum.com',nowDatetime),
    (4, 'kim','kim@gmail.com','010-5555-5555','gmail.com',nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
    VALUES (?,?,?,?,?,?)", userlist)

#테이블 데이터 삭제
conn.execute("DELETE FROM users")
print("users db deleted : ",conn.execute("DELETE FROM users").rowcount)

#conn.rollback() 하면 취소
#커밋 : isolation_leve = None 하면 자동커밋 on!

#끝에 반드시 접속해제하기위해 conn.close()해줘야함









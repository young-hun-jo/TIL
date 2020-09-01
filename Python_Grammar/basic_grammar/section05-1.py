#파이썬 흐름제어(제어문)
#조건문 실습
# if 조건문 : 

#예제1

if True:
    print('yes')

if False:
    print('no')

if False:
    print('no')
else:
    print('yes2')

#관계 연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print( a == b)

# 참 거짓 종류(T/F)
# 참 : "내용이있는 문자열", [내용], (내용), {내용}, 1
# 거짓 : "",[],(),{},0

city = ''
if city:
    print('True')

#논리 연산자
# and, or, not
a = 100
b = 60
c = 15
print('and:', a>b and b>c)
print('or :'  )
print('not:' ) 

# 산술 > 관계 > 논리 순서로 적용됨
print('ex1 :', )

score1 = 90
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print('합격')
else:
    print('불합격')

#다중조건문
num = 90

if num >= 90:
    print('등급 A', num)
elif num >= 80:
    print('등급 B', num)
else:
    print('꽝')

#중첩 조건문
age = 27
height = 175

if age >= 20:
    if height >= 170:
        print('A지망 지원 가능')
    elif height >= 160:
        print('B지망 지원 가능')
    else:
        print('지원 불가')
else:
    print('20세 이상 지원 가능')

print()
print()
print()
print()
print()
print()
print()
print()

#반복문 실습
# 코딩의 핵심 -> 조건 해결 중요!
#기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print('v1 is :', v1)
    v1 += 1 #증감을 해줘야 계속 다음숫자로넘어감

for v2 in range(10): # 0~9까지
    print('v2 is :', v2)

for v3 in range(1,11): #1부터 10까지나와!
    print('v3 is :', v3)

# 1부터 100까지 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print('1~100합:',sum1)

print('1~100 :', sum(range(1,101))) #sum함수는 리스트요소들 다 합함

print('1~100:', sum(range(1,101,2))) # 2개 증가단위로 건너 뛰어서 계산

# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트,튜플,집합, 딕셔너리
# iterable 리턴함수 : range, reversed, enumerate, filter, map, zip

names = ['kim','park','jo','choi','yoo']

for name in names:
    print('you are : ', name)

word = 'dreams'

for v in word:
    print('word :', v)

my_info = {
    'name':'kim',
    'age': 33,
    'city':'Daejeon'
}
#키, 밸류, 아이템 패턴 
for key in my_info:    # 키만 출력
    print('my_info', key)

for k in my_info.keys():
    print('my_info', k)

for v in my_info.values():
    print('my_info', v)

for k, v in my_info.items():
    print('my_info', k, v)



name = 'KennRY'

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

#break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print('found!')
        break
    else:
        print('not')

#for - else 구문(반복문이 정상적으로 수행된 경우 else 블럭 수행)
for num in numbers:
    if num == 100:
        print('found!')
        break
    else:
        print('not')
else:
    print('not found 33....')

#continue
lt = ["1",2,5,True,4.3,complex(4)]

for v in lt:
    if type(v) is float:
        continue # 실수형 요소 출력안하고 걍넘겨
    print('타입 : ', type(v))


# 리스트 일반적

numbers = []

for n in range(1,101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리헨션

numbers2 = [x for x in range(1,101)]
print(numbers2)

# ex)
q3 = ['갑','을','병','정']
q5 = [x for x in q3 if x != '정']
print(q5)
print('-------------------')
q6 = [x for x in range(1,101) if x % 2 != 0]
print(q6)


































































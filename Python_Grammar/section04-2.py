# 리스트, 튜플

#리스트(순서 o , 중복 o, 수정o, 삭제o)
a = []
b = list()
c = [1,2,3,4]
d = [10, 100, 'pen', 'eraser','pencil']
e = [10, 100, ['pen', 'eraser','pencil']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

#슬라이싱
print(d[0:3])
print(d[0:2])
print(e[2][1:2])
#연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

#리스트 수정, 삭제
c[0] = 77
print(c)
 ## 슬라이싱처리하면 요소들어가지만
 ## 인덱스로처리하면 이중리스트처럼 들어감
c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)

print()
print()
print()


#리스트 함수
y = [5, 2, 3, 1 ,4]

y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(2) #요소값을 입력 vs del함수는 인덱스를 넣음
print(y)
y.pop() #맨 마지막 요소를 빼버림
print(y)
ex = [88,77]
y.extend(ex) #요소로 연장해버림
print(y)
y.append(ex)

#삭제 : del , remove , pop

#튜플 (순서o, 중복o, 수정x, 삭제x)
#프로그램의 중요한 값(변경되면 안되는 값)에 사용시 자주 사용

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])
print(d[2:])
print(d[2][0:2])
print( c+ d)
print( c * 2)

#튜플 함수
z = (5, 2, 1, 3, 4)
print(z)
print(3 in z)
print(z.index(5))  #인덱스를 반환하는 함수!
print(z.count(1))











#del c[2] # 안됨

















































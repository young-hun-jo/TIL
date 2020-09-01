# 파일 단위하나하나 = 하나의 모듈
# 모듈들을 디렉토리적으로 구조적으로 관리하는 것 = 패키지
# 파이썬 모듈과 패키지
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리


#사용 1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)
print('ex 1 : ', Fibonacci.fib2(400))
print('ex 1 : ', Fibonacci().title)  # () 인스턴트화 시켜야함!

# 사용 2(클래스) 권장은 x...
from pkg.fibonacci import * #클래스가 여러일때 사용하긴하지만 이렇겐 하지말자 리소스낭비...

# 사용 3(클래스)
from pkg.fibonacci import Fibonacci as fb # as=일리아스

Fibonacci.fib(300)
print('ex 3 : ', fb.fib2(23))
print('ex 3 : ', fb().title)

#사용 4(함수)
import pkg.calculations as cal

print( 'ex4 :', cal.add(10, 100))
print( 'ex4 :',cal.mul(10, 1000))

#사용 5(함수) 필요한것만 골라쓸때 from~ import~ 
from pkg.calculations import divd as d
print('ex5 :', int(d(100, 10)))

#사용6

import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))












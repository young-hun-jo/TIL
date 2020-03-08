# 파이썬 예외처리의 이해

#예외 종류
#문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일을 알려줌, 문법 체크

# SyntaxError : 잘못된 문법

# NameError : 참조변수 없음
a = 10
b = 15

#print(c)

# ZerodivisionError : 0 나누기 에러
#print(10 / 0)

# IndexError : 인덱스 범위 오버
x= [10, 20, 30]
#print(x[3]) -> 에러남!

# KeyError : 키 에러
dic = {'name':'kim','age':33,'city':'seoul'}
#print(dic['hobby'])
print(dic.get('hobby')) #get함수쓰면 해당 key가 없다면 none으로 출력됨

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용ㅇ시에 예외
import time
print(time.time())
#print(time.month())

# ValueError : 참조 값이 없을 때 발생
x = [1, 3, 5]
#x.remove(10) ->에러남
#x.index(10) ->에러남


# FilenotFoundError
#f = open('/test.txt','r')
#없는 파일 읽고 쓰라할 때


# Type Error
x = [1.2]
y = (1,2)
z = 'test'

#print(x+y) -> 에러
#print(x+z) -> 에러

#########################################

#항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장

#예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
  #try에서 except로 감!
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

#예제1

name = ['kim','lee','park']

try:
    z = 'lee' # cho 일때는 에러발생으로 예외처리됨!
    x = name.index(z)
    print('{} found it! in name'.format(z))
except ValueError:
    print('Not found it- occured Error!')
else:
    print('oK! Else')

try:
    z = 'lee' # cho 일때는 에러발생으로 예외처리됨!
    x = name.index(z)
    print('{} found it! in name'.format(z))
except:
    print('Not found it- occured Error!')
else:
    print('oK! Else')



try:
    z = 'cho' # cho 일때는 에러발생으로 예외처리됨!
    x = name.index(z)
    print('{} found it! in name'.format(z))
except:
    print('Not found it- occured Error!')
else:
    print('oK! Else')
finally:
    print('finally ok!')

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('try')
finally:
    print('ok finally')


#예제 5
try:
    z = 'kim' # cho 일때는 에러발생으로 예외처리됨!
    x = name.index(z)
    print('{} found it! in name'.format(z))
except ValueError:   #계층적으로 표현.. 대신 순서 지켜야함!
    print('Not found it- occured Error!')
except IndexError:
    print('Not found it- occured Error!')
except Exception:
    print('Not found it- occured Error!')
else:
    print('oK! Else')
finally:
    print('finally ok!')

#예제 6
#예외를 직접 발생시킬 수 있음 :raise
# raise 키워드로 예외 직접 발생

try:
    a = 'kim'
    if a == 'kim':
        print('ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except  Exception as e:
    print(e)
else:
    print('ok')





















































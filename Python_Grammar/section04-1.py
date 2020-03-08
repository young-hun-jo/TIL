# 데이터 타입

v_str1 = 'niceman'
v_bool = True
v_str2 = 'goodboy'
v_float = 10.3
v_int = 7
v_dict = {"name":"kim","age":25}
v_tuple = 3, 5, 7
v_set = {7, 8, 9}
v_list = [3, 5, 7]

print(type(v_tuple))
print(type(v_str1))

i1 =39
i2 = 939
big_int1 = 99999999999999999999999999999999999
big_int2 = 88888888888888888888888888888888888
f1 = 1.234
f2 = 3.445
f3 = .5
f4 = 10.

result = f1*f2
print(result, type(result))

a = 5.
b = 4

print(type(a),type(b))
result2 = a+b
print(result2)

# 형 변환
# int, float, str, complex(복소수)
print(int(result2))

#단항 연산자
y = 100
y += 100 # -= , *= += 도 가능
print(y)

#수치 연산 함수
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1))

#문자열, 문자열연산, 슬라이싱

str1 = "I am a boy"
str2 = 'Nice man'
str3 = ''
str4 = str()
print(len(str1), len(str2), len(str3), len(str4))

escape_st1 = 'do you have a \"big\"'
print(escape_st1)
escape_st2 = 'tab\ttab\ttab'
print(escape_st2)
escape_st3 = 'I AM \'YOUR\' MAN'
print(escape_st3)

# Raw string
raw_s1 = r'C:\Programs\test\bin'
print(raw_s1)
raw_S2 = r"\\a\\a"
print(raw_S2)
raw_s3 = r'\n\npigs102\n'
print(raw_s3)

#멀티라인
multi = \
"""
문자열 
멀티라인 
테스트
"""
print(multi)

# 문자열 연산
# str_o1 = '*'
# str_o2 = 'abc'
# str_o3 = 'def'
# str_o4 = 'niceman'
# print(str_o1 * 100)
# print(str_o2 + str_o3)
# print(str_o1 * 3)
# print('a' in str_o4)
# print('z' not in str_o4)

# 문자열 형 변환
print(str(77))
# print(str(10.44))
# #문자열 함수

# a = 'nice man'
# b = 'orange'

# print(a.islower())
# print(b.endswith('b'))
# print(a.capitalize())
# print(a.replace('n','b'))
# print(list(reversed(b)))

a = 'niceman'
b = 'orange'

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])
















































































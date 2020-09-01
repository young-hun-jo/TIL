# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV파일 읽기 및 쓰기

#CSV : MIME형태 - text/csv  
# csv의 c는 comma...

import csv #csv파일 읽어올때 필요

#예제 1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 맨위에 있는 헤더(칼럼명) 제외하고 출력
    #확인
    print(reader)
    print(dir(reader)) #메소드 뭐쓸수있는 확인 가능
    # __iter__ -> 반복문가능

    for c in reader:
        print(c)

#예제 2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|') # delimiter로 구분자 알려줌!
    next(reader) # 맨위에 있는 헤더(칼럼명) 제외하고 출력
    #확인
    print(reader)
    print(dir(reader)) #메소드 뭐쓸수있는 확인 가능
    # __iter__ -> 반복문가능

    for c in reader:
        print(c)

#예제 3 (Dict 변환) 메소드 있음!
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items(): #dict으로 변환했으니까!
            print(k, v)
        print()

# 예제 4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./python Grammar/sample3.csv', 'w',newline='') as f:
    wt = csv.writer(f)                    #newline='' 줄바꿈 안할래!

    for v in w:   #조건(검증)이 있을때 
        wt.writerow(v)
#newline 옵션 없애면 open에서 줄바꿈해주고 또 csv.writer에서 줄바꿈해주어서 2줄 간격이 생김

#예제 5
with open('./resource/sample4.csv', 'w',newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) #for문 안쓰고 한번에 쓰기(조건 x때)


# XSL, XLSX 
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 이 있지만
# 주로 pandas를 씀(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd 

# sheetname = '시트명' or 숫자, header=3(3번째행을 헤더로 지정) , skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

#상위 데이터 확인
print(xlsx.head())
print()

#꼬리 데이터 확인
print(xlsx.tail())
print()

# 데이터 확인
print(xlsx.shape) # 행,열 어떤 구조인지 확인 (행, 열)

# 엑셀 or csv 다시 쓰기

xlsx.to_excel('./resources/result.xlsx', index=False) #index=False : 1,2,3...번호 안매겨!
xlsx.to_csv('./resources/result.xlsx', index=False)























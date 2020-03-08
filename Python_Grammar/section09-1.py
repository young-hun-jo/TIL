#파일 읽기, 쓰기
# 읽기 모드 :r  / 쓰기 모드(기존파일 삭제): w / 추가 모드(파일 생성 또는 추가): a
# .. : 상대경로,  . : 절대경로

# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f)) # f에 뭐 어떤 메소드들이 들어있는지 확인!
#반드시 close로 리소스 반환해야함!!
f.close()

#예제 2     with문은 close안해도 알아서 자동으로 리소스 반환함!
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c)) #한글자단위로 리스트로 반환
    print(iter(c)) 

#예제 3   한 줄 단위로 갖고옴 
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) # .strip 양쪽 공백 없애줌

#예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>', content) 
    content = f.read() #여기서부터 내용없음!
    print('>', content)
    #해도 한번밖에 출력안됨..! 

#예제 5 한문장씩 계속 읽어올때
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    #print(line)
    while line :
        print(line, end=' ')
        line = f.readline()
     #null(텍스트가 없을때)일때 false이기때문에 동작이 자동으로 중지댐

#예제 6
with open('./resource/review.txt', 'r') as f:
    content = f.readlines() #엔터(줄바꿈)을 기준으로 구분해서 리스트로 반환
    print(content)
    for c in content:
        print(c, end='******')

#예제 7
 score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
print('AVG : {:6.3}'.format(sum(score)/len(score)))
         # 6자리고 소수점 3자리까지나와라!

#파일 쓰기
#예제 1
with open('./resource/text1.txt','w') as f:
    f.write('Niceman!') #write('텍스트')

with open('./resource/text1.txt','a') as f:
    f.write('Goodman!\n')

#예제 2
from random import randint 
with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1,46)))
        f.write('\n')

#예제 4 리스트로된파일을 쓰기(w)
# writelines : 리스트를 파일로 저장하는 메소드
with open('./resource/text1.txt','w') as f:
    list = ['kim\n','park\n','joe\n']
    f.writelines(list)

#예제 5
with open('./resource/text1.txt','w') as f:
    print('test contents1!', file=f) #file파라미터넣어주면 파일에 직접 텍스트 추가가능
    print('test contents2!', file=f)
    











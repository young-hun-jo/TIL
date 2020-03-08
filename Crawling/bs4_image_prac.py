# BeautifulSoup 사용 스크래핑 - 이미지 다운

import os #폴더 생성 위해
import urllib.parse as rep # 검색어를 사용자 customizing 하기 위해
import urllib.request as req # url에 요청하고 urlopen하기 위해
from fake_useragent import UserAgent # 해당 url에 요청할 때 fake를 써서 접속하기 위해

from bs4 import BeautifulSoup

# Header정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [{'User-agent', UserAgent().ie}]
# Header정보 삽입
req.install_opener(opener)

#네이버 이미지 기본 url(크롬개발자 도구)
base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
#검색어
quote = rep.quote_plus('iu')
#URL 완성
url = base + quote

# 요청 url 확인
print('Request URL : {}'.format(url))

# tiger가 들어간 url open으로 할당
res = req.urlopen(url)

#이미지 저장 경로 설정
save_path = "C:/dsc_project/image_file"

#폴더 생성 시 예외 처리(오류 발생하면 프로그램 종류 ex)이미 해당폴더가 있다거나...)
try:
    #만드려는 폴더가 있는지 체크
    if not (os.path.isdir(save_path)):
        #없으면 폴더 생성
        os.makedirs(os.path.join(save_path))
except OSError as e:
    #에러 내용
    print('Folder creation failed')
    print('Folder name : {}'.format(e.filename)) 

    #런타임 에러 - 폴더가 없다면 더이상 이미지 저장하지말고 그냥 종료!
    raise RuntimeError('System error!')
else:
    #폴더가 생성이 되었거나 이미 존재하는 경우
    print('Folder is created')

# bs4 초기화
soup = BeautifulSoup(res, 'html.parser')

#print(soup.prettify())

# select 사용
img_list = soup.select("div.img_area._item > a.thumb._thumb > img")
#print(img_list)

# 리스트를 인덱스와 튜플형태로 출력 ! => for + enumerate
for i, img in enumerate(img_list, 1):
    print()
    print()
    #print(img['data-source'], i)

    # 저장 파일명 및 경로 설정
    fullFileName = os.path.join(save_path, save_path+str(i)+'.png')

    # 파일명 출력
    print(fullFileName)

    #다운로드 요청 (URL , 다운로드 경로)
    req.urlretrieve(img['data-source'], fullFileName)

#다운로드 완료시 출력
print('Download succeed!')

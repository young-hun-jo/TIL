'''
< 로그 다루는 방법1 >
1. 파이썬의 logging 라이브러리 이용
    - 로깅 정보는 레벨이 있음
    - debug > info > warning > error > critical
    - debug가 가장 상위. debug 요청하면 모든 정보 로깅다 됨

# 파이썬 logging 라이브러리 이용해보기
import logging
# 로그 저장할 파일과 저장할 에러 수준 정의하기
logging.basicConfig(filename='test.log',level=logging.ERROR)
# 로그 남길 부분에 로그 level에 맞추어 메세지 출력하도록 하기
logging.debug('debug') # debug 라고 메세지가뜸
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
'''

'''
< 로그 다루는 방법2 >
2. 파이썬 logging + Flask 함께 사용
    - 주요 logging handler(로그를 어떻게 다룰지) 지정
        a. FileHandler:파일로 로그를 저장
        b. RotatingFileHandler:파일로 로그를 저장하되, 파일이 정해진 사이즈 넘어가면 새로운 파일로 생성
        c. NTEventLogHandler:윈도우 시스템 로그로 남김
        d. SysLogHandler:유닉스 계열(리눅스같은 OS)시스템의 syslog로 남김
    - 서버 상에서 로그 파일이 계속 적재되면 다운을 일으키기 때문에 일반적으로 덮어씌우는 RotatingFileHandler사용
    - app.run인자에 debug=True면 로그정보 안남김(test용), debug=False면 로깅 남김(production용)
'''

from flask import Flask
app = Flask(__name__)
# app인자의 debug가 False일 때(production용=로깅 남김) 작동
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    # log다룰 핸들러 정의. log저장할 파일이름, 파일 당 용량, 파일 개수 임계치 설정
    file_handler = RotatingFileHandler('hun_server.log', maxBytes=2000, backupCount=10)
    # log로 저장할 error level 설정
    file_handler.setLevel(logging.WARNING)
    # 위에서 만들어준 에러 헨들러 app의 핸들러로 최종 추가!
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_found(error):
    #error를 만나면 위에서 만들어준 logger가 작동하도록 설정
    app.logger.error(error)
    return "<h1>404 Error</h1>", 404
    
@app.route('/login')
def login():
    data = {'hi':'younghun'}
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

from flask import Blueprint

# Blueprint 객체명 지정해주기
# Blueprint 이름 지정 : 이 이름이 밑에 라우팅 경로랑 달라도 상관없음!
blue_view = Blueprint('sub_server123', __name__)

#위에서 지정한 Blueprint 객체를 데코레이터로 하여 경로 지정 후 data 리턴
#라우팅 경로를 main_server의 url_prefix랑 같아도 상관은 없지만 이렇게 하면 헷갈릴 듯!
@blue_view.route('/sub_server1')
# 데코레이팅할 함수 이름이 blueprint 객체명과 같아선 안 됨!!
def sub_server():
    data = 'This is sub server page!'
    return data

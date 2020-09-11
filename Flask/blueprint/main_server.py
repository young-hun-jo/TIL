from flask import Flask
# sub_server 폴더의 page_view.py 임포트
from sub_server import page_view

app = Flask(__name__)
# sub_server 폴더의 page_view.py 를 blueprint로 등록
# 인자에는 '하위폴더 소스파일명.blueprint객체명' 과 그쪽으로 routing 디폴트 경로를 설정해주는 url_prefix 설정
app.register_blueprint(page_view.blue_view, url_prefix='/sub_server')

@app.route('/basic')
def basic_view():
    data = 'This is main sever page!'
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

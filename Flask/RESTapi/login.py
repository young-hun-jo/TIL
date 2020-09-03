from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/login')
def login():
    # request를 통해서 route 주소의 파라미터 값으로 넣어줌
    username = request.args.get('user_name')
    password = request.args.get('pass_word')
    email = request.args.get('e_mail')
    print(username, password, email)

    if username == 'younghun':
        data = {'auth' : 'access'}
        return jsonify(data)
    else:
        data = {'auth' : 'denied'}
        return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

## 동작순서 정리 ##
'''
1. flask py 파일에서 웹 서버를 구동시켜준다
2. html 파일에가서 action 취할 주소에 flask py 파일에서 구동해주는 서버 
주소에 맞게해주기
* 참고로 2번처럼 flask 웹 서버 주소랑 맞춰주지 않고 html 파일을 
Go live 실행해주면 Go live 전용 port번호로 따로 들어가기 때문에 
flask 웹 서버 주소 port번호랑 일치하지 않게 됨!
'''

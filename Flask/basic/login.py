from flask import Flask, request, jsonify, render_template
# bootstrap 템플릿의 css, js 동적 기능 사용하기 위해서 해당 파일들이 있는 url_path 지정(단, path는 /(slash)로 시작해야만 함. 현재디렉토리(.)이 들어가면 안 됨!)
app = Flask(__name__, static_url_path='/static')

@app.route('/login')
def login():
    email_address = request.args.get('email_address')
    password = request.args.get('password')
    if email_address == 'joyh1021@naver.com':
        return_data = {'auth':'access'}
    else:
        return_data = {'auth':'denied'}
    return jsonify(return_data)

@app.route('/html_test')
def hello_bootstrap():
    return render_template('login_raw.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

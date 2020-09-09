from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# Flask에서 error 다루기
# app.errorhandler(에러번호)사용
@app.errorhandler(404)
# 404 error를 인자로 받음
def page_not_found(error):
    # 끝에 에러번호 넣어도 됨
    return "<h1>404 Error</h1>", 404

@app.route('/login')
def login():
    data = {'hi':'younghun'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

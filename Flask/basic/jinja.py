from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/jinja_html/<user>')
def jinja_html(user):
    # jinja_html.html 파일에서 사용할 변수명 = 변수에들어갈 값 으로 정의
    region_lst = ['Seoul','Daejeon','Busan']
    return render_template('jinja_html.html', name=user, birth='1995-10-21', regions=region_lst)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')




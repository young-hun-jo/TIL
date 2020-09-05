from flask import Flask
app = Flask(__name__)
# route지정
@app.route('/hello')
def test():
    return "<h1>Hello Younghun!</h1>"
print(__name__)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8081', debug=True)
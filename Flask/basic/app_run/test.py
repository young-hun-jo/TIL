from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def hello():
    data = {'name':'younghun'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')

from flask import Flask
from sub_server import page_view_prac

app = Flask(__name__)
app.register_blueprint(page_view_prac.blue_view, url_prefix='/sub_server')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')


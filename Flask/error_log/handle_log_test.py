from flask import Flask
app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    error_handler = RotatingFileHandler('hun_test.log', maxBytes=2000, backupCount=5)
    error_handler.setLevel(logging.INFO)
    app.logger.addHandler(error_handler)

@app.errorhandler(404)
def page_not_found(error):
    # error를 만든 log handler가 처리해 저장
    app.logger.error(error)
    return "<h1>Page not found and restore its log<h1>", 404

@app.route('/login')
def login():
    data = 'younghun'
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')

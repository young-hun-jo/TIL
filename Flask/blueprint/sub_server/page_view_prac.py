from flask import Blueprint
blue_view = Blueprint('blue_view', __name__)

@blue_view.route('/blueview')
# 데코레이팅할 함수 이름이 blueprint 객체명과 같아선 안 됨!!
def blueview():
    data = 'This is sub server page !'
    return data

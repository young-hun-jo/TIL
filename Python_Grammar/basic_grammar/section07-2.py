# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 상속을 왜 사용? 코드의 생산성, 유지보수, 가독성 위해
# ex) 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름): 부모클래스

class car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'

class Bmwcar(car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your car name : %s' % self.car_name
    
class Benzcar(car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your car name : %s' % self.car_name
    
    def show(self):
        print(super().show())
        return 'Your cat name : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = Bmwcar('520D','sedan','red')

print(model1.color) #부모에서 가져옴
print(model1.type) 
print(model1.car_name) #자식에서 가져옴
print(model1.show()) #부모에서가져옴
print(model1.show_model()) #자식에서 가져옴
print(model1.__dict__)

# 메소드 오버라이딩
model2 = Benzcar('22od','suv','black')
print(model2.show())

# 부모 메소드도 같이 불러오기
model3 = Benzcar('330e','truck','silver')
print(model3.show())

# 상속 정보 확인 .mro()
print(Bmwcar.mro())
print(Benzcar.mro())

#예제2 다중상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

print(A.mro())



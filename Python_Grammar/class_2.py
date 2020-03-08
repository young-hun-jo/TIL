class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def rival(self, vs_name):
        print(self.name + "'s rival anmial is " + vs_name)

    def col(self, vs_color):
        print(self.name + "'s color is " + self.color + " and " + vs_color)
    

class creation(animal):
    def home(self, area):
        print("where is a habitat? " + area)


tiger = animal('tiger', 'yellow')
lion = creation('lion', 'white')

lion.rival('panda')
lion.col('blue')
lion.home('africa')
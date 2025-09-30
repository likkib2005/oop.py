class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def get_circumference(self):
        return 2*self.pi*self.radius #Here we are using self keyword 
circle_1=circle(4)
print(circle_1.get_circumference())

class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def get_circumference(self):
        return 2*circle.pi*self.radius #Here we are using class name circle 
circle_1=circle(45)
circle_2=circle(10)
print(circle_1.get_circumference())
print(circle_2.get_circumference())

class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=circle.pi*radius*radius
    def get_circumference(self):
        return 2*circle.pi*self.radius #Here we are using class name circle 
circle_1=circle(45)
circle_2=circle(10)
print(f"circumfrence of circle_1 is {circle_1.get_circumference()}")
print(f"circumfrence of circle_2 is {circle_2.get_circumference()}")
print(f"area of circle_1 is{circle_1.area}")
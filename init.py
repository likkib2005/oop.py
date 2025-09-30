class Instructor:
    def __init__(self):
        print("creating a new object")
Instructor_1=Instructor()
Instructor_1.name="likitha"
Instructor_1.address="palamaner"
print(Instructor_1.name)
print(Instructor_1.address)
Instructor_2=Instructor()
Instructor_2.name="Rithik"
Instructor_2.address="Banglore"
print(Instructor_2.name)
print(Instructor_2.address)

class Instructor:
    def __init__(self,name,address):
        print("creating a new object")
        self.name=name
        self.address=address
        self.followers=0 #default value
    def display(self):
        print("Hi")
Instructor_1=Instructor("likhitha","Palamaner")
print(Instructor_1.name)
print(Instructor_1.followers)
Instructor_1.display()
Instructor_2=Instructor("rithik","chennai")
print(Instructor_2.address)
print(Instructor_2.followers)
Instructor_2.display()
print(Instructor_2.display()) #we are not returning anything from the function 
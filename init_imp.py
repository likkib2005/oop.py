class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject):
        print(f"I am {self.name} and I am from {self.address}.I teach {subject}.")
    def update_followers(self,follower_name):
        self.followers+=1
Instructor_1=Instructor("likhitha","palamaner")
print(Instructor_1.name)
print(Instructor_1.followers)
Instructor_1.update_followers("narasimha")
print(Instructor_1.followers)
Instructor_1.display("python")
Instructor_2=Instructor("Rithik","Banglore")
print(Instructor_2.name)
print(Instructor_2.followers)
Instructor_2.display("Django")
Instructor_2.update_followers("Rithika")
print(Instructor_2.followers)

class Instructor:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.followers = []   # each instructor has their own followers list

    def display(self, subject):
        print(f"I am {self.name} and I am from {self.address}. I teach {subject}.")

    def update_followers(self, follower_name):
        self.followers.append(follower_name)  # add follower to the list
        print(f"{follower_name} started following {self.name}")
    def count_followers(self):
        return len(self.followers)
# Example usage
Instructor_1 = Instructor("Likhitha", "Palamaner")
Instructor_2 = Instructor("Rithik", "Bangalore")
Instructor_1.update_followers("Narasimha")
Instructor_1.update_followers("Rithika")
Instructor_2.update_followers("Prasanna")
print(f"{Instructor_1.name} has {Instructor_1.count_followers()} followers: {Instructor_1.followers}")
print(f"{Instructor_2.name} has {Instructor_2.count_followers()} followers: {Instructor_2.followers}")
Instructor_1.display("Python")
Instructor_2.display("Django")
print(Instructor_1.count_followers())

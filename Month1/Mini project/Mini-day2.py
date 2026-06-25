
# task 1

class Car():
    pass

c1 = Car()

# task 2

class Player():
    name = "Ravi"
    game = "FIFA"
    print(name)
    print(game)

p1 = Player()

# task 3

class Browser():
    def open(self):
        print ("Browser Opened")

b1 = Browser()

# task 4

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def user_data(self):
        print(self.name)
        print(self.age)
        
u1 = User("Ravi",25)
u1.user_data()
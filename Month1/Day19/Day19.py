# task 1

class Game:
    pass

g1 = Game()

# task 2

class Tester():
    pass

qa1 = Tester()
qa1.name = "Ravi"
qa = Tester()
qa.name = "Teja"

print(qa1.name)
print(qa.name)

# task 3

class Game:
    def play(fuck):
        print ("Playing Game")
    
ply = Game()
ply.play()

# task 4

class Employee():
    def __init__(self, name, role):
        self.name = name
        self.role = role

obj = Employee("Ravi", "QA")

print(obj.name, obj.role)

# task 5
class BasePage():
    def open(self):
        print ("Browser Opened")

class LoginPage(BasePage):
    pass

lp = LoginPage()
lp.open()

# task 6

class LoginPage():
    def __init__(self,url):
        self.url = url
    def open_page(self):
            print (f"Opening:{self.url}")

odj = LoginPage("google.com")
odj.open_page()
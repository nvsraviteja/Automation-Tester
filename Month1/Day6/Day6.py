# movie
age = int(input("enter the age:"))

if age >= 18:
    print ("eligible for movie")
else:
    print ("not eligible for movie")

#game
Health = int(input("enter the health:"))

if Health > 0:
    print ("Player alive")
else:
    print ("Game Over")

#bike

fuel = int(input("enter the fuel:"))

if fuel < 15:
    print ("refuel the bike")
else:
    print ("fuel is sufficient")

#API

API_status = int(input("enter the status code:"))

if API_status == 200:
    print ("API pass")
else:
    print ("API fail")  

# Login

Password = input("enter the password:")

if Password == "1234":
    print ("login successful")
else:
    print ("login failed")

# Game reward

level = int(input("enter the level:"))

if level >= 50:
    print ("reward unlocked")
else:
    print ("Keep Grinding") 

# Mini project

pass_percentage = int(input("enter the pass percentage:"))

if pass_percentage >= 80:
    print ("release approved")

else:
    print ("release rejected")


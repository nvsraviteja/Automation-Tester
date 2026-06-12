
### Task 1
a = int(input("enter the percentage:"))
if a < 20:
    print ("low battery")
# task 2
b = int(input("enter the age:"))
if b >= 18:
    print ("eligible for movie")
# task 3
c = int(input("enter the number of KM driven on bike:"))
if c > 3000:
    print ("service is due")
#task 4
d = int(input("enter the level:"))
if d >= 50:
    print ("elite level")
#task 5
e = int(input("enter the status code:"))
if e == 200:
    print ("ok")

###
# bonus challenge 

Health = int(input("enter the health:"))
Ammo = int(input("enter the ammo:"))
Level = int(input("enter the level:"))

if Health <= 20:
    print ("low health")

if Ammo == 0:
    print ("out of ammo")

if Level >= 25:
    print ("Special Ability Unlocked")
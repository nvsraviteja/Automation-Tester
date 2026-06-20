
# Task 1
tests = ["Login", "Payment", "Logout"]

tests.insert(1,"Profile")

print (tests)

# task 2

games = ["FIFA", "PUBG", "Minecraft", "Valorant"]

games.pop(2)

print(games)

# task 3

bugs = ["Crash", "Audio", "Login"]

bugs.clear()

print(bugs)

# TASK 4

suite = ["Smoke", "Regression", "API"]

if "API" in suite:
    print ("Found")
else: 
    print("Not Found")

# Task 5

bugs = ["Crash Bug", "Audio Bug"]

if "Login Bug" not in bugs:
    print ("New Bug")

# bonus

bonus_suite = ["Login", "Payment"]

bonus_suite.insert(1, "Profile")
bonus_suite.pop()

if "Login" in bonus_suite:
    print ("exists")

print (bonus_suite)
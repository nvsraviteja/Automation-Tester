

# task 1
tests = ["TC1", "TC2"]

try:
    print(tests[5])
except:
    print ("Invalid Test Index")

# Task 2

user = {
    "name": "Ravi"
}

try: 
    print (user["age"])
except:
    print ("Age Not Found")


# task 3
TypeError


# task 4
num = "abc"

try:
    int(num)
except:
    print("Invalid number")

# task 5

response = {
    "status": 200
}


try:
    print(response["token"])
except:
    print("Token Missing")

# 6

def safe_divide(a, b):

    try:
        return a/b
    except:
        return "Cannot divide by zero"
    

val = safe_divide(10,0)

print(val)
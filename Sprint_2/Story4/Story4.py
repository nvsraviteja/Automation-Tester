

# task 1

useri = input("Enter value")



try: 
    int(useri)
    print(useri)
except ValueError:
    print("Invalid number")

# task 2

user = input("Enter a number")



try:
    user = int(user)

    div = 100/user
    print(div)
except ValueError:
    print ("Please enter valid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")


# task 3

try:
    # try this code
except Exception as e:
    print (e)
finally:
    print("Program ended")

# task 4

def validate_age(age):
    if age < 18:
        raise ValueError("Age must be 18+")
    else:
        print ("Valid")

# task 5

response = {
    "status": 500
}

if "status" == 200 in response:
    print("true")
else:
    raise print("API Test Failed")
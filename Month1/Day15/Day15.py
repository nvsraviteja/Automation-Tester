
# task 1
user = {
    "name" : "Ravi",
    "role" : "QA",
    "experience" : 2
}

print (user)

#task 2

user_1 = {
    "name": "Ravi",
    "age": 25,
    "role": "QA"
}

print (user_1["name"])
print (user_1["role"])

# Task 3

user_2 = {
    "name" : "Ravi",
}

user_2["age"] = 25

print(user_2)

# tak 4

user_3 = {
    "name": "Ravi",
    "age": 25,
    "role": "QA"
}


print(user_3.keys())
print(user_3.values())

# task 5

response = {
    "status": 200,
    "message": "success"
}

if response["status"] == 200:
    print("Pass")
else:
    print ("Fail")


# Bonus

login_response = {
    "status": 200,
    "message": "Login Successful",
    "token": "abc123"
}

s_k = "status" in login_response
s_v = login_response["status"] == 200
t_k = "token" in login_response
if s_k and s_v and t_k:
    print ("Login Test Passed")
else:
    print ("Login Test Failed")
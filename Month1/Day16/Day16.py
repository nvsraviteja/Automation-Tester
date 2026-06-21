# task 1

def say_hello():
    print ("Hello Ravi")

say_hello()

# task 2

def show_game(game):
    print(game)

show_game("FIFA")
show_game("Minecraft")

# task 3

def add(a,b):
    return a+b

result = add(2,5)
print (result)
    
# task 4 output = Hi

# Task 5

def validate_status(status):
    if status == 200:
        return True
    else:
        return False

res = validate_status(200)
print(res)
res_1 = validate_status(400)
print(res_1)


# Bonus


def validate_login(response):
    stat = "status" in response
    stat_v = response["status"] == 200
    tok = "token" in response

    if stat and stat_v and tok:
        print (True)
    else:
        print (False)


inp = {
    "status": 200,
    "token": "abc123"
}

res_4 = validate_login(inp)
print(res_4)
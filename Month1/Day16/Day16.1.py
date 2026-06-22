

# Task 1

def count_failures(results):
    cf = 0
    for r in results:
        if r == "Fail":
            cf += 1
    
    return cf

res = ["Pass", "Fail", "Pass", "Blocked", "Fail"]

op = count_failures(res)
print (op)

# task 2

def has_duplicates(bugs):
    if len(bugs) != len(set(bugs)):
        return True
    else:
        return False
    
sets = ["Crash", "Audio", "Crash"]
val = has_duplicates(sets)
print (val)

# task 3

def validate_response(response):
    if "status" in response and  "message" in response and response["status"] == 200 and response["message"] == "success":
        return True
    else:
        return False


ip = {
    "status": 200,
    "message": "success"
}

de = validate_response(ip)

print (de)
     
# task 4

def reverse_list(items):
    new = []
    for i in items:
        new.insert(0,i)
    return new

ip = ["A", "B", "C"]

nnn = reverse_list(ip)

print (nnn)

# task 5

def highest_score(scores):
    high = 0
    for i in scores:
        if i > high:
            high = i

    return high

scr = [45, 78, 99, 12, 67]

hell = highest_score(scr)

print (hell)

# task 6
def validate_login(respons):
    if "status" in respons and  "token" in respons and "user" in respons and respons["status"] == 200 and len(respons["token"]) > 5:
        return True
    else:
        return False
    
ip = {
    "status": 200,
    "token": "abc12345",
    "user": "Ravi"
}


op = validate_login(ip)

print (op)


# final task 

def analyze_suite(results):
    cp = 0
    cf = 0
    cb = 0
    for i in results:
        if i == "Pass":
            cp += 1
        elif i == "Fail":
            cf += 1
        elif i == "Blocked":
            cb += 1

    dic = {
           "pass": cp,
           "fail": cf,
           "blocked": cb
    }
    return dic

val = ["Pass", "Fail", "Pass", "Blocked", "Fail", "Pass"]

new = analyze_suite(val)

print (new)
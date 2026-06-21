

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


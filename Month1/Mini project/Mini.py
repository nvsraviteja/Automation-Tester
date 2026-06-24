
results = [
    {"id": "TC101", "status": "Pass"},
    {"id": "TC102", "status": "Fail"},
    {"id": "TC103", "status": "Blocked"},
    {"id": "TC104", "status": "Fail"},
    {"id": "TC105", "status": "Pass"}
]

cp = 0
cf = 0
cb = 0
list = []

for r in results:
    for key,value in r.items():
        if "Pass" in value:
            print(key)
            cp += 1
        elif "Fail" in value:
            cf += 1
            list.append(r["id"])
        elif "Blocked" in value:
            cb += 1

print (f"Pass: {cp}\nFail:{cf}\nBlocked:{cb}\nFailed IDs:{list}")



def validate_login(response):
    if response["status"] == 200 and "token" in response:
        return True
    else:
        return False

login_response = {
    "token": "abc123",
    "status": 200
}

print(validate_login(login_response))




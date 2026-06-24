# round - 1
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
            # # print(key)
            cp += 1
        elif "Fail" in value:
            cf += 1
            list.append(r["id"])
        elif "Blocked" in value:
            cb += 1

# print (f"Pass: {cp}\nFail:{cf}\nBlocked:{cb}\nFailed IDs:{list}")

# round 2


def validate_login(response):
    if response["status"] == 200 and "token" in response:
        return True
    else:
        return False

login_response = {
    "token": "abc123",
    "status": 200
}

# print(validate_login(login_response))


# round 3


"""def res():
    try:
        if 200 == response["status"] and "token" == response:
            valid += 1
            return valid
    except:
        # print("keyerror")

for response in responses:
    valid = res(response)
    """
responses = [
    {"status": 200, "token": "abc"},
    {"status": 401},
    {"status": 200, "token": "xyz"},
    {"token": "oops"},
]
def res(test):
    valid = 0
    invalid = 0
    for response in test:
        try:
            if 200 == response["status"] and "token" in response:
                valid += 1
            else:
                invalid += 1
        except:
            invalid += 1

    return (f"Valid:{valid}\nInvalid:{invalid}")

output = res(responses)

# print (output)

# task 4


class BasePage():
    def click(self):
        print ("Element Clicked")

class LoginPage(BasePage):
    def __init__(self,username,password):
       self.username = username
       self.password = password
    def login(self):
        if self.username == "admin" and self.password == "1234":
            print ("Login Successful")
        else:
            print ("Login Failed")

username = input("enter username:")
password = input("enter password:")

basepage = BasePage()
basepage.click()

loginpage = LoginPage(username,password)
loginpage.login()

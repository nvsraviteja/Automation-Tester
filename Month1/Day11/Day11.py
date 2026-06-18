# Username Cleaner Pro
name = input("enter name:")

space_name = name.strip()

upper_name = space_name.upper()

print (upper_name)

#QA Response Checker Pro

api_response = input("enter API response:")

api_res = api_response.lower()

if "success" in api_res:
    print ("Passed")
elif "error" in api_res:
    print ("Failed")
else:
    print ("Unknown Response")
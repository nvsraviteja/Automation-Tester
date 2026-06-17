# task 6
name = input("enter name:")
print(name.strip())


# task 7 
password = input("enter password:")

length = len(password)

if length < 8:
    print("Weak Password")
else:
    print("Strong Password")

# task 8
response = input("enter response:")

if "success" in response:
    print ("Passed")

else:
    print ("failed")


# bonus

ai_response = input("enter AI_Response:")

ai_res = ai_response.lower()

if "hack" in ai_res:
    print ("Unsafe Response")

else:
    print ("Safe Response")
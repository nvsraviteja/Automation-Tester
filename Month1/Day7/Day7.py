# Task 1
grade = int(input("enter the grade:"))

if grade >= 90:
    print ("Grade: A")
elif grade >= 80:
    print ("Grade: B")
elif grade >= 70:
    print ("Grade: C")
else:
    print ("Fail")

# task 2

severity_score = int(input("enter the severity score:"))

if severity_score >= 90:
    print ("Critical")
elif severity_score >= 75:
    print ("High")
elif severity_score >= 50:
    print ("Medium")
else:
    print ("Low")   

# task 3

age = int(input("enter the age:"))

Ticket_status = int(input("enter the ticket status (1 = yes, 0 = no):"))

if age >= 18 and Ticket_status == 1:
    print ("Eligible for movie")
else:
    print ("Not eligible for movie")

# task 4

password = int(input("enter the password:"))
otp = int(input("enter the OTP:"))

if password == 1234 or otp == 5678:
    print ("Login successful")
else:
    print ("Login failed")  

# task 5

pass_percentage = int(input("enter the pass percentage:"))
open_bugs = int(input("enter the open bugs:"))

if pass_percentage >= 85 and open_bugs == 0:
    print ("Release approved")
else:
    print ("Release rejected")  

# task 6

logged_in = int(input("enter the logged in status (1 = yes, 0 = no):"))
premium_user = int(input("enter the premium user status (1 = yes, 0 = no):"))

if logged_in == 1:
    if premium_user == 1:
        print ("Access to premium content")
    else:
        print ("Access to regular content")
else:
    print ("Please log in to access content")

# task 7

open_bugs = int(input("enter the open bugs:"))
crash_count = int(input("enter the crash count:"))

if open_bugs >= 20 and crash_count >= 5:
    print ("High risk")
elif open_bugs >= 10
    print ("Medium risk")
else:
    print ("Low risk")


# bonus challenge

age = int(input("enter the age:"))
logged_in_status = int(input("enter the logged in status (1 = yes, 0 = no):"))
subscription_status = int(input("enter the subscription status (1 = basic, 2 = premium):"))
region_allowed = int(input("enter the region allowed status (1 = yes, 0 = no):"))

if logged_in_status == 1:
    if age >= 18:
        if region_allowed == 1:
            if subscription_status == 2:
                print ("Premium Access Granted")
            else:
                print ("Basic Access Granted")
        else:
            print ("Content Unavailable")
    else:
        print ("Restricted Content")
else:
    print ("Access Denied")
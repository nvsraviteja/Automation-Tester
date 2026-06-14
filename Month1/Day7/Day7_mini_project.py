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
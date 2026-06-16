build_number = int(input("enter the build number:"))
total_test_cases = int(input("enter the total test cases:"))
executed_test_cases = int(input("enter the executed test cases:"))
passed_test_cases = int(input("enter the passed test cases:"))
failed_test_cases = int(input("enter the failed test cases:"))
open_bugs = int(input("enter the open bugs:"))

print (f"Build number: {build_number}")
print (f"Total test cases: {total_test_cases}")
print (f"Executed test cases: {executed_test_cases}")
print (f"Passed test cases: {passed_test_cases}")
print (f"Failed test cases: {failed_test_cases}")
print (f"Open bugs: {open_bugs}")

execution_percentage = (executed_test_cases / total_test_cases) * 100
pass_percentage = (passed_test_cases / executed_test_cases) * 100
fail_percentage = (failed_test_cases / executed_test_cases) * 100

print (f"Execution percentage: {execution_percentage}%")
print (f"Pass percentage: {pass_percentage}%")
print (f"Fail percentage: {fail_percentage}%")

if execution_percentage >= 90:
    print ("Execution Status : Good")
else:
    print ("Execution Status : Low")

if pass_percentage >= 85:
    print ("Quality Status : Good")
else:
    print ("Quality Status : Poor")     

if open_bugs == 0:
    print ("Bug Status : Clean")
else:
    print (f"Issues remaining : {open_bugs}")

if execution_percentage >= 90:
    if pass_percentage >= 85:
        if open_bugs == 0:
            print ("Release Status : Approved")
        else:
            print (f"Issues remaining : {open_bugs}")
    else:
        print ("Quality Status : Poor")
else:
    print ("Execution Status : Low")




if execution_percentage >= 90 and pass_percentage >= 85 and open_bugs == 0:
    print ("Release Status : Approved")
else:
    print ("Release Status : Rejected")
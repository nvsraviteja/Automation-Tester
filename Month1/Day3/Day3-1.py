Total = int(input("total number of testcases:"))
Executed = int(input("number of testcases executed:"))
Pass = int(input("number of testcases passed:"))
Open = int(input("number of testcases open:"))

print (f"Total testcases:{Total}")
print (f"Executed testcases:{Executed}")
print (f"Passed testcases:{Pass}")
print (f"Open testcases:{Open}")

EP = Executed/Total*100
PP = Pass/Total*100

print(f"Execution persentage:{EP}")
print(f"Pass percentage:{PP}")
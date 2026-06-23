
results = ["Pass", "Fail", "Pass", "Blocked", "Fail"]


count_of_pass = 0
count_of_fail = 0
count_of_blocked = 0

for result in results:

    if result == "Pass":
        count_of_pass += 1
    elif result == "Fail":
        count_of_fail += 1
    elif result == "Blocked":
        count_of_blocked += 1

sum = (f"Test Execution Summary \n Pass: {count_of_pass} \n Fail: {count_of_fail} \n Blocked: {count_of_blocked}")

with open("report.txt", "w") as f:
    f.write(sum)


"""def log(res):
    con = 0
    list = []
    for i in range(0,len(res)+1) and res:
        con += 1
        app = f"TC{con}", i
        list.append(app)
    return list
    

sum = log(results)

print (sum)

"""
with open("execution.log","a") as a:
        a.write(f"\nPrevious Run")
con = 0
for i in range(0,len(results)+1) and results:
    con += 1
    with open("execution.log","a") as a:
        a.write(f"\nTC{con}:{i}")




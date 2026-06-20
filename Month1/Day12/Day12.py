# task 5
games = ["Skyrim", "We need to go deeper", "Fallguys"]

for i in games:
    print(i)

# task 6
bugs = ["Login Bug", "Audio Bug"]
bugs.append("Crash Bug")
bugs.remove("Audio Bug")
print(bugs)

# task 7

results = ["Pass", "Fail", "Pass", "Fail", "Blocked"]


count = 0
for result in res:
    if result == "fail":
        count +=1

print(count)


# bonus 

results = ["Pass", "Fail", "Pass", "Blocked", "Fail", "Pass"]

countp = 0
countf = 0
countb = 0

for res in results:
    if res == "Pass":
        countp += 1
    elif res == "Fail":
        countf += 1
    elif res == "Blocked":
        countb += 1


print (f"Pass: {countp}")
print (f"Fail: {countf}")
print (f"Blocked: {countb}")




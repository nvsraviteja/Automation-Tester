# Task 1

tup = ("Chrome", "Firefox", "Safari")

print (tup[1])


nums = {1, 2, 2, 3, 3, 4}

print(nums)

# Task 4

bugs = ["hey", "Hello", "hello", "hey"]

if len(bugs) != len(set(bugs)):
    print ("Duplicates Found")
else:
    print ("No Duplicates")


# Bonus


emails = [
    "a@test.com",
    "b@test.com",
    "c@test.com",
    "a@test.com",
    "b@test.com"
]

total = len(emails)
unique = len(set(emails))
dup = total - unique

print (f"Total: {total}")
print (f "Unique: {unique}")
print(f "Duplicates: {dup}")
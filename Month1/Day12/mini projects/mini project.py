"""
# task 1

username = input("enter username:")

u_n = username.lower().strip()

print (u_n)
print (len(u_n))


# Task 2

text = input("enter text:")

txt = text.lower()
count = 0
for char in txt:
    if  "a" in char or "e" in char or"i" in char or"o" in char or"u" in char:
        count += 1
print (count)

# task 3

for i in range (1,11):
    if i == 5:
        continue
    print (i)
"""
# task 4

pas = input("enter pass:")

cu = 0
cn = 0
cs = 0
for char in pas:
    if char.upper() == char and char.upper() != char.lower() and cu < 1:
        cu += 1
    if char in "0123456789":
        cn += 1
    if "@" in char or "#" in char or "$" in char:
        cs += 1

if cu >= 1 and cn >= 1 and cs >= 1:
    print ("Valid Password")
else:
    print ("Invalid Password")
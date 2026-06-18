# Task 3
user_input = input("enter user input:")

u_i = user_input.lower()

count = 0
for char in u_i:
    if "a" in char or "e" in char or "i" in char or "o"in char  or "u"in char :
        count += 1
print (count)


#task 4

password = input("enter password:")

count = 0
for char in password:
    if "0" in char or "1" in char or "2" in char or "3" in char or "4" in char or "5" in char or "6" in char or "7" in char or "8" in char or "9" in char or "0" in char :
        count += 1
    
if count >= 1:
    print ("Valid password")
else: 
    print ("Invalid Password")


# task 5

pswd = input("enter password:")

count = 0
for char in pswd:
    if char.upper() == char and char.upper() != char.lower():
        count += 1


if count >= 1:
    print ("Valid Password")
else:
    print ("Invalid Password")

# task 6

all_pass = input("enter pass:")

count_s = 0
count_u = 0
count_n = 0

for char in all_pass:
    if char.upper() == char and char.upper() != char.lower():
        count_u += 1
    if "0" in char or "1" in char or "2" in char or "3" in char or "4" in char or "5" in char or "6" in char or "7" in char or "8" in char or "9" in char or "0" in char :
        count_n += 1
    if  char == "@" or char == "#" or char == "$":
        count_s += 1


if count_s >= 1 and count_u >= 1 and count_n >= 1:
    print ("Valid password")
else:
    print("invalid Password")

## Bonus

ai_res = input("enter ai response:")


ai_r = ai_res.lower()

count_h = 0
count_e = 0
count_b = 0

if "hack" in ai_r:
    count_h += 1

if "exploit" in ai_r:
    count_e +=1

if "bypass" in ai_r:
    count_b +=1


if count_h > 0 or count_e > 0 or count_b >0:
    print ("Unsafe Response")
    print (count_b+count_h+count_e

password = input("enter password:")

count = 0
for char in password:
    ##if "0" in char or "1" in char or "2" in char or "3" in char or "4" in char or "5" in char or "6" in char or "7" in char or "8" in char or "9" in char or "0" in char :
    if char.isdigit():
        count += 1
    
if count >= 1:
    print ("Valid password")
else: 
    print ("Invalid Password")
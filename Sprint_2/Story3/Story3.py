
# task 1

with open("reporter.txt", "w") as f:
    f.write("mode")

# task 2
with open("reporter.txt", "a") as f:
    f.write("Blocked: 2")

# task 3

with open("file.txt","r") as f:
    for line in f.readlines():
        clean = line.strip()
        print(clean)

# task 4

import json

with open("config.json", "r") as j:
    data = json.load(j)

print(data["browser"])
print(data["timeout"])


# task 5

import json

data = {
    "passed": 20,
    "failed": 5
}
with open("results.json", "w") as j:
    json.dump(data, j)


# task 6

import csv

with open("users.csv", "r") as c:
    rows = csv.reader(c) 
    for row in rows:
        print (row)


# task 7
import csv 

with open("results.csv", "w") as c:
    writer = csv.writer(c)
    writer.writerow (["TC101", "Pass"])
    writer.writerow (["TC102", "Fail"])



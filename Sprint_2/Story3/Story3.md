# Sprint 2 — Story 3: File Handling, JSON & CSV

## Topics Covered
1. File Handling Refresher
2. File Modes (`r`, `w`, `a`)
3. Reading Files (`read()`, `readlines()`, `strip()`)
4. Writing Files (`write()`)
5. File Handling in QA
6. JSON Basics
7. Reading JSON (`json.load()`)
8. Accessing JSON Data
9. Writing JSON (`json.dump()`)
10. CSV Basics
11. Reading CSV (`csv.reader()`)
12. Accessing CSV Data
13. Writing CSV (`csv.writer()`, `writer.writerow()`)
14. Story 3 QA Framework Usage

---

## 1. File Handling Refresher

**File handling** is how Python programs read data from files (like text, JSON, or CSV files) and write data back to them. This is essential for tasks like reading test data, saving logs, or generating reports.

The basic pattern to work with a file in Python:

```python
file = open("example.txt", "r")
content = file.read()
file.close()
```

But the **recommended** approach is to use a `with` block, which automatically closes the file for you — even if an error occurs:

```python
with open("example.txt", "r") as file:
    content = file.read()
# file is automatically closed here, even if an error occurred above
```

**Why `with` is preferred:**
- No risk of forgetting `file.close()`.
- Cleaner, more readable code.
- Safer — file is closed properly even if an exception is raised inside the block.

---

## 2. File Modes

When opening a file, you specify a **mode** that tells Python what you intend to do with it.

### Read Mode (`r`)
Opens the file for **reading only**. This is the default mode if none is specified.
- Raises a `FileNotFoundError` if the file doesn't exist.
- Does **not** modify the file's existing content.

```python
with open("data.txt", "r") as file:
    content = file.read()
```

### Write Mode (`w`)
Opens the file for **writing**.
- **Creates the file** if it doesn't exist.
- **Overwrites/erases all existing content** if the file already exists — use with caution!

```python
with open("data.txt", "w") as file:
    file.write("This replaces everything in the file.")
```

### Append Mode (`a`)
Opens the file for **writing**, but adds new content to the **end** of the file instead of overwriting it.
- **Creates the file** if it doesn't exist.
- Preserves existing content.

```python
with open("data.txt", "a") as file:
    file.write("\nThis line is added to the end.")
```

### Quick Comparison

| Mode | Meaning | File Must Exist? | Erases Existing Content? |
|---|---|---|---|
| `r` | Read | Yes | No |
| `w` | Write | No (creates it) | Yes |
| `a` | Append | No (creates it) | No |

---
## 3. Reading Files

### `read()`
Reads the **entire file content** as a single string.

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### `readlines()`
Reads the file and returns a **list of strings**, where each string is one line from the file (including the newline character `\n` at the end of each line).

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    # ['First line\n', 'Second line\n', 'Third line']
```

You can then loop through the lines:

```python
with open("data.txt", "r") as file:
    for line in file.readlines():
        print(line)
```

### `strip()`
A **string method** (not file-specific) that removes leading/trailing whitespace — including the `\n` newline character left over from `readlines()`.

```python
with open("data.txt", "r") as file:
    for line in file.readlines():
        clean_line = line.strip()
        print(clean_line)  # no trailing newline or extra spaces
```

**Without `strip()`:** `"First line\n"` → printed with an extra blank line after it.
**With `strip()`:** `"First line"` → clean output.

---

## 4. Writing Files

### `write()`
Writes a **string** to the file. It does **not** automatically add a newline — you need to include `\n` yourself if you want line breaks.

```python
with open("output.txt", "w") as file:
    file.write("Line one\n")
    file.write("Line two\n")
    file.write("Line three")
```

**Resulting file content:**
```
Line one
Line two
Line three
```

> **Note:** `write()` only accepts strings. If you want to write a number or other data type, convert it first using `str()`.

```python
with open("output.txt", "w") as file:
    score = 95
    file.write("Score: " + str(score))
```

---
## 5. File Handling in QA

File handling is widely used in QA automation for tasks such as:

- **Reading test data** from text/CSV/JSON files instead of hardcoding values in test scripts.
- **Writing test logs** to track what happened during a test run.
- **Storing test results/reports** in a structured format for later review.
- **Reading configuration files** (URLs, credentials, environment settings) used across multiple tests.

### Example: Logging Test Results

```python
def run_test_and_log(test_name, result):
    with open("test_log.txt", "a") as log_file:
        log_file.write(f"{test_name}: {result}\n")

run_test_and_log("test_login", "PASSED")
run_test_and_log("test_logout", "FAILED")
```

Using **append mode (`a`)** here is important — each test run adds to the log without erasing previous results.

---

## 6. JSON Basics

**JSON** (JavaScript Object Notation) is a lightweight, text-based data format used to store and exchange structured data. It looks very similar to a Python dictionary.

### Example JSON Data

```json
{
  "name": "Alice",
  "age": 25,
  "is_active": true,
  "skills": ["Python", "Selenium", "API Testing"]
}
```

### Why JSON Matters in Programming/QA
- Most **APIs** send and receive data in JSON format — so JSON handling is critical for API testing.
- Configuration files are often written in JSON.
- Test data sets can be stored as JSON for easy reading/writing.

Python's built-in `json` module lets you convert between JSON text and Python objects (dictionaries/lists).

```python
import json
```

---

## 7. Reading JSON

### `json.load()`
Reads JSON data **directly from a file** and converts it into a Python object (usually a dictionary or list).

**`user.json`**
```json
{
  "name": "Alice",
  "age": 25,
  "skills": ["Python", "Selenium"]
}
```

**Reading it:**
```python
import json

with open("user.json", "r") as file:
    data = json.load(file)

print(type(data))  # <class 'dict'>
print(data)
# {'name': 'Alice', 'age': 25, 'skills': ['Python', 'Selenium']}
```

> **Note:** There's also `json.loads()` (with an "s") which converts a JSON **string** (not a file) into a Python object. `load()` = from file, `loads()` = from string.

---
## 8. Accessing JSON Data

Once loaded, JSON data behaves just like a normal Python dictionary/list — you access it the same way.

```python
import json

with open("user.json", "r") as file:
    data = json.load(file)

print(data["name"])          # Alice
print(data["age"])           # 25
print(data["skills"][0])     # Python
print(data["skills"][1])     # Selenium

for skill in data["skills"]:
    print(skill)
```

If the JSON contains nested objects:

```json
{
  "name": "Alice",
  "address": {
    "city": "Hyderabad",
    "zip": "500001"
  }
}
```

```python
print(data["address"]["city"])  # Hyderabad
```

---

## 9. Writing JSON

### `json.dump()`
Converts a Python object (dictionary/list) into JSON format and **writes it directly to a file**.

```python
import json

user_data = {
    "name": "Bob",
    "age": 30,
    "skills": ["Java", "API Testing"]
}

with open("output_user.json", "w") as file:
    json.dump(user_data, file)
```

**Resulting `output_user.json`:**
```json
{"name": "Bob", "age": 30, "skills": ["Java", "API Testing"]}
```

### Making It More Readable: `indent`
By default, `json.dump()` writes everything on one line. Use the `indent` parameter to make it human-readable:

```python
with open("output_user.json", "w") as file:
    json.dump(user_data, file, indent=4)
```

**Resulting file:**
```json
{
    "name": "Bob",
    "age": 30,
    "skills": [
        "Java",
        "API Testing"
    ]
}
```

> Just like `load`/`loads`, there's also `json.dumps()` which converts a Python object into a JSON **string** (instead of writing it to a file) — useful when sending JSON data in an API request.

---

## 10. CSV Basics

**CSV** (Comma-Separated Values) is a simple text format for storing tabular data — rows and columns separated by commas. It's commonly used for test data sets, exported reports, and data-driven testing.

### Example CSV File (`users.csv`)

```
name,age,city
Alice,25,Hyderabad
Bob,30,Mumbai
Carol,28,Delhi
```

- The **first row** is usually the **header** (column names).
- Each subsequent row is a **record** (one row of data).

Python's built-in `csv` module handles reading and writing CSV files properly — including edge cases like commas inside quoted text.

```python
import csv
```

---

## 11. Reading CSV

### `csv.reader()`
Reads a CSV file and returns an iterable where each row is a **list of strings**.

```python
import csv

with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ['name', 'age', 'city']
# ['Alice', '25', 'Hyderabad']
# ['Bob', '30', 'Mumbai']
# ['Carol', '28', 'Delhi']
```

Notice the **header row** is included as a normal row — you often need to handle/skip it separately (see below).

---

## 12. Accessing CSV Data

### Skipping the Header Row

```python
import csv

with open("users.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # grabs the first row (header) and moves iterator forward
    print("Header:", header)  # ['name', 'age', 'city']

    for row in reader:
        print(row)  # remaining rows only, no header
```

### Accessing Specific Columns by Index

```python
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        name = row[0]
        age = row[1]
        city = row[2]
        print(f"{name} is {age} years old and lives in {city}")
```

### Using `csv.DictReader` (Bonus — Cleaner Access)
Instead of accessing columns by index (`row[0]`, `row[1]`), `DictReader` lets you access columns **by name**, which is more readable:

```python
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"], row["city"])
```

---

## 13. Writing CSV

### `csv.writer()`
Creates a writer object that can write rows of data into a CSV file.

### `writer.writerow()`
Writes a **single row** (as a list) to the CSV file.

```python
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])       # header row
    writer.writerow(["David", 22, "Chennai"])
    writer.writerow(["Emma", 27, "Pune"])
```

**Resulting `output.csv`:**
```
name,age,city
David,22,Chennai
Emma,27,Pune
```

> **Important:** Always use `newline=""` when opening a file for CSV writing on Windows — otherwise, you may get unwanted blank lines between rows due to how line endings are handled.

### Writing Multiple Rows at Once: `writerows()`

```python
import csv

data = [
    ["David", 22, "Chennai"],
    ["Emma", 27, "Pune"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])  # header
    writer.writerows(data)                    # all data rows at once
```

---

## 14. Story 3 QA Framework Usage

In a QA automation framework, file handling, JSON, and CSV are combined to support **data-driven testing** — running the same test logic against multiple sets of input data.

### Typical Structure

```
qa_framework/
│
├── test_data/
│   ├── users.json
│   └── login_credentials.csv
│
├── pages/
│   └── login_page.py
│
├── utils/
│   ├── json_reader.py
│   └── csv_reader.py
│
├── tests/
│   └── test_login_data_driven.py
│
└── reports/
    └── test_log.txt
```

### Example: `utils/json_reader.py`

```python
import json

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
```

### Example: `utils/csv_reader.py`

```python
import csv

def read_csv(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
```

### Example: `tests/test_login_data_driven.py`

```python
from pages.login_page import LoginPage
from utils.csv_reader import read_csv

def test_login_with_multiple_users():
    credentials = read_csv("test_data/login_credentials.csv")

    for cred in credentials:
        login_page = LoginPage()
        login_page.login(cred["username"], cred["password"])
        # assert expected result, e.g.:
        # assert login_page.is_logged_in() == (cred["expected_result"] == "success")
```

### Example: Logging Test Results to a File

```python
def log_result(test_name, result):
    with open("reports/test_log.txt", "a") as log_file:
        log_file.write(f"{test_name}: {result}\n")
```

### Why This Matters for QA
- **JSON** is ideal for structured config and API response/request test data (nested objects, lists).
- **CSV** is ideal for simple, table-like test data — especially when multiple people (including non-programmers) need to add test cases via Excel/Sheets.
- **Text file logging (append mode)** keeps a running record of test execution without overwriting previous runs.
- Separating data (`test_data/`) from logic (`tests/`, `pages/`) makes the framework **data-driven** — you can add new test cases just by adding new rows/objects, without touching the test code.

---

## Summary Table

| Topic | Key Function(s) | Purpose |
|---|---|---|
| File Modes | `r`, `w`, `a` | Control read/write/append behavior |
| Reading Files | `read()`, `readlines()`, `strip()` | Get file content as string/list, clean whitespace |
| Writing Files | `write()` | Write string content to a file |
| JSON Reading | `json.load()` | Convert JSON file → Python dict/list |
| JSON Writing | `json.dump()` | Convert Python dict/list → JSON file |
| CSV Reading | `csv.reader()`, `csv.DictReader` | Convert CSV file → rows (list or dict) |
| CSV Writing | `csv.writer()`, `writerow()`, `writerows()` | Write rows of data into a CSV file |
| QA Usage | Data-driven testing | Separate test data (JSON/CSV) from test logic for scalable automation |

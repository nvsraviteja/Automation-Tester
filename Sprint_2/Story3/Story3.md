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

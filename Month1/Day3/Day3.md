# Day 3 - Revision and Reading Error Messages

Day 3 is a revision of all the topics covered in the previous two days, practised through hands-on tasks.

## Tasks to Perform on Day 3

- Task 1: Data Type Detective
- Task 2: Type Conversion
- Task 3: Break the Program
- Task 4: Personal Profile Generator

---

## What are Error Messages?

Error messages occur when the code is not written correctly. Python displays them to tell you what went wrong and where.

## Types of Error Messages

- NameError
- ValueError
- SyntaxError
- IndentationError

---

### NameError

Occurs when Python cannot find a variable or function because it has not been defined or has been mistyped.

**Example:**
```python
name = "Hello"
print(nam)
```

In the above example, `nam` is not a defined variable. The correct variable name is `name`, so Python throws a `NameError`.

---

### ValueError

Occurs when the data type is correct but the value provided is not compatible with it.

**Example:**
```python
name = int("hey")
```

Python expects a number for `int()`, but the value provided is a string. Since `"hey"` cannot be converted to an integer, Python throws a `ValueError`.

---

### SyntaxError

Occurs when the code is not written in a way Python can read or understand.

**Example:**
```python
print("hello"
```

The closing parenthesis `)` is missing. Because the code is incomplete, Python throws a `SyntaxError`.

---

### IndentationError

Occurs when spaces or tabs are not used correctly. Python uses indentation to define code blocks, so incorrect indentation breaks the structure.

**Incorrect:**
```python
if 5 > 3:
print("Hello")
```

**Correct:**
```python
if 5 > 3:
    print("Hello")
```

Python reads the indented line as belonging to the `if` block:
```
if 5 > 3:
    ↓
    print("Hello")
```

---

## What is a Code Block in Python?

A code block is a group of statements that belong together and are executed as a unit.

In Python, code blocks are defined using indentation (spaces or tabs), not curly braces `{}` like in some other programming languages.

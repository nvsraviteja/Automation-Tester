# Day 17 - Exception Handling

## What is an Exception?

An exception is an error that occurs while the program is running. When Python encounters one, it stops execution and displays an error message.

---

## Runtime Error vs Syntax Error

| | Syntax Error | Runtime Error (Exception) |
|-|--------------|---------------------------|
| When it occurs | Before the program runs | While the program is running |
| Cause | Code Python cannot read | Code Python can read but cannot execute |
| Example | Missing `:` or `)` | Dividing by zero, accessing a missing key |

---

## Common Exceptions

### IndexError

Occurs when you try to access an index that does not exist in a list or string.

```python
tests = ["Smoke", "Regression"]
print(tests[5])  # IndexError: list index out of range
```

---

### KeyError

Occurs when you try to access a key that does not exist in a dictionary.

```python
user = {"name": "Ravi"}
print(user["age"])  # KeyError: 'age'
```

---

### TypeError

Occurs when an operation is performed on an incompatible data type.

```python
print("Age: " + 25)  # TypeError: can only concatenate str (not "int") to str
```

---

### ValueError

Occurs when the data type is correct but the value is not compatible.

```python
age = int("hello")  # ValueError: invalid literal for int() with base 10: 'hello'
```

---

## try / except

Instead of letting the program crash, `try / except` lets you handle the error gracefully.

**Without exception handling — program crashes:**

```python
user = {"name": "Ravi"}
print(user["age"])  # KeyError — program stops here
```

**With exception handling — program continues:**

```python
try:
    print(user["age"])
except:
    print("Key not found")
```

**How it works:**

1. Python runs the code inside `try`
2. If an error occurs, it jumps to `except`
3. The code in `except` runs instead of crashing
4. The program continues after the block

---

## Specific Exception Handling

Instead of catching all errors with a general `except`, you can handle each exception type separately.

```python
try:
    age = int(input("Enter age: "))
    print(user["age"])
except ValueError:
    print("Please enter a valid number")
except KeyError:
    print("Key not found in dictionary")
```

This is better practice because:

- It gives the user a clear and relevant error message
- It prevents hiding unexpected errors by catching everything at once
- In QA, specific exception handling makes test failure messages more meaningful

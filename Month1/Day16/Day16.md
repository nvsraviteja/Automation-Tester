# Day 16 - Functions

## 1. What is a Function?

A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, you define it once and call it whenever needed.

**The problem without functions:**

```python
print("Running login test")
print("Checking status")
print("Validating response")
```

If you need to run this for 20 tests, you end up copying the same lines over and over. That is messy and hard to maintain. Functions solve this.

---

## 2. Function Syntax

```python
def greet():
    print("Hello")
```

**Parts of a function:**

| Part | Purpose |
|------|---------|
| `def` | Keyword that tells Python you are defining a function |
| `greet` | The function name |
| `()` | Parentheses — holds parameters if any |
| `:` | Marks the end of the function definition |
| Indentation | Everything indented below belongs to the function |

---

## 3. Calling a Function

Defining a function does not execute it. The code inside runs only when you call the function.

```python
def greet():
    print("Hello")
```

Nothing happens yet. To run it:

```python
greet()  # Output: Hello
```

> **Common beginner mistake:** Writing the function but forgetting to call it and wondering why nothing runs.

---

## 4. Parameters

Parameters allow a function to accept input so it can work with different values each time it is called.

```python
def greet(name):
    print(name)

greet("Ravi")  # Output: Ravi
```

---

## 5. Arguments vs Parameters

This is a small but important distinction that often comes up in interviews.

```python
def greet(name):   # name is the parameter
    print(name)

greet("Ravi")      # "Ravi" is the argument
```

| Term | Definition |
|------|-----------|
| Parameter | The variable defined in the function signature |
| Argument | The actual value passed when calling the function |

---

## 6. Return

`return` sends a value back from the function so it can be stored or used elsewhere. This is different from `print()` which only displays the value.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

| | `print()` | `return` |
|-|-----------|----------|
| What it does | Displays the value on screen | Sends the value back to the caller |
| Can be stored | No | Yes |

---

## 7. QA Use Cases

Functions make test code reusable and easier to maintain.

**Without a function — repeated in every test:**

```python
if response["status"] == 200:
    print("Pass")
```

Copying this across 30 tests means 30 places to update if anything changes.

**With a function — defined once, used everywhere:**

```python
def validate_status(response):
    if response["status"] == 200:
        print("Pass")

validate_status(response)
```

This is the foundation of how automation frameworks are built. Write the logic once, call it anywhere.

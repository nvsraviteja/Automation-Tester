# Day 2 - Variables, User Inputs, Type Conversion & String Formatting

## What is a Variable?

A variable is a named container that stores data which can be used later in the program.

**Example:**
```python
name = "QA Automation"
```
Here `name` is the variable and `"QA Automation"` is the data it stores.

## Why Do We Use Variables?

Variables make code simpler and easier to maintain. When a value needs to be updated, you don't have to find and change it in multiple places. You update it once, and the change is automatically reflected everywhere it is used.

## Data Types Stored in Variables

- Integer
- Float
- Boolean
- String

## Important: Python Considers the Latest Value

If you assign a value to the same variable more than once, Python will use the most recent value and ignore the previous one.

**Example:**
```python
age = 25
age = 30
```
Here Python will consider `age` as `30`, not `25`.

## Variable Naming Rules

- Cannot start with a number
- Cannot contain a hyphen ( - )

## User Input

User input allows a program to receive data from the user while it is running.

`input()` is used to take input from the user. The default data type of `input()` is always a string.

You can verify this with the following code:

```python
a = input("Enter your age: ")
print(a)
print(type(a))
```

To change the data type of the input, we use Type Conversion.

---

## Type Conversion

### What is Type Conversion?

Type Conversion means changing a value from one data type to another.

Examples:
- String to Integer
- Integer to Float
- Float to String

### Why Do We Need Type Conversion?

When you take input from a user, Python treats it as a string by default. If you want to perform calculations with that value, you must first convert it to an integer or float.

### Type Conversion Functions

| Function | Converts to |
|----------|-------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |

**Example:**
```python
a = int(input("Enter your age: "))
print(type(a))
```

> Note: `int()` removes the decimal part of a number. It does not round it.

---

## String Formatting

### What is String Formatting?

String formatting is the process of inserting variables or expressions into a string so they are displayed as part of the output.

### Methods of String Formatting

**1. Using commas**
```python
print("My name is", name, "and I am", age, "years old.")
```

**2. Using f-strings**
```python
print(f"My name is {name} and I am {age} years old.")
```

The most commonly used method in Python is f-strings, where variables are placed inside curly braces `{}` and are automatically replaced with their values when the string is displayed.

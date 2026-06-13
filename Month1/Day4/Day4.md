# Day 4 - Operators & Real Calculations

## What are Operators?

An operator is a symbol that tells Python to perform a specific action.

Without operators, Python would only be used for storing data. Operators allow Python to:

- Calculate
- Compare
- Validate
- Make decisions

Every automation framework, API test, and AI evaluation script uses operators.

## Types of Operators

1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators


---

## Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Name | Example |
|----------|------|---------|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division | `9 / 2 = 4.5` |
| `%` | Modulus | `9 % 8 = 1` |

The above operators are straightforward except for the Modulus operator.

### Modulus Operator

The modulus operator returns the remainder after division.

**Example:**
```python
9 % 8 = 1
```

### Why Do We Use Modulus?

Many systems need to check whether a number divides evenly. The modulus operator makes this possible.

- If the result is `0`, the number divides evenly.
- If the result is not `0`, there is a remainder and the division is not even.

**Example:**
```python
10 % 2 = 0   # divides evenly
10 % 3 = 1   # does not divide evenly
```
## Comparison Operators

Comparison operators are used to compare two values, variables, or expressions.

> **Note:** An expression is a combination of values, variables, operators, and functions that Python evaluates to produce a single result.

### What Does a Comparison Operator Do?

It compares two values and returns either `True` or `False`.

### Types of Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Comparison operators do not change or modify any value or data. They simply evaluate the statement and return a result accordingly.


## Assignment Operators

An assignment operator takes the value on the right and assigns it to the variable on the left.

**Example:**
```python
a = 10
```

Here `a` is the variable on the left, and `10` is the value being stored into it.

> **Note:** The `=` sign is an assignment operator, not a comparison operator. Comparison uses `==`.

---

## Types of Assignment Operators

1. Simple Assignment Operator (`=`)
2. Compound Assignment Operators

---

## Compound Assignment Operators

Compound assignment operators combine an arithmetic operation with a variable to make the code shorter.

---

### Addition Assignment (`+=`)

Used when a value needs to increase over time.

```python
score = 10
score += 3

# Equivalent to:
score = score + 3
```

---

### Subtraction Assignment (`-=`)

Used when a value needs to decrease over time.

```python
health = 100
health -= 20

# Equivalent to:
health = health - 20
```

---

### Multiplication Assignment (`*=`)

Used when a value needs to be multiplied.

```python
score = 10
score *= 2

# Equivalent to:
score = score * 2
```

---

### Division Assignment (`/=`)

Used when a value needs to be divided.

```python
money = 100
money /= 2

# Equivalent to:
money = money / 2
```
## Logical Operators

Logical operators are used to combine conditional statements.

There are three logical operators:

- `and`
- `or`
- `not`

---

### AND

Used when two conditions both need to be satisfied for the overall condition to be `True`.

**Example:**
```python
age >= 18 and ticket_available == 1
```

Python checks two conditions here:
- The user's age is greater than or equal to 18
- A ticket is available

**Truth Table:**

| Condition 1 | Condition 2 | Result  |
|-------------|-------------|---------|
| `True`      | `True`      | `True`  |
| `True`      | `False`     | `False` |
| `False`     | `True`      | `False` |
| `False`     | `False`     | `False` |

---

### OR

Used when only one of the two conditions needs to be satisfied for the overall condition to be `True`.

**Truth Table:**

| Condition 1 | Condition 2 | Result  |
|-------------|-------------|---------|
| `True`      | `True`      | `True`  |
| `True`      | `False`     | `True`  |
| `False`     | `True`      | `True`  |
| `False`     | `False`     | `False` |

---

### NOT

The `not` operator reverses the result of a condition. If the condition is `True`, it returns `False`, and vice versa.

**Example:**
```python
if not condition:
    print(result)
```

**Truth Table:**

| Condition | Result  |
|-----------|---------|
| `True`    | `False` |
| `False`   | `True`  |

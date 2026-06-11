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

# Day 10 - Strings

## What is a String?

A string is a sequence of characters enclosed in quotes.

**Examples:**
```python
name = "Ravi"
username = "Raviteja123"
error = "404 not found"
```

Characters in a string can be:
- Letters
- Numbers
- Spaces
- Symbols

---

## String vs Int

```python
age = 25      # integer
age = "25"    # string
```

Both store the value `25` but they are different data types. Any value enclosed in quotes is treated as a string, regardless of whether it contains numbers, letters, spaces, or special characters.

---

## Indexing

Python sees a string as characters stored in positions. Indexing means accessing a character from a string using its position number.

**Example:**

```
Name:   R  A  V  I
Index:  0  1  2  3
```

```python
name = "RAVI"
print(name[1])  # Output: A
```

> **Note:** Indexing starts at `0`, not `1`.

### Types of Indexing

**1. Positive Indexing** — starts from the left, values go from `0` to `n`.

**2. Negative Indexing** — starts from the right, values go from `-1` to `-n`.

```
Name:   R   A   V   I
Index: -4  -3  -2  -1
```

### Invalid Indexing

If an index is out of range, Python throws an `IndexError`.

```python
name = "ravi"
print(name[4])  # IndexError: string index out of range
```

The valid index range for `"ravi"` is `0` to `3`. Index `4` does not exist.

---

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

## Length — len()

`len()` returns the total number of characters in a string.

```python
name = "raviteja"
print(len(name))  # Output: 8
```

> **Note:** `len()` counts from `1`, not `0`. So a string with 8 characters has a length of `8` but its last index is `7`.

---

## String Slicing

Slicing is used to extract a portion of a string.

**Syntax:**
```python
string[start:end]
```

**Example:**
```python
name = "QA Automation"
print(name[0:7])  # Output: QA Auto
```

The same rules from `range()` apply — `start` is included, `end` is excluded.

### Omitting Start or End

```python
name = "QA tester"

print(name[:2])   # No start — Python defaults to 0. Output: QA
print(name[3:])   # No end — Python defaults to last index. Output: tester
print(name[:])    # Both omitted — prints the whole string. Output: QA tester
```

### Shortcut Rules

| Slice | Meaning |
|-------|---------|
| `[:n]` | Start from beginning, end at `n-1` |
| `[n:]` | Start at `n`, go to the end |
| `[:]` | Entire string |

### Slice Step

Just like `range()`, slicing has an optional third parameter for step.

```python
string[start:end:step]
```

```python
name = "QAtester"
print(name[0:8:2])  # Output: Qtse
```

Starts at `0`, stops before `8`, jumps by `2`.

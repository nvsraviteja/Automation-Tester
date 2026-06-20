# Day 14 - Tuples and Sets
---
## Tuples

A tuple is a collection of values stored in a fixed order. Once created, the values cannot be changed.

**Syntax:**
```python
games = ("FIFA", "PUBG", "Minecraft")
```

Tuples support indexing and slicing just like lists.

```python
games[0]     # FIFA
games[-1]    # Minecraft
games[0:2]   # ("FIFA", "PUBG")
```

---

## Tuple vs List

| | List | Tuple |
|--|------|-------|
| Syntax | `[]` | `()` |
| Mutable | Yes | No |
| Can modify values | Yes | No |

**List — values can be changed:**
```python
games = ["FIFA", "PUBG", "Minecraft"]
games[0] = "Valorant"  # allowed
```

**Tuple — values cannot be changed:**
```python
games = ("FIFA", "PUBG", "Minecraft")
games[0] = "Valorant"  # TypeError
```

> **Immutable** means once a tuple is created, its values are fixed and cannot be modified.

### Why Use Tuples?

Tuples are used when the data should not change, for example:

- Browser names
- Environment names
- Status codes
- Constants

In QA, tuples prevent accidental modification of fixed test data.

---

## Sets

A set is a collection that stores only unique values. If duplicate values are added, they are removed automatically. Sets are also unordered, meaning items have no fixed position.

**Syntax:**
```python
nums = {1, 2, 2, 3}
print(nums)  # Output: {1, 2, 3}
```

### Property 1 — No Duplicates

Duplicate values are removed automatically.

```python
bugs = {"Bug1", "Bug1", "Bug2"}
print(bugs)  # Output: {"Bug1", "Bug2"}
```

### Property 2 — No Indexing

Because sets are unordered, indexing and slicing do not work.

```python
bugs[0]   # TypeError — sets do not support indexing
bugs[1:]  # TypeError — sets do not support slicing
```

---

## Duplicate Detection Using Sets

Sets are commonly used to check whether a list contains duplicate values.

**Formula:**
```python
len(list) != len(set(list))
```

- If the lengths are different → duplicates exist
- If the lengths are equal → no duplicates

**Example:**
```python
bugs = ["Bug1", "Bug2", "Bug1"]

print(len(bugs))         # 3
print(len(set(bugs)))    # 2

if len(bugs) != len(set(bugs)):
    print("Duplicates exist")
```

The original list has 3 items but the set has only 2 because `"Bug1"` appears twice. Since `3 != 2`, duplicates are confirmed.

# Day 13 - List Slicing

## What is List Slicing?

List slicing is used to extract a portion of a list instead of accessing one item at a time.

Just like string slicing, list slicing uses the same syntax and follows the same rules.

**Syntax:**
```python
list[start:end]
```

**Example:**

```python
tests = ["Ad-hoc", "Regression", "Performance", "Compatibility", "Smoke"]

print(tests[1:4])
# Output: ["Regression", "Performance", "Compatibility"]
```

> `start` is included. `end` is excluded.

---

## Slice Shortcuts

You can omit `start` or `end` and Python will use a default value.

```python
tests = ["Ad-hoc", "Regression", "Performance", "Compatibility", "Smoke"]

print(tests[:3])   # No start — defaults to 0
# Output: ["Ad-hoc", "Regression", "Performance"]

print(tests[2:])   # No end — defaults to last item
# Output: ["Performance", "Compatibility", "Smoke"]

print(tests[:])    # Both omitted — returns the whole list
# Output: ["Ad-hoc", "Regression", "Performance", "Compatibility", "Smoke"]
```

### Shortcut Rules

| Slice | Meaning |
|-------|---------|
| `[:n]` | Start from beginning, end at `n-1` |
| `[n:]` | Start at `n`, go to the end |
| `[:]` | Entire list |

---

## Step Slicing

Step slicing adds a third parameter to control how many items to skip after each selection.

**Syntax:**
```python
list[start:end:step]
```

**Example:**

```python
tests = ["Ad-hoc", "Regression", "Performance", "Compatibility", "Smoke", "Sanity"]

print(tests[0:6:2])
# Output: ["Ad-hoc", "Performance", "Smoke"]
```

Starts at index `0`, stops before index `6`, picks every 2nd item.

---

## Reverse Slicing

Using a negative step reverses the order of the list.

**Example:**

```python
tests = ["Ad-hoc", "Regression", "Performance", "Compatibility", "Smoke"]

print(tests[::-1])
# Output: ["Smoke", "Compatibility", "Performance", "Regression", "Ad-hoc"]
```

You can also reverse a specific portion:

```python
print(tests[4:1:-1])
# Output: ["Smoke", "Compatibility", "Performance"]
```

Starts at index `4`, stops before index `1`, moves backwards by `1`.

---

## Summary

| Type | Syntax | What it does |
|------|--------|--------------|
| Basic slicing | `list[start:end]` | Extracts a portion of the list |
| Shortcut — from start | `list[:end]` | Starts at index `0` |
| Shortcut — to end | `list[start:]` | Goes to the last item |
| Full copy | `list[:]` | Returns entire list |
| Step slicing | `list[start:end:step]` | Picks every nth item |
| Reverse slicing | `list[::-1]` | Returns list in reverse order |

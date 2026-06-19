# Day 12 - List

## What is a List?

A list is a collection of items enclosed in square brackets and separated by commas.

```python
tests = ["Ad-hoc", "Regression", "Performance"]
```

---

## List Indexing

Indexing in a list works the same as in strings, but here it is used to locate an item within the list.

```
tests:  ["Ad-hoc", "Regression", "Performance"]
index:      0           1              2
```

Indexing starts at `0` and goes up to `n-1`.

### Negative Indexing

Negative indexing starts from the right and moves left.

```
tests:  ["Ad-hoc", "Regression", "Performance"]
index:     -3          -2             -1
```

---

## Length — len()

Returns the total number of items in the list.

```python
tests = ["Ad-hoc", "Regression", "Performance"]
print(len(tests))  # Output: 3
```

---

## Mutability

A list is mutable, meaning its values can be changed after it is created.

```python
tests = ["Ad-hoc", "Regression", "Performance"]
tests[1] = "Compatibility"

# Result:
# ["Ad-hoc", "Compatibility", "Performance"]
```

---

## List Methods

### append()

Adds a new item to the end of the list.

```python
tests = ["Ad-hoc", "Regression", "Performance"]
tests.append("Compatibility")

# Result:
# ["Ad-hoc", "Regression", "Performance", "Compatibility"]
```

### remove()

Removes an item from the list by its value, not by its position.

```python
tests = ["Ad-hoc", "Regression", "Performance", "Compatibility"]
tests.remove("Compatibility")

# Result:
# ["Ad-hoc", "Regression", "Performance"]
```

---

## Loop Through a List

Looping through a list works the same way as looping through a string. Instead of iterating over each character, it iterates over each item in the list.

```python
tests = ["Ad-hoc", "Regression", "Performance", "Compatibility"]

for test in tests:
    print(test)
```

**Breakdown of the loop:**

```python
for temporary_variable in list_variable:
    print(temporary_variable)
```

- `temporary_variable` — can be named anything; it holds the current item on each iteration
- `list_variable` — must match the exact name of the list you defined

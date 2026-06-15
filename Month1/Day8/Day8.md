# Day 8 - Loops

Loops are control flow structures used to repeatedly execute a block of code.

**Examples of when loops are used:**
- Counting from 1 to 100
- Running the same test multiple times

---

## What Problem Do Loops Solve?

Suppose you want to print `"Hello"` 5 times:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

This works — but imagine printing it 1000 times. That is not practical.

With a loop:

```python
for i in range(5):
    print("Hello")
```

Loops solve the following problems:

- Repetition and automation
- Working through collections
- Handling an unknown number of repetitions

---

## Types of Loops

---

### While Loop

A `while` loop repeats a block of code as long as a condition is `True`. Once the condition becomes `False`, the loop stops.

**Syntax:**

```python
while condition:
    code
```

**Example:**

```python
count = 1
while count <= 3:
    print("Hello")
```

### Three Mandatory Parts of a While Loop

| Part | Purpose |
|------|---------|
| Initialization | Sets the starting state before the loop begins |
| Condition | Keeps the loop running while `True` |
| Update | Changes the state so the loop eventually stops |

**What happens if one part is missing:**

- No initialization → error
- Wrong condition → incorrect behavior
- No update → infinite loop


## Break

`break` is the first loop control statement.

Normally a loop stops when its condition becomes `False`. But sometimes you need to stop the loop immediately, even if the condition is still `True`. That is what `break` does.

**Example:**

```python
count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1
```

`break` does not wait for the loop condition to become `False`. It exits the loop immediately, regardless of whether the condition is still `True`.

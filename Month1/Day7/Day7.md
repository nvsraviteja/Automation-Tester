## Elif Statement

With `if-else` we can only handle two possible outcomes. If there are more possible outcomes — such as 5 or 6 — then `if-else` alone is not enough.

This is where `elif` comes in.

---

### What is Elif?

`elif` stands for "else if". If the first condition fails, Python checks the second. If that fails, it checks the third, and so on.

### Structure

```python
if condition1:
    action
elif condition2:
    action
elif condition3:
    action
else:
    action
```

---

### Example

Consider the pass percentage of a test cycle:

- 90 and above → Excellent
- 80 and above → Good
- 70 and above → Average
- Below 70 → Poor

There are 4 possible outcomes. Using `elif`, Python can handle all of them:

```python
if percentage >= 90:
    print("Excellent")
elif percentage >= 80:
    print("Good")
elif percentage >= 70:
    print("Average")
else:
    print("Poor")
```

---

> **Golden Rule:** Python executes only the first `True` branch. Not all true branches — only the first one.

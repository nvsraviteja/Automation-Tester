# Day 6 - Else Statement

Yesterday we learned about the `if` statement. But what happens when the condition fails? Python simply ends the block and moves on without giving any information about why it was skipped.

As a QA engineer, we expect Python to give feedback on the code it executed — even when a condition fails, it should state that the condition was not met. This is not possible with `if` alone.

That is where the `else` statement comes in.

---

## What is Else?

`else` tells Python that if the `if` condition is `False`, then execute a different block of code.

**With only `if`:**

- Condition `True` → execute the block
- Condition `False` → skip the block, nothing happens

**With `if-else`:**

- Condition `True` → execute the `if` block
- Condition `False` → execute the `else` block

---

## Structure

```python
if condition:
    true_action
else:
    false_action
```

- **Block 1** (`if`) — runs when the condition is `True`
- **Block 2** (`else`) — runs when the condition is `False`

> **Note:** With `if-else`, only one block is executed, never both.

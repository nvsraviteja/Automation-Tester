# Day 9 - Continue & For Loop

Yesterday we learned about the `break` statement. Today we will look at `continue`.

---

## Continue

When a condition is met, `continue` stops the current iteration, skips any remaining lines in that iteration, and moves on to the next one.

In simple terms: skip this round and continue with the next round.

**Example:**

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```

---

## Continue vs Break

| Statement | Behaviour |
|-----------|-----------|
| `continue` | Skips the current iteration and keeps the loop going |
| `break` | Exits the loop completely |

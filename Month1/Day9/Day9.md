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

## For Loop

A `for` loop is used to repeat a block of code for each item in a sequence.

In simple terms: run this code again and again for every item until the end of the sequence.

### Syntax

```python
for variable in sequence:
    # code block
```

### Example

```python
for i in range(1, 5):
    print(i)
```

### Quick Interview Answer

A `for` loop is used to iterate over a sequence such as a list, string, or range and execute a block of code repeatedly for each item. It is mainly used to automate repetitive tasks and process collections of data efficiently.

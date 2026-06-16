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

---

## Why Does For Loop Exist?

The `for` loop makes code cleaner and more readable. It removes the need to manually write initialization, condition, and update parts — Python handles all of that automatically. You only need to specify how many iterations are required.

---

## range()

`range()` is used to define where the loop starts, where it ends, and by how much it increments or decrements after each iteration.

```python
range(start, stop, step)
```

| Parameter | Description |
|-----------|-------------|
| `start` | The starting point of the iteration |
| `stop` | The ending point (not included) |
| `step` | The amount to increment or decrement each iteration |

### Three Ways to Use range()

- `range(stop)` — starts at `0` by default and increments by `1` each iteration
- `range(start, stop)` — starts at the given value and increments by `1` by default
- `range(start, stop, step)` — all three parts are specified, no default values applied

### Rules for range()

- `start` is **included**
  ```python
  range(1, 5)  # starts from 1
  ```

- `stop` is **excluded**
  ```python
  range(1, 5)  # ends at 4, never reaches 5
  ```

- `step` controls the jump size
  ```python
  range(1, 10, 2)  # increments by 2 each time, ends before 10
  ```

- `step` can be negative (counts down)
  ```python
  range(10, 0, -1)  # counts from 10 down to 1
  ```

- Empty ranges are possible
  ```python
  range(5, 5)  # start and stop are the same, no iterations run
  ```

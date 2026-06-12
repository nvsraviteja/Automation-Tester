# Day 5 - If Statements

Over the last few days we covered what Python can do:

- Store data
- Take inputs
- Perform calculations
- Compare values

But after getting a result, what happens next is decided by conditional statements.

**Example from a QA perspective:**

If the pass percentage of a build is 80%:

```python
pass_percentage = 80
pass_percentage >= 80
```

Will Python just print `True` and stop? No. This is where conditional statements come in. Python will decide what to do based on the requirement and execute accordingly.

## Types of Conditional Statements

- `if`
- `if-else`
- `elif`
- Nested `if`

---

## If Statement

The `if` statement tells Python to execute a block of code only when the condition is `True`. If the condition is `False`, Python skips that block and moves to the next line.

### Structure

```python
if condition:
    action
```

This has two parts:

1. **Condition** - A question that returns either `True` or `False`.
2. **Action** - What Python should do if the condition is `True`.

### How It Works Step by Step

1. Evaluate the condition.
2. Check if the result is `True` or `False`.
3. If `True`, execute the block of code.
4. If `False`, skip the block of code.

> **Note:** The colon `:` at the end of the condition is mandatory. Without it, Python does not know where the condition ends and where the action begins.

---

## Indentation

The lines of code that belong to the `if` block are called the conditional block. Python identifies them by their indentation — the space before each line inside the block.

If the indentation is missing, Python will not treat those lines as part of the `if` block.

**Example:**

```python
if condition:
    action
```

The space before `action` is the indentation. The action can span any number of lines, but every line must be consistently indented so Python knows they all belong to the same block.

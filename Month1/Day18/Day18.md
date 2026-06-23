# Day 18 - Files / CSV

## What is a File?

A file is data stored permanently outside Python’s memory. Unlike variables, files remain saved even after the program stops running.

## Variable vs File

| | Variable | File |
|-|----------|------|
| Storage | RAM (temporary memory) | Disk (permanent storage) |
| Lifetime | Exists only while program runs | Exists until deleted |
| Example | `name = "Ravi"` | `report.txt` |

## Why QA Uses Files
- Test data
- Execution logs
- Test reports
- Failed test case IDs
- API payload samples

## Common File Types
- `.txt`
- `.csv`
- `.log`

## What is CSV?
CSV stands for **Comma Separated Values**.

## Opening a File

```python
open("file.txt")
```

Safer syntax:

```python
with open("file.txt") as f:
```

## with open()
`with` ensures the file gets automatically closed after use.

## as f Meaning
`f` is a variable storing the opened file object.

## Reading a File
Use `.read()` to read entire file.
`.read()` returns a **string**.

## Writing to a File
Use `.write()`.

Write mode: `"w"`

This overwrites old content.

## Append Mode
Use `"a"`.

This keeps old content and adds new content.

## Difference Between File Modes

| Mode | Purpose |
|------|---------|
| `"r"` | Read file |
| `"w"` | Write / Overwrite |
| `"a"` | Append to existing file |

## Mini Practical Project — QA Log Generator

Input:

```python
results = ["Pass", "Fail", "Pass", "Blocked", "Fail"]
```

### Step 1 — Analyze Results
Count Pass, Fail, Blocked

### Step 2 — Generate Summary

Pass: 2  
Fail: 2  
Blocked: 1  

### Step 3 — Save Report
Write summary into `report.txt` using `"w"`.

### Step 4 — Append Execution Logs
Append into `execution.log`:

TC1 Pass  
TC2 Fail  
TC3 Pass  
TC4 Blocked  
TC5 Fail

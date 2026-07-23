# SQL Cheat Sheet — Sprint 6, Story 2
### Topic: Create Database/Table, Insert, Select, Where, Operators, Sorting, Filtering

---

## 1. Create Database

```sql
CREATE DATABASE CompanyDB;

-- Switch to the database
USE CompanyDB;
```

**Key points**
- `CREATE DATABASE` sets up a new empty database container.
- `USE` selects which database subsequent queries run against (MySQL syntax; other RDBMS may differ slightly, e.g., PostgreSQL uses `\c dbname`).

---

## 2. Create Table

```sql
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50) NOT NULL,
    Department VARCHAR(30),
    Salary DECIMAL(10,2),
    JoiningDate DATE,
    Age INT
);
```

**Key points**
- Define column name, data type, and optional constraints together.
- `PRIMARY KEY` uniquely identifies rows; `NOT NULL` prevents empty values.

---

## 3. Insert

```sql
-- Insert a single row (all columns, in order)
INSERT INTO Employee VALUES (101, 'John', 'IT', 55000.00, '2022-01-15', 28);

-- Insert with specific columns (recommended - order-independent, allows skipping optional columns)
INSERT INTO Employee (EmpID, EmpName, Department, Salary)
VALUES (102, 'Priya', 'HR', 60000.00);

-- Insert multiple rows at once
INSERT INTO Employee (EmpID, EmpName, Department, Salary)
VALUES
    (103, 'Raj', 'Finance', 50000.00),
    (104, 'Anita', 'IT', 62000.00);
```

**Key point:** Always specify column names explicitly — protects your insert from breaking if the table structure changes later.

---

## 4. Select

```sql
-- Select specific columns
SELECT EmpName, Salary FROM Employee;

-- Select all columns
SELECT * FROM Employee;
```

**Key point:** Avoid `SELECT *` in real applications/queries where possible — fetching only needed columns is more efficient.

---

## 5. Where (Filtering Rows)

```sql
SELECT * FROM Employee WHERE Department = 'IT';

SELECT * FROM Employee WHERE Salary > 55000;
```

**Key point:** `WHERE` filters rows **before** grouping/aggregation — it operates on raw table rows.

---

## 6. Comparison Operators

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `Salary = 50000` |
| `!=` or `<>` | Not equal to | `Department <> 'HR'` |
| `>` | Greater than | `Age > 25` |
| `<` | Less than | `Age < 30` |
| `>=` | Greater than or equal | `Salary >= 60000` |
| `<=` | Less than or equal | `Salary <= 60000` |

```sql
SELECT * FROM Employee WHERE Age >= 30;
```

---

## 7. Logical Operators

| Operator | Meaning |
|---|---|
| `AND` | Both conditions must be true |
| `OR` | At least one condition must be true |
| `NOT` | Negates a condition |

```sql
SELECT * FROM Employee WHERE Department = 'IT' AND Salary > 55000;

SELECT * FROM Employee WHERE Department = 'HR' OR Department = 'Finance';

SELECT * FROM Employee WHERE NOT Department = 'IT';
```

---

## 8. Order By (Sorting)

```sql
-- Ascending (default)
SELECT * FROM Employee ORDER BY Salary;
SELECT * FROM Employee ORDER BY Salary ASC;

-- Descending
SELECT * FROM Employee ORDER BY Salary DESC;

-- Sort by multiple columns
SELECT * FROM Employee ORDER BY Department ASC, Salary DESC;
```

---

## 9. Limit (Restrict Number of Rows)

```sql
-- First 5 rows
SELECT * FROM Employee LIMIT 5;

-- Skip first 5, then return next 5 (pagination) - MySQL syntax
SELECT * FROM Employee LIMIT 5 OFFSET 5;
```

**Key point:** `LIMIT` syntax varies by RDBMS — SQL Server uses `TOP`, Oracle uses `FETCH FIRST n ROWS ONLY`.

---

## 10. Distinct (Unique Values)

```sql
-- Remove duplicate values from result
SELECT DISTINCT Department FROM Employee;
```

**Key point:** `DISTINCT` applies to the **combination** of all selected columns, not just one — `SELECT DISTINCT Department, Salary` returns unique (Department, Salary) pairs, not unique Departments alone.

---

## 11. Like (Pattern Matching)

| Wildcard | Meaning |
|---|---|
| `%` | Matches zero or more characters |
| `_` | Matches exactly one character |

```sql
-- Names starting with 'A'
SELECT * FROM Employee WHERE EmpName LIKE 'A%';

-- Names ending with 'a'
SELECT * FROM Employee WHERE EmpName LIKE '%a';

-- Names containing 'an'
SELECT * FROM Employee WHERE EmpName LIKE '%an%';

-- Names with exactly 4 characters
SELECT * FROM Employee WHERE EmpName LIKE '____';
```

---

## 12. In (Match Any Value in a List)

```sql
SELECT * FROM Employee WHERE Department IN ('IT', 'HR', 'Finance');

-- Equivalent using OR (IN is shorter/cleaner)
SELECT * FROM Employee WHERE Department = 'IT' OR Department = 'HR' OR Department = 'Finance';

-- NOT IN
SELECT * FROM Employee WHERE Department NOT IN ('IT');
```

---

## 13. Between (Range Filtering)

```sql
SELECT * FROM Employee WHERE Salary BETWEEN 50000 AND 60000;

-- Date range
SELECT * FROM Employee WHERE JoiningDate BETWEEN '2022-01-01' AND '2022-12-31';

-- NOT BETWEEN
SELECT * FROM Employee WHERE Salary NOT BETWEEN 50000 AND 60000;
```

**Key point:** `BETWEEN` is **inclusive** of both boundary values.

---

## 14. NULL Handling

`NULL` represents a **missing/unknown** value — it's not the same as `0` or an empty string, and cannot be compared using `=` or `!=`.

```sql
-- Find rows with NULL values
SELECT * FROM Employee WHERE Department IS NULL;

-- Find rows with NOT NULL values
SELECT * FROM Employee WHERE Department IS NOT NULL;

-- WRONG - this will never return rows, even if Department IS NULL
-- SELECT * FROM Employee WHERE Department = NULL;
```

**Key points**
- Always use `IS NULL` / `IS NOT NULL` — never `= NULL` or `!= NULL` (these evaluate to unknown, not true/false).
- `NULL` in arithmetic/comparisons generally propagates as `NULL` (e.g., `NULL + 5` = `NULL`).
- Functions like `COALESCE(column, 'default_value')` substitute a default when a value is `NULL`.

---

## Quick Reference Table

| Clause/Operator | Purpose |
|---|---|
| `CREATE DATABASE` | Create a new database |
| `CREATE TABLE` | Define a new table structure |
| `INSERT INTO` | Add new rows |
| `SELECT` | Retrieve columns |
| `WHERE` | Filter rows by condition |
| `=, !=, >, <, >=, <=` | Comparison operators |
| `AND, OR, NOT` | Logical operators |
| `ORDER BY` | Sort results (`ASC`/`DESC`) |
| `LIMIT` | Restrict number of rows returned |
| `DISTINCT` | Remove duplicate rows |
| `LIKE` | Pattern match with `%` and `_` |
| `IN` | Match against a list of values |
| `BETWEEN` | Match within an inclusive range |
| `IS NULL` / `IS NOT NULL` | Check for missing values |

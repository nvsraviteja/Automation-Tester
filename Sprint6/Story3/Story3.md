# SQL Cheat Sheet — Sprint 6, Story 3
### Topic: Aggregate Functions — COUNT(), SUM(), AVG(), MAX(), MIN()

---

## 0. What are Aggregate Functions?

Aggregate functions perform a calculation on a **set of rows** and return a **single summarized value**. They're commonly used with `GROUP BY` to summarize data per category.

### Sample table used in examples: `Employee`

| EmpID | EmpName | Department | Salary |
|---|---|---|---|
| 101 | John | IT | 55000 |
| 102 | Priya | HR | 60000 |
| 103 | Raj | Finance | 50000 |
| 104 | Anita | IT | 62000 |
| 105 | Kabir | IT | NULL |

---

## 1. COUNT()

Returns the **number of rows** that match a condition.

```sql
-- Count all rows in the table (includes NULLs)
SELECT COUNT(*) FROM Employee;

-- Count non-NULL values in a specific column
SELECT COUNT(Salary) FROM Employee;   -- excludes rows where Salary is NULL

-- Count with a condition
SELECT COUNT(*) FROM Employee WHERE Department = 'IT';

-- Count distinct values
SELECT COUNT(DISTINCT Department) FROM Employee;
```

**Key points**
- `COUNT(*)` → counts **all rows**, including ones with NULL values in any column.
- `COUNT(column_name)` → counts only rows where that **specific column is NOT NULL**.
- `COUNT(DISTINCT column_name)` → counts unique non-NULL values only.

---

## 2. SUM()

Returns the **total sum** of a numeric column.

```sql
SELECT SUM(Salary) FROM Employee;

-- Sum with condition
SELECT SUM(Salary) FROM Employee WHERE Department = 'IT';

-- Sum grouped by department
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employee
GROUP BY Department;
```

**Key points**
- `SUM()` automatically **ignores NULL values** (treats them as 0, doesn't error out).
- Works only on numeric columns.

---

## 3. AVG()

Returns the **average (mean)** value of a numeric column.

```sql
SELECT AVG(Salary) FROM Employee;

-- Average per department
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employee
GROUP BY Department;
```

**Key points**
- `AVG()` **ignores NULL values** both in the sum and in the count used for division.
  - Example: `AVG(Salary)` for IT (55000, 62000, NULL) = `(55000+62000)/2 = 58500`, **not** divided by 3.
- To treat NULL as 0 in the average, wrap it: `AVG(COALESCE(Salary, 0))`.

---

## 4. MAX()

Returns the **largest value** in a column.

```sql
SELECT MAX(Salary) FROM Employee;

-- Max per department
SELECT Department, MAX(Salary) AS HighestSalary
FROM Employee
GROUP BY Department;
```

**Key points**
- Works on numeric, string (alphabetical order), and date (latest date) columns.
- `MAX()` ignores NULL values.

---

## 5. MIN()

Returns the **smallest value** in a column.

```sql
SELECT MIN(Salary) FROM Employee;

-- Min per department
SELECT Department, MIN(Salary) AS LowestSalary
FROM Employee
GROUP BY Department;
```

**Key points**
- Works on numeric, string (alphabetical order), and date (earliest date) columns.
- `MIN()` ignores NULL values.

---

## 6. Combining Multiple Aggregate Functions

```sql
SELECT
    Department,
    COUNT(*) AS TotalEmployees,
    SUM(Salary) AS TotalSalary,
    AVG(Salary) AS AvgSalary,
    MAX(Salary) AS MaxSalary,
    MIN(Salary) AS MinSalary
FROM Employee
GROUP BY Department;
```

---

## 7. Filtering Aggregated Results — HAVING vs WHERE

`WHERE` filters rows **before** aggregation; `HAVING` filters groups **after** aggregation.

```sql
-- WRONG - can't use aggregate function directly in WHERE
-- SELECT Department, AVG(Salary) FROM Employee WHERE AVG(Salary) > 55000 GROUP BY Department;

-- CORRECT - use HAVING to filter on aggregated values
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employee
GROUP BY Department
HAVING AVG(Salary) > 55000;

-- WHERE + HAVING together
SELECT Department, COUNT(*) AS EmpCount
FROM Employee
WHERE Salary IS NOT NULL
GROUP BY Department
HAVING COUNT(*) > 1;
```

---

## Quick Reference Table

| Function | Purpose | NULL Handling |
|---|---|---|
| `COUNT(*)` | Count all rows | Includes rows with NULLs |
| `COUNT(column)` | Count non-NULL values in column | Excludes NULLs |
| `SUM(column)` | Total of numeric column | Ignores NULLs |
| `AVG(column)` | Average of numeric column | Ignores NULLs (in both sum & count) |
| `MAX(column)` | Largest value | Ignores NULLs |
| `MIN(column)` | Smallest value | Ignores NULLs |
| `WHERE` | Filter rows before aggregation | — |
| `HAVING` | Filter groups after aggregation | — |

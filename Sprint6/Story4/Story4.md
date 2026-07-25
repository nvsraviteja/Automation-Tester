# SQL Cheat Sheet — Sprint 6, Story 4
### Topic: GROUP BY | HAVING | HAVING vs WHERE

---

## 0. Sample Table Used in Examples: `Employee`

| EmpID | EmpName | Department | Salary |
|---|---|---|---|
| 101 | John | IT | 55000 |
| 102 | Priya | HR | 60000 |
| 103 | Raj | Finance | 50000 |
| 104 | Anita | IT | 62000 |
| 105 | Kabir | IT | 48000 |
| 106 | Meena | HR | 45000 |

---

## 1. GROUP BY

`GROUP BY` arranges rows into **groups** based on the values in one or more columns, so aggregate functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`) can be applied **per group** instead of the whole table.

```sql
-- Count employees per department
SELECT Department, COUNT(*) AS TotalEmployees
FROM Employee
GROUP BY Department;
```

**Result:**

| Department | TotalEmployees |
|---|---|
| IT | 3 |
| HR | 2 |
| Finance | 1 |

### More examples

```sql
-- Total salary per department
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employee
GROUP BY Department;

-- Average salary per department
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employee
GROUP BY Department;

-- Group by multiple columns
SELECT Department, JobTitle, COUNT(*) AS Total
FROM Employee
GROUP BY Department, JobTitle;
```

**Key points**
- Every column in the `SELECT` list that is **not** wrapped in an aggregate function **must** appear in the `GROUP BY` clause.
- `GROUP BY` executes **after** `WHERE` (row filtering) and **before** `ORDER BY` (sorting).
- Without `GROUP BY`, an aggregate function like `COUNT(*)` summarizes the **entire table** into one row; with `GROUP BY`, it summarizes **per group**.

---

## 2. HAVING

`HAVING` filters **groups** (created by `GROUP BY`) based on a condition — typically involving an **aggregate function**. This is the key reason `WHERE` can't be used for this purpose (see next section).

```sql
-- Departments with more than 1 employee
SELECT Department, COUNT(*) AS TotalEmployees
FROM Employee
GROUP BY Department
HAVING COUNT(*) > 1;

-- Departments where average salary exceeds 50000
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employee
GROUP BY Department
HAVING AVG(Salary) > 50000;

-- Combine multiple conditions
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employee
GROUP BY Department
HAVING SUM(Salary) > 100000 AND COUNT(*) >= 2;
```

**Key points**
- `HAVING` runs **after** grouping and aggregation — it filters the summarized/grouped results.
- Can reference aggregate functions directly (`COUNT(*)`, `SUM(Salary)`, etc.) — something `WHERE` cannot do.

---

## 3. HAVING vs WHERE

| Aspect | WHERE | HAVING |
|---|---|---|
| Filters | Individual rows | Groups (after `GROUP BY`) |
| Runs | **Before** grouping/aggregation | **After** grouping/aggregation |
| Aggregate functions | Cannot use (`WHERE COUNT(*) > 1` ❌) | Can use (`HAVING COUNT(*) > 1` ✅) |
| Used with | Any query | Typically used with `GROUP BY` |
| Applies to | Raw column values | Aggregated/summarized values |

### Side-by-side example

```sql
-- WHERE: filter rows BEFORE grouping (only non-NULL salaries considered)
-- HAVING: filter groups AFTER aggregation (only depts with total > 100000)
SELECT Department, SUM(Salary) AS TotalSalary
FROM Employee
WHERE Salary IS NOT NULL
GROUP BY Department
HAVING SUM(Salary) > 100000;
```

**Execution order for the query above:**
1. `FROM Employee` → get the table
2. `WHERE Salary IS NOT NULL` → filter individual rows first
3. `GROUP BY Department` → group the filtered rows
4. `SUM(Salary)` → calculate aggregate per group
5. `HAVING SUM(Salary) > 100000` → filter the grouped/aggregated results
6. `SELECT` → return final columns

**Common mistake:**
```sql
-- WRONG - WHERE cannot reference an aggregate function
-- SELECT Department, COUNT(*) FROM Employee WHERE COUNT(*) > 1 GROUP BY Department;

-- CORRECT
SELECT Department, COUNT(*) FROM Employee GROUP BY Department HAVING COUNT(*) > 1;
```

---

## Quick Reference Table

| Clause | Purpose | Filters | Runs Relative to Aggregation |
|---|---|---|---|
| `GROUP BY` | Groups rows sharing common values | — | Creates the groups |
| `HAVING` | Filters groups based on a condition | Groups | After |
| `WHERE` | Filters individual rows | Rows | Before |

**Rule of thumb:** *If your filter condition involves an aggregate function (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`), use `HAVING`. Otherwise, use `WHERE`.*

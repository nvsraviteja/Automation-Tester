# SQL Cheat Sheet — Sprint 6, Story 5
### Topic: Subqueries — Single-row, Multi-row, IN/ANY/ALL, Correlated, EXISTS/NOT EXISTS

---

## 0. Sample Tables Used in Examples

### `Employee`

| EmpID | EmpName | DeptID | Salary |
|---|---|---|---|
| 1 | John | 10 | 55000 |
| 2 | Priya | 20 | 60000 |
| 3 | Raj | 10 | 50000 |
| 4 | Anita | 10 | 62000 |
| 5 | Kabir | 30 | 45000 |

### `Department`

| DeptID | DeptName |
|---|---|
| 10 | IT |
| 20 | HR |
| 30 | Finance |

---

## 1. What is a Subquery?

A **subquery** (inner query / nested query) is a `SELECT` query written **inside another query**. It runs first, and its result is used by the outer query to filter, compare, or compute further.

```sql
SELECT EmpName
FROM Employee
WHERE Salary > (SELECT AVG(Salary) FROM Employee);
```

**Key points**
- The subquery `(SELECT AVG(Salary) FROM Employee)` runs first → returns a single average value.
- The outer query then uses that value to filter employees earning above average.
- Subqueries can appear in `WHERE`, `FROM`, `SELECT`, or `HAVING` clauses.

---

## 2. Single-Row Subquery

Returns **exactly one row, one column** — used with single-value comparison operators (`=`, `>`, `<`, `>=`, `<=`).

```sql
-- Employees earning more than John's salary
SELECT EmpName, Salary
FROM Employee
WHERE Salary > (SELECT Salary FROM Employee WHERE EmpName = 'John');

-- Employee(s) with the highest salary
SELECT EmpName
FROM Employee
WHERE Salary = (SELECT MAX(Salary) FROM Employee);
```

**Key point:** If a single-row subquery unexpectedly returns **more than one row**, SQL throws an error (`subquery returns more than 1 row`) — use a multi-row operator instead in that case.

---

## 3. Multi-Row Subquery

Returns **multiple rows** — must be used with operators that handle multiple values: `IN`, `ANY`, `ALL`, `EXISTS`.

```sql
-- Employees who work in departments located in IT or HR
SELECT EmpName
FROM Employee
WHERE DeptID IN (SELECT DeptID FROM Department WHERE DeptName IN ('IT', 'HR'));
```

**Key point:** Using `=` with a multi-row subquery throws an error — only `IN`/`ANY`/`ALL`/`EXISTS` work correctly here.

---

## 4. IN

Checks if a value **matches any value** returned by the subquery.

```sql
SELECT EmpName
FROM Employee
WHERE DeptID IN (SELECT DeptID FROM Department WHERE DeptName = 'IT' OR DeptName = 'HR');

-- NOT IN
SELECT EmpName
FROM Employee
WHERE DeptID NOT IN (SELECT DeptID FROM Department WHERE DeptName = 'Finance');
```

**Key point:** Be careful with `NOT IN` when the subquery can return `NULL` — if **any** row in the subquery result is `NULL`, the entire `NOT IN` condition returns no rows (unexpected empty result). Prefer `NOT EXISTS` in that situation.

---

## 5. ANY

Compares a value to **each value** returned by the subquery — condition is true if it matches **at least one** of them.

```sql
-- Employees earning more than ANY employee in department 20 (i.e., more than the minimum in dept 20)
SELECT EmpName, Salary
FROM Employee
WHERE Salary > ANY (SELECT Salary FROM Employee WHERE DeptID = 20);
```

**Key point:** `> ANY` effectively means "greater than the **minimum**" value in the subquery result — the condition succeeds if it beats even one value.

---

## 6. ALL

Compares a value against **every value** returned by the subquery — condition is true only if it holds for **all** of them.

```sql
-- Employees earning more than ALL employees in department 10 (i.e., more than the maximum in dept 10)
SELECT EmpName, Salary
FROM Employee
WHERE Salary > ALL (SELECT Salary FROM Employee WHERE DeptID = 10);
```

**Key point:** `> ALL` effectively means "greater than the **maximum**" value in the subquery result — must outperform every single row.

### ANY vs ALL Quick Comparison

| Operator | Meaning | Equivalent to |
|---|---|---|
| `> ANY (...)` | Greater than at least one value | `> MIN(...)` |
| `> ALL (...)` | Greater than every value | `> MAX(...)` |
| `< ANY (...)` | Less than at least one value | `< MAX(...)` |
| `< ALL (...)` | Less than every value | `< MIN(...)` |

---

## 7. Correlated Subquery

Unlike a regular subquery (which runs once, independently), a **correlated subquery** references a column from the **outer query** — so it runs **once per row** of the outer query.

```sql
-- Employees earning more than the average salary of their OWN department
SELECT e1.EmpName, e1.Salary, e1.DeptID
FROM Employee e1
WHERE e1.Salary > (
    SELECT AVG(e2.Salary)
    FROM Employee e2
    WHERE e2.DeptID = e1.DeptID   -- references outer query's table (e1)
);
```

**Key points**
- The inner query's `WHERE e2.DeptID = e1.DeptID` depends on the outer query's current row — this makes it "correlated."
- Executes row-by-row (re-evaluated for each outer row), so it can be **slower** than a regular subquery on large tables.
- Common use case: comparing each row against an aggregate calculated **specific to that row's group**.

---

## 8. EXISTS

Checks whether the subquery returns **at least one row** — returns `TRUE`/`FALSE`, doesn't care about the actual values returned.

```sql
-- Departments that have at least one employee
SELECT DeptName
FROM Department d
WHERE EXISTS (
    SELECT 1 FROM Employee e WHERE e.DeptID = d.DeptID
);
```

**Key points**
- `SELECT 1` is a common convention — the actual selected value doesn't matter since `EXISTS` only checks for row presence.
- Often more efficient than `IN` for large datasets since it can **short-circuit** (stop as soon as one match is found).
- Almost always used as a **correlated subquery** (references the outer table).

---

## 9. NOT EXISTS

Checks whether the subquery returns **zero rows** — the opposite of `EXISTS`.

```sql
-- Departments that have NO employees
SELECT DeptName
FROM Department d
WHERE NOT EXISTS (
    SELECT 1 FROM Employee e WHERE e.DeptID = d.DeptID
);
```

**Key point:** `NOT EXISTS` is generally **safer** than `NOT IN` when the subquery might return `NULL` values — `NOT EXISTS` doesn't suffer from the NULL-related empty-result issue that `NOT IN` does.

---

## Quick Reference Table

| Concept | Returns | Used With |
|---|---|---|
| Single-row subquery | 1 row, 1 column | `=`, `>`, `<`, `>=`, `<=` |
| Multi-row subquery | Multiple rows | `IN`, `ANY`, `ALL`, `EXISTS` |
| `IN` | Match any value in list | Multi-row subqueries |
| `ANY` | True if condition matches at least one row | Multi-row subqueries |
| `ALL` | True if condition matches every row | Multi-row subqueries |
| Correlated subquery | Re-evaluated per outer row | References outer query column |
| `EXISTS` | True if subquery returns ≥1 row | Correlated subqueries |
| `NOT EXISTS` | True if subquery returns 0 rows | Correlated subqueries |

**Rule of thumb:** *Use `EXISTS`/`NOT EXISTS` over `IN`/`NOT IN` when checking for row existence (especially with correlated conditions or when NULLs might be present) — it's both safer and often faster.*

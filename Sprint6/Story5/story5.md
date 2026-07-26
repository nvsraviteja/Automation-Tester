# SQL Cheat Sheet — Sprint 6, Story 5
### Topic: SQL Joins — Inner, Left, Right, Full Outer, Cross, Self

---

## 0. Sample Tables Used in Examples

### `Employee`

| EmpID | EmpName | DeptID |
|---|---|---|
| 1 | John | 10 |
| 2 | Priya | 20 |
| 3 | Raj | 10 |
| 4 | Anita | NULL |

### `Department`

| DeptID | DeptName |
|---|---|
| 10 | IT |
| 20 | HR |
| 30 | Finance |

---

## 1. Types of Join — Overview

A **JOIN** combines rows from two or more tables based on a related column between them.

| Join Type | Returns |
|---|---|
| `INNER JOIN` | Only matching rows in both tables |
| `LEFT JOIN` | All rows from left table + matched rows from right (NULL if no match) |
| `RIGHT JOIN` | All rows from right table + matched rows from left (NULL if no match) |
| `FULL OUTER JOIN` | All rows from both tables (NULL where no match on either side) |
| `CROSS JOIN` | Cartesian product — every row of table A with every row of table B |
| `SELF JOIN` | A table joined with itself |

---

## 2. INNER JOIN

Returns only the rows where there's a **match** in both tables.

```sql
SELECT e.EmpName, d.DeptName
FROM Employee e
INNER JOIN Department d ON e.DeptID = d.DeptID;
```

**Result:**

| EmpName | DeptName |
|---|---|
| John | IT |
| Priya | HR |
| Raj | IT |

**Key point:** Anita (DeptID = NULL) and Finance (no matching employee) are **excluded** — only rows matching on both sides appear.

---

## 3. LEFT JOIN (LEFT OUTER JOIN)

Returns **all rows from the left table**, plus matching rows from the right table. Unmatched right-side columns show `NULL`.

```sql
SELECT e.EmpName, d.DeptName
FROM Employee e
LEFT JOIN Department d ON e.DeptID = d.DeptID;
```

**Result:**

| EmpName | DeptName |
|---|---|
| John | IT |
| Priya | HR |
| Raj | IT |
| Anita | NULL |

**Key point:** Anita is included even though she has no matching department — `DeptName` shows `NULL`.

---

## 4. RIGHT JOIN (RIGHT OUTER JOIN)

Returns **all rows from the right table**, plus matching rows from the left table. Unmatched left-side columns show `NULL`.

```sql
SELECT e.EmpName, d.DeptName
FROM Employee e
RIGHT JOIN Department d ON e.DeptID = d.DeptID;
```

**Result:**

| EmpName | DeptName |
|---|---|
| John | IT |
| Raj | IT |
| Priya | HR |
| NULL | Finance |

**Key point:** Finance is included even though no employee belongs to it — `EmpName` shows `NULL`.

---

## 5. FULL OUTER JOIN

Returns **all rows from both tables** — matched where possible, `NULL` on whichever side has no match.

```sql
SELECT e.EmpName, d.DeptName
FROM Employee e
FULL OUTER JOIN Department d ON e.DeptID = d.DeptID;
```

**Result:**

| EmpName | DeptName |
|---|---|
| John | IT |
| Priya | HR |
| Raj | IT |
| Anita | NULL |
| NULL | Finance |

**Key point:** Combines the effect of `LEFT JOIN` + `RIGHT JOIN`. Note: **MySQL doesn't support `FULL OUTER JOIN` directly** — it's typically emulated using `UNION` of a `LEFT JOIN` and `RIGHT JOIN`:

```sql
SELECT e.EmpName, d.DeptName
FROM Employee e LEFT JOIN Department d ON e.DeptID = d.DeptID
UNION
SELECT e.EmpName, d.DeptName
FROM Employee e RIGHT JOIN Department d ON e.DeptID = d.DeptID;
```

---

## 6. CROSS JOIN

Returns the **Cartesian product** — every row from table A combined with every row from table B. No `ON` condition; result size = (rows in A) × (rows in B).

```sql
SELECT e.EmpName, d.DeptName
FROM Employee e
CROSS JOIN Department d;
```

**Result (4 employees × 3 departments = 12 rows):**

| EmpName | DeptName |
|---|---|
| John | IT |
| John | HR |
| John | Finance |
| Priya | IT |
| ... | ... |

**Key point:** Rarely used directly in real queries (can produce huge result sets) — mostly useful for generating combinations (e.g., all possible date × store combinations for reporting).

---

## 7. SELF JOIN

A table joined **with itself** — useful for comparing rows within the same table (e.g., employee-manager relationships).

### Sample table: `Employee` (with a manager reference)

| EmpID | EmpName | ManagerID |
|---|---|---|
| 1 | John | NULL |
| 2 | Priya | 1 |
| 3 | Raj | 1 |
| 4 | Anita | 2 |

```sql
SELECT e.EmpName AS Employee, m.EmpName AS Manager
FROM Employee e
LEFT JOIN Employee m ON e.ManagerID = m.EmpID;
```

**Result:**

| Employee | Manager |
|---|---|
| John | NULL |
| Priya | John |
| Raj | John |
| Anita | Priya |

**Key point:** The same table is given **two different aliases** (`e` and `m`) so it can be treated as two separate tables for the join. Typically implemented as a `LEFT JOIN` so rows without a match (e.g., the top-level manager) are still included.

---

## Quick Reference Table

| Join Type | Syntax Keyword | Includes Unmatched Rows? |
|---|---|---|
| Inner Join | `INNER JOIN` | No — only matches |
| Left Join | `LEFT JOIN` / `LEFT OUTER JOIN` | Yes — unmatched left rows |
| Right Join | `RIGHT JOIN` / `RIGHT OUTER JOIN` | Yes — unmatched right rows |
| Full Outer Join | `FULL OUTER JOIN` | Yes — unmatched rows from both sides |
| Cross Join | `CROSS JOIN` | N/A — all combinations, no matching condition |
| Self Join | Any join type, same table twice (aliased) | Depends on join type used |

---

## Visual Summary (Venn Diagram Logic)

```
INNER JOIN   →  A ∩ B                (only overlap)
LEFT JOIN    →  A (all) + overlap    (all of A, matched part of B)
RIGHT JOIN   →  B (all) + overlap    (all of B, matched part of A)
FULL OUTER   →  A ∪ B                (everything from both)
CROSS JOIN   →  A × B                (every combination, no overlap logic)
```

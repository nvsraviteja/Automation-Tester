# SQL Cheat Sheet — Sprint 6, Story 9.1
### Topic: Clustered vs Non-Clustered Index | Unique Index | Composite Index | Leftmost Prefix Rule | Interview Questions

---

## 0. Sample Table Used in Examples

```sql
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    Salary DECIMAL(10,2),
    Email VARCHAR(100)
);
```

---

## 1. Clustered Index

A **Clustered Index** determines the **physical order** in which data rows are actually stored on disk. The table data itself is sorted according to the clustered index's key.

```sql
-- Primary key automatically becomes the clustered index (SQL Server, MySQL InnoDB)
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,   -- this IS the clustered index
    EmpName VARCHAR(50)
);
```

**Key points**
- A table can have **only ONE clustered index**, because data rows can physically exist in only one order.
- Usually created automatically on the `PRIMARY KEY` column (in SQL Server and MySQL InnoDB).
- Since data is physically sorted by this key, retrieving rows using the clustered index (e.g., `WHERE EmpID = 101`) is extremely fast — no separate lookup needed.
- Range queries (`WHERE EmpID BETWEEN 100 AND 200`) are especially efficient since matching rows are physically adjacent.

---

## 2. Non-Clustered Index

A **Non-Clustered Index** is a **separate structure** from the actual table data — it stores the indexed column's values sorted, along with a **pointer** (row locator) back to the actual row's physical location.

```sql
CREATE INDEX idx_empname ON Employee(EmpName);
```

**Key points**
- A table can have **multiple non-clustered indexes** (unlike clustered, which is limited to one).
- Works like a book's index at the back — a separate lookup list pointing to actual page numbers (rows), rather than reordering the book's own pages.
- Slightly slower than a clustered index lookup (an extra step to follow the pointer to the actual row), but still vastly faster than a full table scan.

### Clustered vs Non-Clustered — Quick Comparison

| Aspect | Clustered Index | Non-Clustered Index |
|---|---|---|
| Data storage order | Physically sorts the table data | Separate structure with pointers to data |
| Count per table | Only 1 | Multiple allowed |
| Speed | Faster (data IS the index) | Slightly slower (extra pointer lookup) |
| Default on | Usually `PRIMARY KEY` | Manually created (`CREATE INDEX`) |

---

## 3. Unique Index

A **Unique Index** ensures all values in the indexed column(s) are **distinct**, while also providing the performance benefit of a normal index.

```sql
CREATE UNIQUE INDEX idx_email ON Employee(Email);
```

**Key points**
- Functionally similar to a `UNIQUE` constraint — in fact, creating a `UNIQUE` constraint automatically creates a unique index behind the scenes.
- Prevents duplicate values from being inserted, in addition to speeding up searches on that column.
- Commonly used on columns like `Email`, `Username`, or `PhoneNumber` where duplicates should never exist.

---

## 4. Composite Index

A **Composite Index** (a.k.a. concatenated/multi-column index) is built on **two or more columns together**, rather than a single column.

```sql
CREATE INDEX idx_dept_salary ON Employee(DeptID, Salary);
```

**Key points**
- Column **order matters** — this index is optimized for queries filtering on `DeptID` first, then optionally `Salary`.
- Most effective when queries commonly filter by the **same combination** of columns together.
- One composite index can often replace the need for several single-column indexes, if query patterns align with the leftmost prefix rule (see next section).

---

## 5. Leftmost Prefix Rule

For a composite index on `(ColumnA, ColumnB, ColumnC)`, the index can be used **only** if the query's `WHERE`/`ORDER BY` conditions include the columns **starting from the leftmost** column, in order.

```sql
CREATE INDEX idx_dept_salary_age ON Employee(DeptID, Salary, Age);
```

| Query Condition | Uses the Index? |
|---|---|
| `WHERE DeptID = 10` | ✅ Yes (leftmost column) |
| `WHERE DeptID = 10 AND Salary > 50000` | ✅ Yes (leftmost 2 columns, in order) |
| `WHERE DeptID = 10 AND Salary > 50000 AND Age > 30` | ✅ Yes (all 3 columns, in order) |
| `WHERE Salary > 50000` (skipping DeptID) | ❌ No (doesn't start from leftmost column) |
| `WHERE Age > 30` (skipping DeptID, Salary) | ❌ No (doesn't start from leftmost column) |

**Key point:** Think of it like a phone book sorted by (Last Name, First Name) — you can quickly search "Smith" or "Smith, John," but you can't efficiently search by first name alone ("John") without scanning the whole book, since the book isn't sorted by first name independently.

**Practical tip:** When designing a composite index, put the column that's **most frequently used alone or first** in `WHERE` clauses as the leftmost column.

---

## 6. Interview Questions

**Q1: What is the difference between a clustered and a non-clustered index?**
> A clustered index determines the physical storage order of table data (only 1 per table), while a non-clustered index is a separate structure with pointers to the actual rows (multiple allowed per table).

**Q2: Can a table have multiple clustered indexes?**
> No — only one, because data rows can physically be sorted in just one order at a time.

**Q3: Does creating a PRIMARY KEY automatically create an index?**
> Yes — it typically creates a clustered index (in SQL Server/MySQL InnoDB) or at minimum a unique index, depending on the RDBMS.

**Q4: What's the difference between a UNIQUE constraint and a UNIQUE INDEX?**
> They achieve a similar result (no duplicate values), but a `UNIQUE` constraint is a schema-level rule, while creating it automatically generates a unique index internally to enforce and speed up that rule.

**Q5: What is a composite index, and when should you use one?**
> An index built on multiple columns together — useful when queries frequently filter by the same combination of columns (e.g., `DeptID` + `Salary`).

**Q6: What is the leftmost prefix rule?**
> A composite index can only be used efficiently if the query conditions include the index's columns starting from the leftmost one, in order — skipping the leftmost column makes the index unusable for that query.

**Q7: Do indexes always improve performance?**
> No — they speed up reads (`SELECT`) but slow down writes (`INSERT`/`UPDATE`/`DELETE`) since the index must also be updated. Over-indexing a table can hurt overall performance.

**Q8: How do you check whether a query is actually using an index?**
> Using `EXPLAIN` (MySQL/PostgreSQL) or execution plan tools (SQL Server) to view the query's execution plan and confirm whether an index scan/seek is happening instead of a full table scan.

**Q9: Why is a clustered index generally faster than a non-clustered index for a given lookup?**
> Because the clustered index IS the data — there's no extra step to follow a pointer to a separate row location, unlike a non-clustered index which requires an additional lookup.

**Q10: If you have a composite index on (A, B, C), can a query filtering only on column B use this index?**
> No — because it violates the leftmost prefix rule; the query must include column A to make use of this index.

---

## Quick Reference Table

| Index Type | Count per Table | Key Characteristic |
|---|---|---|
| Clustered Index | 1 | Physically sorts table data |
| Non-Clustered Index | Multiple | Separate structure with pointers to rows |
| Unique Index | Multiple | Enforces distinct values + speeds up search |
| Composite Index | Multiple | Built on 2+ columns; leftmost prefix rule applies |

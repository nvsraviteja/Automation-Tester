# SQL Cheat Sheet — Sprint 6, Story 9
### Topic: Indexes

---

## 1. What is an Index?

An **Index** is a special database structure that improves the **speed of data retrieval** on a table, at the cost of some extra storage space and slightly slower writes (insert/update/delete).

```sql
CREATE INDEX idx_empname ON Employee(EmpName);
```

Think of it as a lookup structure the database maintains **alongside** the table, so it doesn't have to scan every row to find what you're looking for.

---

## 2. Why Indexes are Needed

Without an index, the database must check **every single row** in a table to find matching data — this is fine for small tables, but becomes very slow as tables grow to millions of rows.

- Speeds up `SELECT` queries with `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` clauses.
- Critical for performance in large production databases.
- Trade-off: indexes speed up reads but slightly slow down writes (`INSERT`/`UPDATE`/`DELETE`), since the index also needs updating.

---

## 3. Book Index Analogy

Think of a textbook:
- **Without an index:** to find "Normalization," you'd flip through every page from start to end (slow).
- **With an index:** you check the book's index page at the back, find "Normalization — Page 245," and jump straight there (fast).

A database index works the same way — it's a **sorted reference** pointing to where the actual data lives, so the database can jump directly to it instead of reading the whole table.

---

## 4. Full Table Scan

A **Full Table Scan** happens when the database has **no index** to use, so it reads **every row, one by one**, checking if it matches the query condition.

```sql
-- Without an index on EmpName, this triggers a full table scan
SELECT * FROM Employee WHERE EmpName = 'John';
```

**Key point:** Full table scans are acceptable for small tables but become a major performance bottleneck on large tables (millions of rows) — this is exactly the problem indexes solve.

---

## 5. Searching Data With an Index

```sql
-- With an index on EmpName, the database uses the index to jump directly to matching rows
CREATE INDEX idx_empname ON Employee(EmpName);

SELECT * FROM Employee WHERE EmpName = 'John';  -- now uses the index, much faster
```

**Key point:** The query syntax doesn't change — the database's **query optimizer** automatically decides whether to use an available index behind the scenes.

---

## 6. How an Index Works (Concept)

- An index stores a **sorted copy of the indexed column's values**, each paired with a pointer to the actual row's location in the table.
- When you search using an indexed column, the database uses this **sorted structure** to quickly locate matching pointers, then fetches only those specific rows — instead of scanning the whole table.
- Most relational databases implement indexes internally using a **B-Tree** (Balanced Tree) structure.

---

## 7. B-Tree (High-Level Overview)

A **B-Tree (Balanced Tree)** is the most common data structure used to implement indexes.

- Data is organized in a **tree structure** with a root node, branch nodes, and leaf nodes.
- Every path from the root to a leaf is the **same length** (balanced), keeping lookups consistently fast regardless of which value you're searching for.
- At each level, the tree narrows down the search range (similar to a binary search), quickly eliminating large portions of data that can't match.
- Leaf nodes contain pointers to the actual table rows.

**Key point:** You don't need to implement a B-Tree yourself — the database engine (MySQL, PostgreSQL, etc.) manages this internally when you run `CREATE INDEX`. Understanding it conceptually just helps explain *why* indexed lookups are so much faster.

---

## 8. Time Complexity (O(n) vs O(log n)) — Basic Understanding

| Scenario | Time Complexity | Meaning |
|---|---|---|
| Full table scan (no index) | `O(n)` | Time grows **linearly** with the number of rows — 1 million rows = up to 1 million checks |
| Indexed search (B-Tree) | `O(log n)` | Time grows **logarithmically** — 1 million rows ≈ only ~20 comparisons |

**Example intuition:**
- 1,000,000 rows, no index → worst case ~1,000,000 row checks.
- 1,000,000 rows, with B-Tree index → worst case ~20 comparisons (log₂ 1,000,000 ≈ 20).

**Key point:** This is *why* indexes matter so much at scale — the performance gap between `O(n)` and `O(log n)` becomes enormous as table size grows.

---

## 9. Creating an Index (`CREATE INDEX`)

```sql
-- Basic index on one column
CREATE INDEX idx_empname ON Employee(EmpName);

-- Index on multiple columns (composite index)
CREATE INDEX idx_dept_salary ON Employee(DeptID, Salary);

-- Unique index (also enforces uniqueness, like a UNIQUE constraint)
CREATE UNIQUE INDEX idx_email ON Employee(Email);
```

**Key points**
- Index names must be unique within the database (naming convention: `idx_<table>_<column>`).
- A composite index is most effective when queries filter on the **leftmost column(s)** of the index first.

---

## 10. Using an Index in Queries

You don't explicitly "call" an index in a query — you just query normally, and the database's optimizer decides whether to use it.

```sql
SELECT * FROM Employee WHERE EmpName = 'John';         -- uses idx_empname if it exists
SELECT * FROM Employee WHERE DeptID = 10 AND Salary > 50000;  -- uses idx_dept_salary if it exists
```

**Key point:** You can check if an index is actually being used via `EXPLAIN` (MySQL/PostgreSQL) to see the query execution plan:
```sql
EXPLAIN SELECT * FROM Employee WHERE EmpName = 'John';
```

---

## 11. Dropping an Index (`DROP INDEX`)

```sql
-- MySQL syntax
DROP INDEX idx_empname ON Employee;

-- PostgreSQL / SQL Server syntax
DROP INDEX idx_empname;
```

**Key point:** Dropping an index only removes the lookup structure — the actual table data is completely unaffected.

---

## 12. Relationship Between Primary Key and Index

- A `PRIMARY KEY` **automatically creates an index** (usually a unique B-Tree index) on that column — you don't need to manually create one.
- Similarly, a `UNIQUE` constraint also automatically creates an index.
- This is why lookups by primary key are always fast, even without explicitly running `CREATE INDEX`.

```sql
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,   -- automatically indexed
    EmpName VARCHAR(50)      -- NOT indexed unless you create one manually
);
```

**Key point:** If you frequently query by a **non-primary-key column** (e.g., `EmpName`, `Email`, `DeptID`), you need to create an index on it explicitly — the primary key index alone won't help those queries.

---

## 13. Real-World QA Example

- **Test data setup:** A QA automation script inserts/searches thousands of test records daily. Without an index on a lookup column (e.g., `TestCaseID` or `OrderID`), test execution slows down significantly as the test database grows.
- **Verifying query performance:** QA/performance testers use `EXPLAIN` to confirm a critical production query is actually using the expected index, rather than falling back to a full table scan — an important part of performance test validation.
- **Regression around schema changes:** When a developer removes or renames a column that has an index, QA should verify that dependent indexes/constraints are still intact and searches still perform as expected.
- **Load testing:** Indexes are a key factor validated during load/performance testing — a missing index on a frequently searched column is a common root cause of slow response times found during testing.

---

## 14. Benefits of Indexes

- Dramatically **faster SELECT queries** on large tables.
- Speeds up `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` operations.
- Enforces uniqueness when combined with `UNIQUE INDEX`.
- Reduces the load on the database engine for read-heavy applications.

**Trade-offs to be aware of:**
- Extra storage space required for the index structure.
- Slightly slower `INSERT`/`UPDATE`/`DELETE` (index must be updated too).
- Too many indexes on one table can hurt write performance — indexes should be added deliberately, not on every column.

---

## 15. Key Takeaways

- An index is like a book's index — it lets the database jump directly to relevant data instead of scanning everything.
- Without an index → **full table scan** → `O(n)` — slow on large tables.
- With an index (typically a **B-Tree**) → `O(log n)` — dramatically faster.
- `PRIMARY KEY` and `UNIQUE` constraints automatically create indexes; other columns need manual `CREATE INDEX`.
- Indexes speed up reads but come with storage and write-performance trade-offs — use them thoughtfully, not on every column.
- `EXPLAIN` helps verify whether a query is actually using an index.

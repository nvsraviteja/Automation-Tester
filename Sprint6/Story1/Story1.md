# Database Fundamentals — Sprint 6, Story 1 Cheat Sheet
### Topic: DB Basics, DBMS vs RDBMS, Keys, Constraints, Normalization

---

## 1. What is a Database?

A **database** is an organized collection of structured data stored electronically so it can be easily accessed, managed, and updated.

- Data is stored in a way that allows efficient **storage, retrieval, update, and deletion**.
- Examples: a list of employees, customer orders, product inventory, student records.
- Managed through software called a **DBMS** (Database Management System).

---

## 2. DBMS vs RDBMS

| Aspect | DBMS | RDBMS |
|---|---|---|
| Full form | Database Management System | Relational Database Management System |
| Data storage | Stores data as files (no relation between data) | Stores data in **tables** with relationships between them |
| Relationships | Not supported | Supported (via keys) |
| Data redundancy | Common (no normalization enforced) | Minimized (through normalization) |
| ACID properties | Not necessarily followed | Follows ACID (Atomicity, Consistency, Isolation, Durability) |
| Examples | File systems, XML databases | MySQL, Oracle, PostgreSQL, SQL Server |
| Query language | May or may not use SQL | Uses SQL |
| Multiple users | Limited/no support | Supports multiple users with data integrity |

**Key point:**
> Every RDBMS is a DBMS, but not every DBMS is an RDBMS. RDBMS adds the relational model — tables linked via keys, constraints, and normalization rules.

---

## 3. Tables

A **table** is the fundamental structure in an RDBMS where data is stored in a **row-column format** — similar to a spreadsheet.

```sql
CREATE TABLE Employee (
    EmpID INT,
    EmpName VARCHAR(50),
    Salary DECIMAL(10,2)
);
```

- Each table has a unique name within the database.
- A database can contain multiple related tables (e.g., `Employee`, `Department`, `Salary`).

---

## 4. Rows & Columns

- **Row (Record / Tuple):** A single entry in a table — represents one complete set of related data.
- **Column (Field / Attribute):** Represents a single property/characteristic of the data, shared across all rows.

**Example:**

| EmpID (column) | EmpName (column) | Salary (column) |
|---|---|---|
| 101 | John | 50000 |  ← Row 1
| 102 | Priya | 60000 | ← Row 2

- Each **row** = one employee's complete data.
- Each **column** = one attribute (EmpID, EmpName, Salary) for every employee.

---

## 5. Data Types

Defines what kind of value a column can hold. Common SQL data types:

| Category | Data Type | Description |
|---|---|---|
| Numeric | `INT` | Whole numbers |
| Numeric | `DECIMAL(p,s)` / `FLOAT` | Decimal/fractional numbers |
| String | `VARCHAR(n)` | Variable-length text, max n characters |
| String | `CHAR(n)` | Fixed-length text |
| Date/Time | `DATE` | Stores date (YYYY-MM-DD) |
| Date/Time | `DATETIME` / `TIMESTAMP` | Stores date + time |
| Boolean | `BOOLEAN` / `BIT` | True/False, 1/0 |
| Large text | `TEXT` | Large blocks of text |

**Key point:**
> Choosing the correct data type ensures data integrity (e.g., you can't accidentally store text in a numeric salary column) and optimizes storage.

---

## 6. Primary Key

A column (or set of columns) that **uniquely identifies each row** in a table.

```sql
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50)
);
```

**Rules:**
- Must contain **unique** values (no duplicates).
- Cannot contain **NULL** values.
- Only **one** primary key per table (though it can span multiple columns — see Composite Key).

---

## 7. Foreign Key

A column in one table that refers to the **Primary Key** of another table — used to establish a **relationship** between two tables.

```sql
CREATE TABLE Department (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50)
);

CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);
```

**Key points:**
- Enforces **referential integrity** — you can't insert an `Employee` with a `DeptID` that doesn't exist in `Department`.
- Can contain duplicate values and NULLs (unlike a primary key).
- Links "child" table (`Employee`) to "parent" table (`Department`).

---

## 8. Unique Key

Ensures all values in a column are **distinct**, similar to a primary key, but:

```sql
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE
);
```

| Aspect | Primary Key | Unique Key |
|---|---|---|
| NULL values | Not allowed | Allowed (usually one NULL) |
| Count per table | Only 1 | Multiple allowed |
| Purpose | Main row identifier | Enforce uniqueness on other columns (e.g., email, phone) |

---

## 9. Composite Key

A **Primary Key made up of two or more columns** together, used when a single column isn't enough to uniquely identify a row.

```sql
CREATE TABLE OrderItems (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID)
);
```

**Key point:**
> Individually, `OrderID` and `ProductID` may repeat across rows, but the **combination** of both is unique for each row.

---

## 10. Constraints

Rules enforced on table columns to maintain data accuracy and integrity.

| Constraint | Purpose |
|---|---|
| `PRIMARY KEY` | Uniquely identifies each row |
| `FOREIGN KEY` | Links to another table's primary key |
| `UNIQUE` | Ensures all values in a column are distinct |
| `NOT NULL` | Column cannot have a NULL/empty value |
| `CHECK` | Restricts values based on a condition (e.g., `Age >= 18`) |
| `DEFAULT` | Assigns a default value if none is provided |

```sql
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    Age INT CHECK (Age >= 18),
    Status VARCHAR(20) DEFAULT 'Active',
    Email VARCHAR(100) NOT NULL UNIQUE
);
```

---

## 11. Normalization (1NF, 2NF, 3NF)

**Normalization** is the process of organizing table structure to **reduce data redundancy** and **avoid update/insert/delete anomalies**, by splitting large tables into smaller related ones.

### 1NF (First Normal Form)
- Each column must hold **atomic (indivisible)** values — no multiple values in a single cell.
- No repeating groups of columns.

**Before (violates 1NF):**
| StudentID | Name | Subjects |
|---|---|---|
| 1 | John | Math, Science |

**After (1NF applied):**
| StudentID | Name | Subject |
|---|---|---|
| 1 | John | Math |
| 1 | John | Science |

### 2NF (Second Normal Form)
- Must already be in 1NF.
- Every non-key column must depend on the **whole** primary key (relevant when using a composite key) — no **partial dependency**.

**Before (violates 2NF — composite key StudentID+CourseID):**
| StudentID | CourseID | CourseName | Marks |
|---|---|---|---|
CourseName depends only on CourseID, not the full composite key.

**After (2NF applied) — split into two tables:**
- `StudentCourse(StudentID, CourseID, Marks)`
- `Course(CourseID, CourseName)`

### 3NF (Third Normal Form)
- Must already be in 2NF.
- No **transitive dependency** — non-key columns must depend only on the primary key, not on another non-key column.

**Before (violates 3NF):**
| EmpID | DeptID | DeptName |
|---|---|---|
DeptName depends on DeptID, not directly on EmpID (transitive dependency).

**After (3NF applied) — split into two tables:**
- `Employee(EmpID, DeptID)`
- `Department(DeptID, DeptName)`

**Key point:**
> Each normal form builds on the previous one: 1NF removes repeating/multi-valued columns → 2NF removes partial dependency (composite keys) → 3NF removes transitive dependency (non-key depending on non-key).

---

## Quick Reference Table

| Term | One-Line Definition |
|---|---|
| Database | Organized collection of structured data |
| DBMS | Software to manage databases (no relationships) |
| RDBMS | DBMS + relational model (tables linked via keys) |
| Table | Data stored in rows and columns |
| Row | A single record |
| Column | A single attribute/field |
| Primary Key | Uniquely identifies each row, no NULL, one per table |
| Foreign Key | Links to another table's primary key |
| Unique Key | Ensures distinct values, allows NULL |
| Composite Key | Primary key made of 2+ columns combined |
| Constraint | Rule to maintain data integrity (`NOT NULL`, `CHECK`, etc.) |
| 1NF | Atomic values, no repeating groups |
| 2NF | 1NF + no partial dependency |
| 3NF | 2NF + no transitive dependency |

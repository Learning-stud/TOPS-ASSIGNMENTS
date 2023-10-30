# Database and SQL Basics

## 1. What do you understand By Database?
   A **database** is a structured collection of data used to store and manage information efficiently. Databases can be used for various applications, from simple address books to complex enterprise systems.

## 2. What is Normalization?
   **Normalization** is the process of organizing a relational database to reduce data redundancy and improve data integrity. It involves breaking down large tables into smaller, related tables and defining relationships between them.

## 3. What is the Difference between DBMS and RDBMS?
   - **DBMS (Database Management System)**: Provides basic data management functionalities but may not enforce strict data integrity and relationships between tables.
   - **RDBMS (Relational Database Management System)**: Manages data using a relational model, enforces data integrity, and provides support for SQL.

## 4. What is MF Cod Rule of RDBMS Systems?
   (Note: I couldn't find information about the "MF Cod Rule" in the context of RDBMS systems. Please provide more context or check for any typos in the question.)

## 5. What do you understand By Data Redundancy?
   **Data redundancy** occurs when the same data is stored in multiple places within a database, leading to increased storage requirements and potential data inconsistencies.

## 6. What is DDL Interpreter?
   A **DDL (Data Definition Language) interpreter** processes SQL statements for creating, altering, and deleting database objects.

## 7. What is DML Compiler in SQL?
   A **DML (Data Manipulation Language) compiler** processes SQL statements for querying, inserting, updating, and deleting data in a database.

## 8. What is SQL Key Constraints writing an Example of SQL Key Constraints?
   SQL key constraints include:
   - **Primary Key**: Ensures uniqueness and identifies each row in a table.
   - **Unique Key**: Ensures uniqueness but does not necessarily identify each row.
   - **Foreign Key**: Enforces relationships between tables.

   Example of a Primary Key:
   ```sql
   CREATE TABLE Students (
       StudentID INT PRIMARY KEY,
       FirstName VARCHAR(50),
       LastName VARCHAR(50)
   );
```


## 9.What is save Point? How to create a save Point write a Query? 


# Save Point and Trigger in SQL

### What is a Save Point, and how to create a Save Point using SQL?

A **Save Point** in SQL is a point within a transaction to which you can roll back without rolling back the entire transaction. It allows you to save the current state of a transaction and return to it if needed.

To create a Save Point, we can use it as given below  in SQL query:

```sql ```
##  SAVEPOINT my_savepoint;


## 10  What is trigger and how to create a Trigger in SQL? 

### A trigger in SQL is a database object that automatically executes a set of SQL statements when specific events occur. Triggers are commonly used to enforce data integrity, log changes, or automate actions based on database events.

## To create a Trigger in SQL, you can use the CREATE TRIGGER statement. Here's an example:


```
CREATE TRIGGER log_changes
AFTER INSERT OR UPDATE OR DELETE ON your_table
FOR EACH ROW
BEGIN
    -- Your SQL statements to log the changes go here
    -- For example, you can INSERT into a log table.
END;

```


# SAVE POINT EXAMPLE 

``` SQL
-- Start a transaction
BEGIN;

-- Perform some operations
INSERT INTO Customers (CustomerID, FirstName, LastName)
VALUES (1, 'John', 'Doe');

-- Create a Save Point
SAVEPOINT my_savepoint;

-- More operations
UPDATE Orders
SET OrderStatus = 'Shipped'
WHERE OrderID = 1001;

-- Roll back to the Save Point
ROLLBACK TO my_savepoint;

-- Commit the transaction
COMMIT;


```


# TRIGGER EXAMPLE

```SQL
-- Create a log table to store changes
CREATE TABLE ChangeLog (
    ChangeID INT PRIMARY KEY,
    TableName VARCHAR(50),
    ChangeType VARCHAR(10),
    ChangeDescription VARCHAR(255),
    ChangeTimestamp TIMESTAMP
);

-- Create a trigger to log changes
CREATE TRIGGER log_changes
AFTER INSERT OR UPDATE OR DELETE ON Orders
FOR EACH ROW
BEGIN
    INSERT INTO ChangeLog (TableName, ChangeType, ChangeDescription, ChangeTimestamp)
    VALUES ('Orders', 
            CASE
                WHEN NEW.OrderID IS NOT NULL THEN 'INSERT'
                WHEN OLD.OrderID IS NOT NULL AND NEW.OrderID IS NOT NULL THEN 'UPDATE'
                WHEN OLD.OrderID IS NOT NULL THEN 'DELETE'
            END,
            CONCAT('Order ID: ', COALESCE(OLD.OrderID, NEW.OrderID)),
            NOW());
END;

```
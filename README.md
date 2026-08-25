# Background

SQL sublanguage: DQL (Data Query Language)

We have learned how to query all records from a table as well as filter the amount of records we get back
utilizing the WHERE keyword. In this lab we are going to learn how to filter the amount of columns that we want
returned.

The syntax to return an entire table:

SELECT \* FROM table_name;

We can instead specify only the columns we want to display:

SELECT col_1, col_2, ...col_N FROM table_name;

## Problem 1

Assume the following table already exists.

| id  | firstname | lastname |
| --- | --------- | -------- |
| 1   | Steve     | Garcia   |
| 2   | Alexa     | Smith    |
| 3   | Steve     | Jones    |
| 4   | Brandon   | Smith    |
| 5   | Adam      | Jones    |

Write an SQL statement in `problem1.sql` that returns only the `firstname` column from the `site_user` table.

> **Note:** SQL table and column names are case-insensitive in SQLite (and most other databases) - `song`,
> `Song`, and `SONG` all refer to the same table. This only applies to identifiers (table/column names), not to
> data, string values in single quotes ARE case-sensitive, so `WHERE artist = 'beatles'` would NOT match a row
> stored as `'Beatles'`.

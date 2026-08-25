import os
import sqlite3

from src.main.user import User

"""
SQL sublanguage: DQL (Data Query Language)

We have learned how to query all records from a table as well as filter the amount of records we get back utilizing
the WHERE keyword.

In this lab we are going to learn how to filter the amount of columns that we want returned.

Let's take a look at the syntax to return an entire table again:
SELECT * FROM table_name;

In the statement above, the * is the wildcard to retrieve all the columns in this specific table.
However, we can specify the columns that we want to display by the following syntax:
SELECT col_1, col_2, ...col_N FROM table_name;
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def problem1():
    """
    problem 1: Write the SQL statement in the problem1.sql file to return only the 'firstname' column from the
    site_user table.

         site_user table:
         |   id  |     firstname        |        lastname        |
         ----------------------------------------------------------
         |1      |'Steve'               |'Garcia'                |
         |2      |'Alexa'               |'Smith'                 |
         |3      |'Steve'               |'Jones'                 |
         |4      |'Brandon'             |'Smith'                 |
         |5      |'Adam'                |'Jones'                 |
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE site_user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT
    );
    """)
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Steve', 'Garcia');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Alexa', 'Smith');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Steve', 'Jones');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Brandon', 'Smith');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Adam', 'Jones');")
    conn.commit()

    users = []
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            users.append(User(0, row[0], None))
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return users

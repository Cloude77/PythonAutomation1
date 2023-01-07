import sqlite3

DB_NAME = "sqlite_db.db"  # file variable

# connect db

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)

# create sql query to create table. New table
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = """CREATE TABLE IF NOT EXISTS courses (
          id integer PRIMARY KEY,
          title text NOT NULL,
          students_qty integer,
          reviews_qty integer
      );"""
    sqlite_conn.execute(sql_request)

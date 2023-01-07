import sqlite3

DB_NAME = "sqlite_db.db"  # file variable

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses"
    sql_cursor = sqlite_conn.execute(sql_request)  # execute returns cursor

    # 1 example
    for record in sql_cursor:
        # print(record[1])
        print(record)  # (251, 'Python course', 100, 30) (351, 'JavaScript course', 415, 100)

    # 2 example

    # records = sql_cursor.fetchall() # return a list
    # print(records) # [(251, 'Python course', 100, 30), (351, 'JavaScript course', 415, 100)

    print(end='================================================================\n\n')

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty>=50"
    sql_cursor = sqlite_conn.execute(sql_request)  # execute returns cursor

    # 1 example
    for record in sql_cursor:
        print(record)  # (251, 'Python course', 100, 30) (351, 'JavaScript course', 415, 100)

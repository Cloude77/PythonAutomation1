import sqlite3

DB_NAME = "sqlite_db.db"  # file variable

courses = [
    (351, "JavaScript course", 415, 100),
    (614, "C++ course", 161, 10),
    (721, "Java full course", 100, 35)
]

# insert value

with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    #  sqlite_conn.execute(sql_request, (251, "Python course", 100, 30)) # The 1 st request
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()  # changes in db

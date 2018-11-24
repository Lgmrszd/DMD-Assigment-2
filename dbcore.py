import sqlite3

DB_NAME = "database.db"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# cur.execute("CREATE TABLE test("
#             "id NUMBER PRIMARY KEY,"
#             "name VARCHAR[50]);")

conn.commit()

cur.close()
conn.close()

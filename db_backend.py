from dbcore import conn

with open("creation.sql", "r") as f:
    creation_sql = f.read()


def create_tables():
    conn.executescript(creation_sql)
    conn.commit()

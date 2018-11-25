import dbcore
import dbtypes
import db_backend

conn = dbcore.conn

db_backend.create_tables()

# t1 = dbtypes.Test(conn, {"name": "AAAA"})
# print(t1.name)
cp = dbtypes.PartsProviders(conn, {"NAME": "FSD", "PHONE": "FSD", "ADDRESS": "dadas"})
cp.insert()

# cur = conn.cursor()
# cur.execute("INSERT INTO CAR_PARTS VALUES (?)", "A")
# cur.close()
# conn.commit()

import dbcore
import dbtypes
import db_backend
import test_data

conn = dbcore.conn

db_backend.create_tables()
db_backend.create_test_data()

# t1 = dbtypes.Test(conn, {"name": "AAAA"})
# print(t1.name)
# cp = dbtypes.PartsProviders({"NAME": "FSD", "PHONE": "FSD", "ADRESS": "dadas"})
# cp.insert()


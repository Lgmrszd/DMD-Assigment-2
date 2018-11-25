import dbcore
import dbtypes
import db_backend

conn = dbcore.conn

db_backend.create_tables()

# t1 = dbtypes.Test(conn, {"name": "AAAA"})
# print(t1.name)
cp = dbtypes.PartsProviders({"NAME": "FSD", "PHONE": "FSD", "ADRESS": "dadas"})
cp.insert()

print(dbtypes.parts_providers_select())
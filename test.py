import dbcore
import dbtypes

conn = dbcore.conn

t1 = dbtypes.Test(conn, {"name": "AAAA"})

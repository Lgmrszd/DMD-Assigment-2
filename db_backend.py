from dbcore import conn
import test_data
import datetime

with open("creation.sql", "r") as f:
    creation_sql = f.read()


def check_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def create_tables():
    conn.executescript(creation_sql)
    conn.commit()


def clear_tables():
    tables = ['PAYMENT', 'CHARGES', 'ORDERS', 'REPAIRS', 'AVAILABLE_PARTS', 'PARTS_FOR', 'SOCKETS', 'CAN_PROVIDE',
              'CHARGING_STATIONS', 'CUSTOMERS', 'CARS', 'CAR_TYPES', 'WORKSHOPS', 'CAR_PARTS', 'PARTS_PROVIDERS']
    cur = conn.cursor()
    for table in tables:
        cur.execute("DELETE FROM {}".format(table))
    conn.commit()
    cur.close()


def _selection(sql_statement, data=None):
    cur = conn.cursor()
    if data:
        cur.execute(sql_statement, data)
    else:
        cur.execute(sql_statement)
    result = cur.fetchall()
    cur.close()
    return result


def _insertion(sql_statement, data):
    cur = conn.cursor()
    if isinstance(data, list):
        cur.executemany(sql_statement, data)
    else:
        cur.execute(sql_statement, data)
    conn.commit()
    cur.close()


def create_test_data():
    sql_statement = "INSERT INTO `CAR_TYPES` (MODEL,PLUG_TYPE) VALUES (?, ?);"
    car_types = test_data.car_types()
    _insertion(sql_statement, car_types)

    sql_statement = "INSERT INTO `CAR_PARTS` (NAME) VALUES (?);"
    parts = test_data.parts()
    _insertion(sql_statement, parts)

    sql_statement = "INSERT INTO `PARTS_FOR` (NAME,MODEL) VALUES (?, ?);"
    parts_for = test_data.parts_for()
    _insertion(sql_statement, parts_for)

    sql_statement = "INSERT INTO `PARTS_PROVIDERS` (ID,ADRESS,NAME,PHONE) VALUES (?, ?, ?, ?);"
    parts_providers = test_data.parts_providers()
    _insertion(sql_statement, parts_providers)

    sql_statement = "INSERT INTO `CAN_PROVIDE` (ID,NAME) VALUES (?, ?);"
    can_provide = test_data.can_provide()
    _insertion(sql_statement, can_provide)

    sql_statement = "INSERT INTO `CARS` (CAR_ID, COLOR, MODEL) VALUES (?, ?, ?)"
    cars = test_data.cars()
    _insertion(sql_statement, cars)

    sql_statement = "INSERT INTO `WORKSHOPS` (WID,GPS_LOCATION,AVAILABILITY) VALUES (?, ?, ?);"
    workshops = test_data.workshops()
    _insertion(sql_statement, workshops)

    sql_statement = "INSERT INTO `CUSTOMERS` (USERNAME,EMAIL,PHONE,FULL_NAME,COUNTRY,CITY,ZIP_CODE) " \
                    "VALUES (?, ?, ?, ?, ?, ?, ?);"
    customers = test_data.customers()
    _insertion(sql_statement, customers)

    sql_statement = "INSERT INTO `CHARGING_STATIONS` (UID,GPS_LOCATION,CHARGING_COST,CHARGING_TIME) " \
                    "VALUES (?, ?, ?, ?);"
    charging_stations = test_data.charging_stations()
    _insertion(sql_statement, charging_stations)

    sql_statement = "INSERT INTO `SOCKETS` (UID,PLUG_TYPE,NUMBER) VALUES (?, ?, ?);"
    sockets = test_data.sockets()
    _insertion(sql_statement, sockets)

    sql_statement = "INSERT INTO `AVAILABLE_PARTS` (NAME,WID) VALUES (?, ?);"
    available_parts = test_data.available_parts()
    _insertion(sql_statement, available_parts)

    sql_statement = "INSERT INTO `REPAIRS` (WID,CAR_ID,DATETIME,STATUS,PRICE) " \
                    "VALUES (?, ?, ?, ?, ?);"
    repairs = test_data.repairs()
    _insertion(sql_statement, repairs)

    orders, payments = test_data.orders_payments(cars)
    sql_statement = "INSERT INTO `ORDERS` " \
                    "(USERNAME,CAR_ID,DATETIME,FROM_,TO_,STATUS,PRICE,TRAVELED_TO_CLIENT,DURATION) " \
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
    _insertion(sql_statement, orders)
    sql_statement = "INSERT INTO `PAYMENT` (USERNAME,CAR_ID,ORDER_DATETIME,PAYMENT_DATETIME,AMOUNT) " \
                    "VALUES (?, ?, ?, ?, ?);"
    _insertion(sql_statement, payments)

    sql_statement = "INSERT INTO `CHARGES` (UID,CAR_ID,DATETIME,STATUS,CHARGING_TIME,COST) " \
                    "VALUES (?, ?, ?, ?, ?, ?);"
    charges = test_data.charges(cars)
    _insertion(sql_statement, charges)


def cars_select():
    sql_statement = "select C.CAR_ID, C.MODEL, T.PLUG_TYPE, C.COLOR from CARS C, CAR_TYPES T where C.MODEL = T.MODEL;"
    return _selection(sql_statement)


def customers_select():
    sql_statement = "select C.USERNAME, C.EMAIL, C.PHONE, C.FULL_NAME, C.COUNTRY, C.CITY, C.ZIP_CODE from CUSTOMERS C;"
    return _selection(sql_statement)


def orders_select():
    sql_statement = "select O.USERNAME, O.CAR_ID, O.FROM_, O.TO_, O.DATETIME, O.DURATION, " \
                    "O.TRAVELED_TO_CLIENT, O.STATUS, O.PRICE from ORDERS O;"
    return _selection(sql_statement)


def workshops_select():
    sql_statement = "select W.WID, W.GPS_LOCATION, W.AVAILABILITY from WORKSHOPS W;"
    return _selection(sql_statement)


def parts_in_workshop_select():
    sql_statement = "select AP.WID, AP.NAME from AVAILABLE_PARTS AP;"
    return _selection(sql_statement)


def can_provide_select():
    sql_statement = "select CP.ID, CP.NAME from CAN_PROVIDE CP;"
    return _selection(sql_statement)


def repairs_select():
    sql_statement = "select R.CAR_ID, R.WID, R.DATETIME, R.STATUS, R.PRICE from REPAIRS R;"
    return _selection(sql_statement)


def charging_stations_select():
    sql_statement = (
        "select C.UID, GROUP_CONCAT(S.PLUG_TYPE||'-'||S.NUMBER, '; '), "
        "C.CHARGING_COST, C.GPS_LOCATION, C.CHARGING_TIME\n"
        "from CHARGING_STATIONS C, SOCKETS S\n"
        "where C.UID = S.UID\n"
        "GROUP BY C.UID;")
    return _selection(sql_statement)


def charges_select():
    sql_statement = "select CH.CAR_ID, CH.UID, CH.DATETIME, CH.CHARGING_TIME, CH.COST    from CHARGES CH;"
    return _selection(sql_statement)


def parts_providers_select():
    sql_statement = "select P.ID, P.ADRESS, P.NAME, P.PHONE from PARTS_PROVIDERS P;"
    return _selection(sql_statement)


def payment_select():
    sql_statement = "select P.ORDER_DATETIME, P.PAYMENT_DATETIME, P.AMOUNT, P.USERNAME, P.CAR_ID from PAYMENT P;"
    return _selection(sql_statement)


def init():
    create_tables()


def query1():
    sql_statement = ("SELECT car_id\n"
                     "FROM cars\n"
                     "WHERE color LIKE 'Red' AND car_id LIKE 'AN%';")
    return _selection(sql_statement)


def query2(date):
    valid = check_date(date)
    if not valid:
        return False
    sql_statement = ("SELECT a, count(time)\n"
                     "FROM \n"
                     "(select 0 as a union values (0),(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12),(13),(14),"
                     "(15),(16),(17),(18),(19),(20),(21),(22),(23))\n"
                     "LEFT JOIN\n"
                     "(\n"
                     "    SELECT time(strftime('%s', datetime) - 60*strftime('%M', datetime), 'unixepoch') as time\n"
                     "    FROM charges\n"
                     "    WHERE date(datetime) LIKE ?\n"
                     ") ON a = CAST(strftime('%H', time) AS INTEGER)\n"
                     "GROUP BY a;")
    return _selection(sql_statement, (date,))


def query3():
    sql_statement = ("SELECT b, e, count(DISTINCT car_id)\n"
                     "FROM (select '07:00' as b, '10:00' as e "
                     "union values ('12:00', '14:00'), ('17:00', '19:00')), orders\n"
                     "WHERE \n"
                     "    --intersection\n"
                     "    CAST(strftime('%s', b) AS INTEGER) < CAST(strftime('%s', time(datetime)) AS INTEGER) "
                     "+ CAST(strftime('%s', duration) AS INTEGER) - CAST(strftime('%s', '00:00') AS INTEGER)\n"
                     "    AND CAST( strftime('%s', time(datetime)) as INTEGER) < CAST(strftime('%s', e) as INTEGER)\n"
                     "    --week constraint\n"
                     "    AND CAST(strftime('%s', datetime) AS INTEGER) "
                     "> CAST(strftime('%s', 'now', '-7 days') AS INTEGER)\n"
                     "GROUP BY b;")
    return _selection(sql_statement)


def query4(username):
    sql_statement = ("SELECT O.datetime, O.car_id\n"
                     "FROM orders O, payment P\n"
                     "WHERE O.car_id = P.car_id AND O.datetime = P.order_datetime AND O.username = P.username "
                     "and P.username = ?\n"
                     "GROUP by O.datetime, O.car_id\n"
                     "HAVING O.price != SUM(P.amount);")
    return _selection(sql_statement, (username,))


def query5(date):
    valid = check_date(date)
    if not valid:
        return False
    sql_statement = ("SELECT car_id, trav/c, strftime('%H:%M', sec/c, 'unixepoch')\n"
                     "FROM (\n"
                     "    SELECT car_id, sum(traveled_to_client) as trav, "
                     "sum(strftime('%s', duration)) as sec, count(*) as c\n"
                     "    FROM orders\n"
                     "    WHERE date(datetime) like ?\n"
                     "    GROUP BY car_id\n"
                     ");")
    return _selection(sql_statement, (date,))


def query6():
    sql_statement_1 = ("SELECT b, e, from_\n"
                       "FROM(\n"
                       "    SELECT b, e, from_, count(*) as c\n"
                       "    FROM (select ? as b, ? as e), orders\n"
                       "    WHERE\n"
                       "        CAST(strftime('%s', b) AS INTEGER) < CAST(strftime('%s', time(datetime)) AS INTEGER)\n"
                       "        AND CAST(strftime('%s', time(datetime)) as INTEGER) < CAST(strftime('%s', e) as INTEGER)\n"
                       "    GROUP BY from_\n"
                       "    UNION values(?, ?, null, 0)\n"
                       ")\n"
                       "ORDER BY c DESC LIMIT 1;")

    morning = _selection(sql_statement_1, ("07:00", "10:00", "07:00", "10:00"))
    afternoon = _selection(sql_statement_1, ("12:00", "14:00", "12:00", "14:00"))
    evening = _selection(sql_statement_1, ("17:00", "19:00", "17:00", "19:00"))
    _all = []
    _all.extend(morning)
    _all.extend(afternoon)
    _all.extend(evening)

    sql_statement_2 = ("SELECT b, e, to_\n"
                       "FROM(\n"
                       "    SELECT b, e, to_, count(*) as c\n"
                       "    FROM (select ? as b, ? as e), orders\n"
                       "    WHERE\n"
                       "        CAST(strftime('%s', b) AS INTEGER) < CAST(strftime('%s', time(datetime)) AS INTEGER)\n"
                       "        AND CAST(strftime('%s', time(datetime)) as INTEGER) < CAST(strftime('%s', e) as INTEGER)\n"
                       "    GROUP BY to_\n"
                       "    UNION values(?, ?, null, 0)\n"
                       ")\n"
                       "ORDER BY c DESC LIMIT 1;")

    morning = _selection(sql_statement_2, ("07:00", "10:00", "07:00", "10:00"))
    afternoon = _selection(sql_statement_2, ("12:00", "14:00", "12:00", "14:00"))
    evening = _selection(sql_statement_2, ("17:00", "19:00", "17:00", "19:00"))
    _all_2 = []
    _all_2.extend(morning)
    _all_2.extend(afternoon)
    _all_2.extend(evening)
    return _all, _all_2


def query7():
    sql_statement = ("SELECT C.car_id\n"
                     "FROM cars C\n"
                     "LEFT JOIN\n"
                     "(\n"
                     "    SELECT car_id\n"
                     "    FROM orders\n"
                     "    WHERE CAST(strftime('%s', datetime) AS INTEGER) > CAST(strftime('%s', 'now', '-3 months') AS INTEGER)\n"
                     ") as O ON C.car_id = O.car_id\n"
                     "GROUP BY C.car_id\n"
                     "ORDER BY count(O.car_id)\n"
                     "LIMIT ROUND(0.1*(\n"
                     "    SELECT COUNT(*) FROM cars\n"
                     "));")
    return _selection(sql_statement)


def query8():
    sql_statement = ("SELECT username, count(distinct C.datetime)\n"
                     "FROM orders O, charges C\n"
                     "WHERE date(O.datetime) = date(C.datetime)\n"
                     "GROUP BY username;")
    return _selection(sql_statement)


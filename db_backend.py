from dbcore import conn
import test_data

with open("creation.sql", "r") as f:
    creation_sql = f.read()


def create_tables():
    conn.executescript(creation_sql)
    conn.commit()


def _selection(sql_statement):
    cur = conn.cursor()
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
    sql_statement = "INSERT INTO CAR_TYPES (MODEL,PLUG_TYPE) VALUES (?, ?);"
    car_types = test_data.car_types()
    _insertion(sql_statement, car_types)

    sql_statement = "INSERT INTO CARS(CAR_ID, COLOR, MODEL) VALUES (?, ?, ?)"
    cars = [test_data.random_car() for i in range(20)]
    _insertion(sql_statement, cars)


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
                     "WHERE color LIKE 'red' AND car_id LIKE 'AN%';")
    return _selection(sql_statement)
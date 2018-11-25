from dbcore import conn

class FieldsError(Exception):
    pass


class DbValueError(Exception):
    pass


# class Field(object):
#     def __init__(self):
#         pass
#
#
# class VarcharField(Field):
#     pass
#
# class IntField(Field):

class Entity(object):
    _table_name = ""

    def _check_fields(self):
        if not (self._db_fields_types and isinstance(self._db_fields_types, dict)):
            raise FieldsError
        for field_type in self._db_fields_types.values():
            if field_type not in (int, str):
                raise FieldsError

    def _check_value_type(self, name, value):
        value_type = self._db_fields_types[name]
        if value_type == int:
            if type(value) != int:
                raise DbValueError
        if value_type == str:
            if type(value) != str:
                raise DbValueError

    def _check_values_init(self, values):
        for name in values.keys():
            if name not in self._db_fields_types.keys():
                raise DbValueError
            self._check_value_type(name, values[name])
        for name in self._db_fields_types.keys():
            if name not in values.keys():
                values[name] = None

    def check_values(self):
        pass

    def get_values(self):
        values = {}
        for name in self._db_fields_types.keys():
            values[name] = self.__dict__[name]
        return values

    def insert(self):
        cur = conn.cursor()
        _values = self.get_values()
        columns = _values.keys()
        values = [_values[c] for c in columns]
        sql_statement = "INSERT INTO {tname}({col}) VALUES ({ph})"\
            .format(tname=self._table_name, col=", ".join(columns), ph=", ".join(len(values)*"?"))
        cur.execute(sql_statement, values)
        cur.close()
        conn.commit()

    def __init__(self, values):
        self._db_fields_types = {k: v for k, v in self.__class__.__dict__.items() if not k.startswith("_")}
        # print({k: v for k, v in self.__class__.__dict__.items() if not k.startswith("_")})
        self._check_fields()
        self._check_values_init(values)
        self.__dict__.update(values)
        # self._values = values
        # print(self.__dict__)


# class Test(Entity):
#     # _db_fields_types = {
#     #         "id": ("number",),
#     #         "name": ("text",)
#     #     }
#     id = int
#     name = str


class CarParts(Entity):
    NAME = str
    _table_name = "CAR_PARTS"


class PartsProviders(Entity):
    ID = int
    ADRESS = str
    NAME = str
    PHONE = str
    _table_name = "PARTS_PROVIDERS"


class Workshops(Entity):
    WID = int
    GPS_LOCATION = str
    AVAILABILITY = str
    _table_name = "WORKSHOPS"


class CarTypes(Entity):
    MODEL = str
    PLUG_TYPE = str
    _table_name = "CAR_TYPES"


class Payment(Entity):
    USERNAME = str
    CAR_ID = str
    ORDER_DATETIME = str
    PAYMENT_DATETIME = str
    AMOUNT = int
    _table_name = "PAYMENT"


class Charges(Entity):
    UID = int
    CAR_ID = str
    DATETIME = str
    STATUS = str
    CHARGING_TIME = str
    _table_name = "CHARGES"


class Orders(Entity):
    USERNAME = str
    CAR_ID = str
    DATETIME = str
    FROM_ = str
    TO_ = str
    STATUS = str
    PRICE = int
    TRAVELED_TO_CLIENT = int
    DURATION = str
    _table_name = "ORDERS"


class Repairs(Entity):
    WID = int
    CAR_ID = str
    DATETIME = str
    STATUS = str
    PRICE = int
    _table_name = "REPAIRS"


class AvaibleParts(Entity):
    NAME = str
    WID = int
    _table_name = "AVAILABLE_PARTS"


class PartsFor(Entity):
    NAME = str
    MODEL = str
    _table_name = "PARTS_FOR"


class CanProvide(Entity):
    ID = int
    NAME = str
    _table_name = "CAN_PROVIDE"


class Sockets(Entity):
    UID = int
    PLUG_TYPE = str
    NUMBER = int
    _table_name = "SOCKETS"


class ChargingStations(Entity):
    UID = int
    GPS_LOCATION = str
    CHARGING_COST = str
    CHARGING_TIME = str
    _table_name = "CHARGING_STATIONS"


class Customers(Entity):
    USERNAME = str
    EMAIL = str
    PHONE = str
    FULL_NAME = str
    COUNTRY = str
    CITY = str
    ZIP_CODE = str
    _table_name = "CUSTOMERS"


class Cars(Entity):
    CAR_ID = str
    COLOR = str
    MODEL = str
    _table_name = "CARS"


def _selection(sql_statement):
    cur = conn.cursor()
    cur.execute(sql_statement)
    result = cur.fetchall()
    cur.close()
    return result


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


def can_provide_select():
    sql_statement = "select AP.WID, AP.NAME from AVAILABLE_PARTS AP;"
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
    sql_statement = "select CH.CAR_ID, CH.UID, CH.DATETIME, CH.CHARGING_TIME from CHARGES CH;"
    return _selection(sql_statement)


def parts_providers_select():
    sql_statement = "select P.ID, P.ADRESS, P.NAME, P.PHONE from PARTS_PROVIDERS P;"
    return _selection(sql_statement)


def payment_select():
    sql_statement = "select P.ORDER_DATETIME, P.PAYMENT_DATETIME, P.AMOUNT, P.USERNAME, P.CAR_ID from PAYMENT P;"
    return _selection(sql_statement)


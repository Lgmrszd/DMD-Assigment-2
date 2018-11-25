import sqlite3


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
        cur = self.__db_connection.cursor()
        _values = self.get_values()
        columns = _values.keys()
        values = [_values[c] for c in columns]
        sql_statement = "INSERT INTO {tname}({col}) VALUES ({ph})"\
            .format(tname=self._table_name, col=", ".join(columns), ph=", ".join(len(values)*"?"))
        cur.execute(sql_statement, values)
        cur.close()
        self.__db_connection.commit()

    def __init__(self, db_connection, values):
        assert isinstance(db_connection, sqlite3.Connection)
        self.__db_connection = db_connection
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
    ADDRESS = str
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


class Payments(Entity):
    USERNAME = str
    CAR_ID = str
    ORDER_DATETIME = str
    PAYMENT_DATETIME = str
    AMOUNT = int
    _table_name = "PAYMENTS"


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

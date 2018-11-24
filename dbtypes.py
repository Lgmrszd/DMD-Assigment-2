import sqlite3


class FieldsError(Exception):
    pass

class ValueError(Exception):
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
    _db_fields_types = {}
    _table_name = ""

    def _check_fields(self):
        if not (self._db_fields_types and isinstance(self._db_fields_types, dict)):
            raise FieldsError
        for field_type in self._db_fields_types.values():
            if field_type[0].lower() not in ("number", "varchar"):
                raise FieldsError
            if field_type[0] == "varchar":
                size = field_type[1]
                if type(size) != int or size < 1 or size > 255:
                    raise FieldsError

    def _check_value_type(self, name, value):
        value_type = self._db_fields_types[name]
        if value_type[0].lower() == "number":
            if type(value) != int:
                raise ValueError
        if value_type[0].lower() == "varchar":
            if type(value) != str:
                raise ValueError
            elif len(value) > value_type[1]:
                raise ValueError

    def _check_values(self, values):
        for name in values.keys():
            if name not in self._db_fields_types.keys():
                raise ValueError
            self._check_value_type(name, values[name])
        for name in self._db_fields_types.keys():
            if name not in values.keys():
                values[name] = None

    def get_values(self):
        return self._values.copy()

    def __init__(self, db_connection, values):
        self.__db_connection = db_connection
        self._check_fields()
        self._check_values(values)
        self._values = values


class Test(Entity):
    _db_fields_types = {
            "id": ("number",),
            "name": ("varchar", 6)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

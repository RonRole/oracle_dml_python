import cx_Oracle

class OracleDmlValueChanger:
    def __init__(self, column_type=None):
        self._column_type = column_type
    
    def handle(self, value):
        if(value is None):
            return f"''"
        if(self._column_type is cx_Oracle.DB_TYPE_NUMBER):
            return f'{value}'
        return f"'{value}'"

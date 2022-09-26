from functools import reduce

class OracleRecordList:
    def __init__(self, table_name, column_name_dml):
        self._table_name = table_name
        self._column_name_dml = column_name_dml
        self._oracle_record_list = []
    
    def append(self, column_name_value):
        new_item = OracleRecord(self._table_name, self._column_name_dml, column_name_value)
        self._oracle_record_list.append(new_item)
    
    def to_dml_list(self, replacements={}, excludes=[]):
        return list(map(lambda record: record.to_dml(replacements, excludes), self._oracle_record_list))

class OracleRecord:
    def __init__(self, table_name, column_name_dml, column_name_value):
        self._table_name = table_name
        self._column_name_dml = column_name_dml
        self._column_name_value = column_name_value
    
    def to_dml(self, replacements = {}, excludes = []):
        tmp_replacements = upper_key_dict(replacements)
        tmp_excludes = upper_list(excludes) 
        target_col_names = [colname for colname in self._column_name_dml.keys() if colname not in tmp_excludes]
        values = map(lambda colname: self._column_name_dml[colname].handle(tmp_replacements.get(colname, self._column_name_value[colname])), target_col_names)
        column_query = ",".join(target_col_names)
        values_query = ",".join(values)
        return f"INSERT INTO {self._table_name} ({column_query}) VALUES ({values_query})\n/\n"

def upper_key_dict(target):
    def add_dict(previous, key):
        previous.setdefault(key.upper(), target[key])
        return previous
    return reduce(add_dict, target, {})

def upper_list(target):
    return list(map(lambda item: item.upper(), target))
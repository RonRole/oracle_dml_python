import oracle_client
import cx_Oracle

# ColumnValue
column_value = oracle_client.ColumnValue(cx_Oracle.DB_TYPE_VARCHAR, 114)
column_value2 = oracle_client.ColumnValue(cx_Oracle.DB_TYPE_VARCHAR, 514)
column_value3 = oracle_client.ColumnValue(cx_Oracle.DB_TYPE_VARCHAR, 1919)
dict_record = oracle_client.DictRecord('SAWAI', {"KEI" : column_value, "KANDA" : column_value2, "KENGO" : column_value3})
print(dict_record.to_dml())
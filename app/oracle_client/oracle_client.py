import cx_Oracle
import oracle_client.dml_value_changer
import oracle_client.oracle_record

class OracleClient:
    def __init__(self, host, port, sid, username, password):
        self._tns = cx_Oracle.makedsn(host, port, sid)
        self._username = username
        self._password = password
    
    def change_connection_target(self, username, password):
        self._username = username
        self._password = password
        return self

    def get_dict_records(self, table_name, specify={}):
        with cx_Oracle.connect(self._username, self._password, self._tns) as conn:
            with conn.cursor() as cur:
                query = build_query(
                    table_name = table_name,
                    specify    = specify
                )
                cur.execute(query, specify)
                column_names = [d[0] for d in cur.description]
                column_types = [d[1] for d in cur.description]
                column_dmls = list(map(lambda column_type: oracle_client.dml_value_changer.OracleDmlValueChanger(column_type), column_types))
                column_name_dml = dict(zip(column_names, column_dmls))
                record_list = oracle_client.oracle_record.OracleRecordList(table_name, column_name_dml)
                rows = cur.fetchall()
                for row in rows:
                    column_name_value = dict(zip(column_names, row))
                    record_list.append(column_name_value)
                return record_list

def build_query(table_name, col_names = ['*'], specify = {}):
    return f'''
        SELECT
            {','.join(col_names)}
        FROM
            {table_name}
        WHERE
            {' AND '.join(['1=1'] + list(map(lambda key: f'{key}=:{key}', specify.keys())))}
    '''

from oracle_client import OracleClient
import dml_output
import settings

def handler(
    settings, 
    table_name, 
    specify = {}, 
    replacements = {},
    excludes = [],
    dml_output = dml_output.Standard()
): 
    client = OracleClient(
        host     = settings.host_ip,
        port     = settings.host_port,
        sid      = settings.sid,
        username = settings.username,
        password = settings.password
    )

    dict_records = client.get_dict_records(
        table_name = table_name,
        specify = specify
    )
    dml_list = dict_records.to_dml_list(
        replacements = replacements,
        excludes = excludes
    )
    dml_output.output(dml_list)
from handler import handler
import dml_output
import settings
import query

if __name__ == '__main__':
    json_settings = settings.loaders.JSON.load("settings.json")
    json_query = query.loaders.JSON.load('query.json')
    dml_output = dml_output.Sql('out')
    
    handler(
        settings = json_settings, 
        table_name = json_query.table_name,
        specify = json_query.specify,
        replacements = json_query.replacements,
        excludes = json_query.excludes,
        dml_output = dml_output
    )

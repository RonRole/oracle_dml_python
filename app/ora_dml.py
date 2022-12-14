from handler import handler
import dml_output
import settings
import query

if __name__ == '__main__':
    json_settings = settings.loaders.JSON.load("settings.json")
    json_queries = query.loaders.JSON.load('query.json')
    dml_output = dml_output.Sql('out')
    
    handler(
        settings = json_settings, 
        queries = json_queries,
        dml_output = dml_output
    )

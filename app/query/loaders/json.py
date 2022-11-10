import json
from ..query import Query

class JSON:
    def load(json_path):
        with open(json_path, 'r') as src:
            json_src = json.load(src)
            return list(map(lambda json_query: Query(
                table_name = json_query['table_name'],
                specify = json_query['specify'],
                replacements = json_query['replacements'],
                excludes = json_query['excludes'] 
            ), json_src['queries']))
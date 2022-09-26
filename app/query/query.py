class Query:
    def __init__(
        self,
        table_name,
        specify = {},
        replacements = {},
        excludes = []
    ):
        self.table_name = table_name
        self.specify = specify
        self.replacements = replacements
        self.excludes = excludes
import datetime

class Sql:
    def __init__(self, output_dir):
        self._output_dir = output_dir

    def output(self, dml_list):
        now = datetime.datetime.now()
        prefix = f'{now.strftime("%Y%m%d%H%M%S")}'
        file_path = f'{self._output_dir}/output_{prefix}.sql'
        with open(file_path, 'a') as f:
            for dml in dml_list:
                f.write(dml)
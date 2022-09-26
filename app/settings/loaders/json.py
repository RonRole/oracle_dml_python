import json
from ..settings import Settings

class JSON:
    def load(json_path):
        with open(json_path, 'r') as src:
            json_oracle_settings = json.load(src)["oracle"]
            return Settings(
                host_ip = json_oracle_settings["host_ip"],
                host_port = json_oracle_settings["host_port"],
                sid = json_oracle_settings["sid"],
                username = json_oracle_settings["username"],
                password = json_oracle_settings["password"],
            )
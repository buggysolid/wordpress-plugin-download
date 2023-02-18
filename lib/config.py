import tomllib
from pathlib import Path


def get():
    toml_config = None

    def __read_config():
        with open(Path("config/settings.toml"), 'rb') as config_file_handle:
            toml_config_ = tomllib.load(config_file_handle)
        return toml_config_

    if toml_config:
        return toml_config
    else:
        toml_config = __read_config()
        return toml_config

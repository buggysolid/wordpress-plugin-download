import logging
import toml
from pathlib import Path

toml_config = None
logger = logging.getLogger("wordpress-plugin-grep")


def get():
    def __read_config():
        with open(Path("config/settings.toml")) as config_file_handle:
            logger.debug("Opened config file. %s", config_file_handle)
            toml_config_ = toml.load(config_file_handle)
        return toml_config_

    global toml_config

    if toml_config is None:
        toml_config = __read_config()

    return toml_config

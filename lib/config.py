import logging
from pathlib import Path

import toml

toml_config = None
logger = logging.getLogger(__name__)


def get_config():
    def __read_config():
        with open(Path("config/settings.toml")) as config_file_handle:
            logger.debug("Opened config file. %s", config_file_handle)
            toml_config_ = toml.load(config_file_handle)
        return toml_config_

    global toml_config

    if toml_config is None:
        toml_config = __read_config()

    return toml_config

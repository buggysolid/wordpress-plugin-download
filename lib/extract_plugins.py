import logging
import zipfile
from pathlib import Path

from lib.config import get_config
from lib.paths import plugin_extraction_path

logger = logging.getLogger(f"wordpress-plugin-grep.{__name__}")


def extract_plugins():
    extraction_path = plugin_extraction_path()
    # this relationship may not always exist, but it does for now
    plugin_path = extraction_path.parent
    logger.info("Extracting plugins to %s", extraction_path)
    for zipfile_ in plugin_path.glob('**/*.zip'):
        if not zipfile.is_zipfile(zipfile_):
            logger.error("There are no zip files to extract.")
            break
        with zipfile.ZipFile(zipfile_) as plugin_zip:
            plugin_zip.extractall(path=extraction_path)

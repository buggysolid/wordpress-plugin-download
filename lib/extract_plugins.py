import logging
import zipfile
from pathlib import Path

from lib.config import get_config

logger = logging.getLogger(f"wordpress-plugin-grep.{__name__}")


def make_extraction_directory():
    config = get_config()
    download_directory = config.get('download').get('directory')
    extraction_directory = config.get('extraction').get('directory')
    extraction_path = Path(download_directory, extraction_directory)
    extraction_path.mkdir(parents=True, exist_ok=True)
    return extraction_path


def extract_plugins():
    extraction_path = make_extraction_directory()
    # this relationship may not always exist, but it does for now
    plugin_path = extraction_path.parent
    logger.info("Extracting plugins to %s", extraction_path)
    for zipfile_ in plugin_path.glob('**/*.zip'):
        if not zipfile.is_zipfile(zipfile_):
            logger.error("There are no zip files to extract.")
            break
        with zipfile.ZipFile(zipfile_) as plugin_zip:
            plugin_zip.extractall(path=extraction_path)

from lib.config import get_config
from pathlib import Path


def plugin_extraction_path():
    config = get_config()
    download_directory = config.get('download').get('directory')
    extraction_directory = config.get('extraction').get('directory')
    extraction_path = Path(download_directory, extraction_directory)
    extraction_path.mkdir(parents=True, exist_ok=True)
    return extraction_path


def plugin_download_path(plugin_name):
    config = get_config()
    plugin_directory = config.get('download').get('directory')
    plugin_path = Path(plugin_directory, plugin_name)
    plugin_path.parent.mkdir(exist_ok=True, parents=True)
    return plugin_path

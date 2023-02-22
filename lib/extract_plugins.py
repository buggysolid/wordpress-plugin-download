import logging
import zipfile

from lib.paths import plugin_extraction_path, has_plugin_been_extracted_already

logger = logging.getLogger(f"wordpress-plugin-grep.{__name__}")


def extract_plugins():
    extraction_path = plugin_extraction_path()
    # this relationship may not always exist, but it does for now
    plugin_path = extraction_path.parent
    logger.info("Extracting plugins to %s", extraction_path)
    for zipfile_ in plugin_path.glob('**/*.zip'):
        try:
            with zipfile.ZipFile(zipfile_) as plugin_zip:
                # First entry is always the directory the archive will extract to
                plugin_extraction_directory = plugin_zip.namelist()[0]
                # Someone might want to re-extract everything so this will likely need a flag in the future.
                if not has_plugin_been_extracted_already(plugin_extraction_directory):
                    plugin_zip.extractall(path=extraction_path)
                logger.info('Extracted %s to %s.', plugin_zip.filename, extraction_path)
        except zipfile.BadZipFile:
            logger.exception('Tried to extract invalid zip file.')

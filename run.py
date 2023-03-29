import argparse
import logging

from lib.download_plugins import get_plugins
from lib.extract_plugins import extract_plugins

argparse = argparse.ArgumentParser("wordpress-plugin-grep", "python run.py", "A program to use the "
                                                                             "WordPress plugin API to"
                                                                             " fetch plugins, "
                                                                             "download and extract "
                                                                             "them.")
group = argparse.add_mutually_exclusive_group()

group.add_argument("-d", "--download-only", action="store_true")
group.add_argument("-e", "--extract-existing", action="store_true")
group.add_argument("-f", "--full-run", action="store_true")

arguments = argparse.parse_args()

# this will go into its own logging module
logger = logging.getLogger(f"wordpress-plugin-grep")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('service.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

# Args are getting a bit unwildly.
if arguments.download_only:
    logger.info("Downloading plugins.")
    get_plugins()
elif arguments.extract_existing:
    logger.info("Extracting already downloaded plugins.")
    extract_plugins()
elif arguments.full_run:
    logger.info("Downloading plugins.")
    get_plugins()
    logger.info("Extracting plugins.")
    extract_plugins()

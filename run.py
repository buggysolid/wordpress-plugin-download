import argparse
import logging

from lib.download_plugins import get_plugins
from lib.extract_plugins import extract_plugins
from lib.find_functionality import check_plugins
from lib.report import write_report

argparse = argparse.ArgumentParser("wordpress-plugin-grep", "python run.py", "A program to use the "
                                                                             "WordPress plugin API to"
                                                                             " fetch plugins, "
                                                                             "download and extract "
                                                                             "them.")
group = argparse.add_mutually_exclusive_group()

group.add_argument("-d", "--download-only", action="store_true")
group.add_argument("-e", "--extract-existing", action="store_true")
group.add_argument("-c", "--check-existing", action="store_true")
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
elif arguments.check_existing:
    logger.info("Searching extracted plugins for features.")
    extract_plugins()
    features = check_plugins()
    logger.info("Writing report to report.txt.")
    write_report(features)
elif arguments.full_run:
    logger.info("Downloading plugins.")
    get_plugins()
    logger.info("Extracting plugins.")
    extract_plugins()
    logger.info("Searching for features in plugins.")
    features = check_plugins()
    logger.info("Writing report to report.txt.")
    write_report(features)
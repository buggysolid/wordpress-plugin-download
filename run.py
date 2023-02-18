import argparse
import logging

from lib.download_plugins import get_plugins

argparse = argparse.ArgumentParser("wordpress-plugin-grep", "python run.py --download-only", "A program to use the "
                                                                                             "WordPress plugin API to"
                                                                                             " fetch plugins, "
                                                                                             "download and extract "
                                                                                             "them.")
argparse.add_argument("-d", "--download-only", action="store_true", default=True)

arguments = argparse.parse_args()

# this will go into its own logging module
logger = logging.getLogger("wordpress-plugin-grep")
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

if arguments.download_only:
    logger.info("Downloading plugins.")
    get_plugins()

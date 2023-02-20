import logging

import requests

from lib.config import get_config
from lib.paths import plugin_download_path

logger = logging.getLogger(f"wordpress-plugin-grep.{__name__}")


def get_plugin_info(page=1):
    config = get_config()
    wordpress_api_hostname = config.get('api').get('hostname')
    wordpress_api_querystring = config.get('api').get('querystring')
    url = f"https://{wordpress_api_hostname}/{wordpress_api_querystring}{page}"
    logger.debug("Using URL. %s", url)
    try:
        request = requests.get(url)
    except requests.RequestException as failed_request:
        raise failed_request
    data = request.json()
    plugins = data['plugins']
    return plugins


def get_plugin_download_links():
    config = get_config()
    plugins_ = []
    page = 1
    logger.info("Getting plugins with >= %s active installs.", config.get('plugins').get('active_install'))
    # check the top plugin on each page to make sure we have not traversed too far.
    # .e.g. if I want only >= 200k active installs there is no point in going to page 500 of the results.
    while True:
        plugins = get_plugin_info(page)
        if plugins[0]['active_installs'] >= config.get('plugins').get('active_install'):
            for plugin in plugins:
                plugins_.append(plugin['download_link'])
            logger.info("Collected %d download links.", len(plugins_))
            page += 1
        else:
            break

    return plugins_


def download_plugins(plugins_to_download):
    logger.info("Downloading %d plugins.", len(plugins_to_download))
    for plugin in plugins_to_download:
        r = requests.get(plugin)
        plugin_name = plugin.split('/')[-1]
        plugin_path = plugin_download_path(plugin_name)
        logger.info("Writing plugin to %s", plugin_path)
        with open(plugin_path, 'wb') as plugin_file:
            plugin_file.write(r.content)


def get_plugins():
    plugins_to_download = get_plugin_download_links()
    download_plugins(plugins_to_download)

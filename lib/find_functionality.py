import logging
import re
from pathlib import Path

from lib.config import get_config
from lib.paths import plugin_extraction_path

logger = logging.getLogger(f"wordpress-plugin-grep.{__name__}")


def __build_plugin_feature_mapping_dict(plugin_names, regular_expression_patterns):
    plugin_features = dict()
    for plugin_name in plugin_names:
        plugin_features[plugin_name] = dict()
        for re_pattern in regular_expression_patterns:
            plugin_features[plugin_name][re_pattern.pattern.lower()] = 0
    return plugin_features


def check_plugins():
    config = get_config()
    regular_expression_patterns = [re.compile(re.escape(pattern), flags=re.MULTILINE | re.IGNORECASE) for pattern in config.get('checks').get('regular_expression_patterns')]
    extraction_path = plugin_extraction_path()

    plugin_names = [plugin_name.stem for plugin_name in extraction_path.glob("*")]

    plugin_features = __build_plugin_feature_mapping_dict(plugin_names, regular_expression_patterns)

    for plugin in plugin_names:
        plugin_dir = Path(extraction_path, plugin)
        for php_file in plugin_dir.glob("**/*.php"):
            if php_file.is_dir():
                continue
            with open(php_file) as php_file_handle:
                try:
                    data = php_file_handle.read()
                    for re_pattern in regular_expression_patterns:
                        match = re_pattern.search(data)
                        if match:
                            # case-insensitive keys for the dictionary
                            plugin_features[plugin][re_pattern.pattern.lower()] += 1
                except UnicodeDecodeError:
                    logger.warning("Failed to decode unicode symbol when reading file %s", php_file)

    def sort_by_inner_dictionary_value(plugin_name_to_features, sort_key_):
        # The second element of each tuple is a dictionary containing the tally of how many times
        # the regular expression patterns we searched for made a match.
        #
        # I want to be able to sort by an arbitrary feature that will come from the config while maintaining
        # the natural plugin_name to features mapping.
        #
        # Example argument: ('wordpress-seo', {'$wpdb->prepare': 17, 'nopriv': 0})
        return plugin_name_to_features[1][sort_key_]

    sort_key = config.get('report').get('sort_key').lower()
    # maybe destroy the original dictionary to save some memory?
    return sorted(plugin_features.items(), key=lambda x: sort_by_inner_dictionary_value(x, sort_key_=sort_key),
                  reverse=True)

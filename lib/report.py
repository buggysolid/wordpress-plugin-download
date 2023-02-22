import logging

logger = logging.getLogger(f"wordpress-plugin-grep.{__name__}")


def write_report(features):
    with open('report.txt', 'w') as report_file_handle:
        report_file_handle.writelines("Plugin name->Features\n")
        for plugin in features:
            # I can probably get this into a JSON like document and dump it that way.
            # The client should not have to be aware of the data layout.
            plugin_name = plugin[0]
            plugin_features = plugin[1]
            features_str = f"{plugin_name}->{plugin_features}\n"
            report_file_handle.writelines(features_str)
        logger.info("Report written.")

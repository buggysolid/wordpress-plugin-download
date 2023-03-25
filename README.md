# wordpress-plugin-grep
Download, extract and search wordpress plugins that match an active install threshold for specific strings.

# Why?

I needed to audit wordpress plugins that had >= 200k active installations. I was manually checking plugins as a start so
I ended up writing this little client to collect, extract and search wordpress plugins for specific functionality.

The wordpress website has an SVN repo with all the plugins so you could just checkout the entire SVN repo but it is very slow.

It is much faster to download the zipped plugin artifacts.

# How to use?

Edit the config/settings.toml file and specify how many active_installs a plugin should have to download it.

```
python -m venv wordpress-plugin-grep
source wordpress-plugin-grep/bin/activate
pip install -r requirements.txt
python run.py -h
```

# Usage

```
usage: python run.py

A program to use the WordPress plugin API to fetch plugins, download and extract them.

options:
  -h, --help            show this help message and exit
  -d, --download-only
  -e, --extract-existing
  -f, --full-run
```

After the script has executed you will have a bunch of zipped wordpress plugins in the data/ folder.

## Download plugins with >= 4M active installs.

```
python run.py -d
2023-03-25 16:57:30,354 - wordpress-plugin-grep - INFO - Downloading plugins.
2023-03-25 16:57:30,355 - wordpress-plugin-grep.lib.download_plugins - INFO - Getting plugins with >= 4000000 active installs.
2023-03-25 16:57:31,811 - wordpress-plugin-grep.lib.download_plugins - INFO - Collected 24 download links.
2023-03-25 16:57:33,233 - wordpress-plugin-grep.lib.download_plugins - INFO - Downloading 24 plugins.
2023-03-25 16:57:34,214 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/contact-form-7.5.7.5.1.zip
2023-03-25 16:57:35,882 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wordpress-seo.20.3.zip
2023-03-25 16:57:37,526 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/elementor.3.11.5.zip
2023-03-25 16:57:38,159 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/classic-editor.1.6.2.zip
2023-03-25 16:57:38,951 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/akismet.5.1.zip
2023-03-25 16:57:40,697 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/woocommerce.7.5.1.zip
2023-03-25 16:57:42,203 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wpforms-lite.1.8.0.2.zip
2023-03-25 16:57:43,387 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/really-simple-ssl.6.2.2.zip
2023-03-25 16:57:45,693 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/jetpack.11.9.1.zip
2023-03-25 16:57:47,004 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/all-in-one-wp-migration.7.72.zip
2023-03-25 16:57:48,563 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wordfence.7.9.1.zip
2023-03-25 16:57:49,532 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/duplicate-post.4.5.zip
2023-03-25 16:57:50,740 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/litespeed-cache.5.3.3.zip
2023-03-25 16:57:51,354 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wordpress-importer.0.8.zip
2023-03-25 16:57:54,108 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/updraftplus.1.23.3.zip
2023-03-25 16:57:56,134 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/google-analytics-for-wordpress.8.13.1.zip
2023-03-25 16:57:57,619 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/all-in-one-seo-pack.4.3.3.zip
2023-03-25 16:57:59,050 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wp-mail-smtp.3.7.0.zip
2023-03-25 16:58:00,451 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/google-site-kit.1.96.0.zip
2023-03-25 16:58:01,166 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/duplicate-page.zip
2023-03-25 16:58:02,511 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/tinymce-advanced.5.6.0.zip
2023-03-25 16:58:04,023 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/redirection.5.3.9.zip
2023-03-25 16:58:05,117 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/mailchimp-for-wp.4.9.2.zip
2023-03-25 16:58:06,289 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/limit-login-attempts-reloaded.2.25.13.zip
```

# Check downloaded plugins.

```
python run.py -c
2023-03-25 16:59:13,726 - wordpress-plugin-grep - INFO - Searching extracted plugins for features.
2023-03-25 16:59:13,726 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracting plugins to data/extracted_plugins
2023-03-25 16:59:13,742 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/classic-editor.1.6.2.zip to data/extracted_plugins.
2023-03-25 16:59:13,847 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/all-in-one-seo-pack.4.3.3.zip to data/extracted_plugins.
2023-03-25 16:59:13,875 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/really-simple-ssl.6.2.2.zip to data/extracted_plugins.
2023-03-25 16:59:13,992 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordpress-seo.20.3.zip to data/extracted_plugins.
2023-03-25 16:59:13,993 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/duplicate-page.zip to data/extracted_plugins.
2023-03-25 16:59:14,004 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/contact-form-7.5.7.5.1.zip to data/extracted_plugins.
2023-03-25 16:59:14,022 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/all-in-one-wp-migration.7.72.zip to data/extracted_plugins.
2023-03-25 16:59:14,042 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/limit-login-attempts-reloaded.2.25.13.zip to data/extracted_plugins.
2023-03-25 16:59:14,140 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordfence.7.9.1.zip to data/extracted_plugins.
2023-03-25 16:59:14,143 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/akismet.5.1.zip to data/extracted_plugins.
2023-03-25 16:59:14,144 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordpress-importer.0.8.zip to data/extracted_plugins.
2023-03-25 16:59:14,300 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/updraftplus.1.23.3.zip to data/extracted_plugins.
2023-03-25 16:59:14,314 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/mailchimp-for-wp.4.9.2.zip to data/extracted_plugins.
2023-03-25 16:59:14,350 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/redirection.5.3.9.zip to data/extracted_plugins.
2023-03-25 16:59:14,493 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/elementor.3.11.5.zip to data/extracted_plugins.
2023-03-25 16:59:14,600 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wpforms-lite.1.8.0.2.zip to data/extracted_plugins.
2023-03-25 16:59:14,889 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/jetpack.11.9.1.zip to data/extracted_plugins.
2023-03-25 16:59:14,917 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/litespeed-cache.5.3.3.zip to data/extracted_plugins.
2023-03-25 16:59:14,982 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/google-analytics-for-wordpress.8.13.1.zip to data/extracted_plugins.
2023-03-25 16:59:15,084 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/google-site-kit.1.96.0.zip to data/extracted_plugins.
2023-03-25 16:59:15,188 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wp-mail-smtp.3.7.0.zip to data/extracted_plugins.
2023-03-25 16:59:15,576 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/woocommerce.7.5.1.zip to data/extracted_plugins.
2023-03-25 16:59:15,581 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/duplicate-post.4.5.zip to data/extracted_plugins.
2023-03-25 16:59:15,588 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/tinymce-advanced.5.6.0.zip to data/extracted_plugins.
2023-03-25 16:59:18,766 - wordpress-plugin-grep - INFO - Writing report to report.txt.
2023-03-25 16:59:18,766 - wordpress-plugin-grep.lib.report - INFO - Report written.
```

# Report output

```
cat report.txt 
Plugin name->Features
jetpack->{'\\$wpdb\\->prepare': 47, 'nopriv': 7, 'add_action': 410, 'add_filter': 285, 'wp_rest_request': 59, 'esc_url_raw': 91, 'sanitize_url': 3}
woocommerce->{'\\$wpdb\\->prepare': 124, 'nopriv': 3, 'add_action': 308, 'add_filter': 189, 'wp_rest_request': 179, 'esc_url_raw': 54, 'sanitize_url': 0}
wpforms-lite->{'\\$wpdb\\->prepare': 16, 'nopriv': 4, 'add_action': 133, 'add_filter': 71, 'wp_rest_request': 0, 'esc_url_raw': 18, 'sanitize_url': 0}
wordpress-seo->{'\\$wpdb\\->prepare': 17, 'nopriv': 0, 'add_action': 137, 'add_filter': 77, 'wp_rest_request': 13, 'esc_url_raw': 9, 'sanitize_url': 10}
all-in-one-seo-pack->{'\\$wpdb\\->prepare': 6, 'nopriv': 2, 'add_action': 88, 'add_filter': 26, 'wp_rest_request': 17, 'esc_url_raw': 9, 'sanitize_url': 0}
wp-mail-smtp->{'\\$wpdb\\->prepare': 12, 'nopriv': 2, 'add_action': 50, 'add_filter': 17, 'wp_rest_request': 0, 'esc_url_raw': 6, 'sanitize_url': 1}
google-site-kit->{'\\$wpdb\\->prepare': 4, 'nopriv': 0, 'add_action': 40, 'add_filter': 48, 'wp_rest_request': 16, 'esc_url_raw': 6, 'sanitize_url': 0}
really-simple-ssl->{'\\$wpdb\\->prepare': 1, 'nopriv': 0, 'add_action': 29, 'add_filter': 30, 'wp_rest_request': 5, 'esc_url_raw': 5, 'sanitize_url': 0}
akismet->{'\\$wpdb\\->prepare': 2, 'nopriv': 0, 'add_action': 4, 'add_filter': 2, 'wp_rest_request': 1, 'esc_url_raw': 2, 'sanitize_url': 0}
redirection->{'\\$wpdb\\->prepare': 9, 'nopriv': 0, 'add_action': 7, 'add_filter': 7, 'wp_rest_request': 9, 'esc_url_raw': 2, 'sanitize_url': 11}
elementor->{'\\$wpdb\\->prepare': 7, 'nopriv': 1, 'add_action': 90, 'add_filter': 49, 'wp_rest_request': 8, 'esc_url_raw': 2, 'sanitize_url': 0}
google-analytics-for-wordpress->{'\\$wpdb\\->prepare': 0, 'nopriv': 4, 'add_action': 44, 'add_filter': 18, 'wp_rest_request': 0, 'esc_url_raw': 2, 'sanitize_url': 0}
wordfence->{'\\$wpdb\\->prepare': 17, 'nopriv': 2, 'add_action': 13, 'add_filter': 8, 'wp_rest_request': 4, 'esc_url_raw': 1, 'sanitize_url': 0}
duplicate-page->{'\\$wpdb\\->prepare': 0, 'nopriv': 0, 'add_action': 1, 'add_filter': 1, 'wp_rest_request': 0, 'esc_url_raw': 1, 'sanitize_url': 0}
litespeed-cache->{'\\$wpdb\\->prepare': 6, 'nopriv': 0, 'add_action': 38, 'add_filter': 39, 'wp_rest_request': 1, 'esc_url_raw': 0, 'sanitize_url': 0}
updraftplus->{'\\$wpdb\\->prepare': 14, 'nopriv': 2, 'add_action': 25, 'add_filter': 18, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
wordpress-importer->{'\\$wpdb\\->prepare': 1, 'nopriv': 0, 'add_action': 1, 'add_filter': 1, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
limit-login-attempts-reloaded->{'\\$wpdb\\->prepare': 1, 'nopriv': 1, 'add_action': 1, 'add_filter': 1, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
tinymce-advanced->{'\\$wpdb\\->prepare': 0, 'nopriv': 0, 'add_action': 1, 'add_filter': 1, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
classic-editor->{'\\$wpdb\\->prepare': 0, 'nopriv': 0, 'add_action': 1, 'add_filter': 1, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
all-in-one-wp-migration->{'\\$wpdb\\->prepare': 0, 'nopriv': 1, 'add_action': 1, 'add_filter': 1, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
contact-form-7->{'\\$wpdb\\->prepare': 2, 'nopriv': 0, 'add_action': 39, 'add_filter': 21, 'wp_rest_request': 1, 'esc_url_raw': 0, 'sanitize_url': 9}
mailchimp-for-wp->{'\\$wpdb\\->prepare': 0, 'nopriv': 0, 'add_action': 37, 'add_filter': 18, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
duplicate-post->{'\\$wpdb\\->prepare': 0, 'nopriv': 0, 'add_action': 23, 'add_filter': 15, 'wp_rest_request': 0, 'esc_url_raw': 0, 'sanitize_url': 0}
```
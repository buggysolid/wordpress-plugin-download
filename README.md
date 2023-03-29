# wordpress-plugin-grep
Download and extract wordpress plugins that match an active install threshold.

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

## Download plugins and extract them.

```
(venv-test) cs@host:~/PycharmProjects/wordpress-plugin-grep$ python run.py -f
2023-03-29 16:34:38,631 - wordpress-plugin-grep - INFO - Downloading plugins.
2023-03-29 16:34:38,631 - wordpress-plugin-grep.lib.download_plugins - INFO - Getting plugins with >= 4000000 active installs.
2023-03-29 16:34:39,397 - wordpress-plugin-grep.lib.download_plugins - INFO - Collected 24 download links.
2023-03-29 16:34:40,697 - wordpress-plugin-grep.lib.download_plugins - INFO - Downloading 24 plugins.
2023-03-29 16:34:41,712 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/contact-form-7.5.7.5.1.zip
2023-03-29 16:34:44,015 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wordpress-seo.20.4.zip
2023-03-29 16:34:46,164 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/elementor.3.12.0.zip
2023-03-29 16:34:46,744 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/classic-editor.1.6.2.zip
2023-03-29 16:34:47,482 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/akismet.5.1.zip
2023-03-29 16:34:49,918 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/woocommerce.7.5.1.zip
2023-03-29 16:34:52,485 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wpforms-lite.1.8.0.2.zip
2023-03-29 16:34:54,254 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/really-simple-ssl.6.2.3.zip
2023-03-29 16:34:56,916 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/jetpack.11.9.1.zip
2023-03-29 16:34:58,349 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/all-in-one-wp-migration.7.73.zip
2023-03-29 16:35:00,033 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wordfence.7.9.2.zip
2023-03-29 16:35:00,843 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/duplicate-post.4.5.zip
2023-03-29 16:35:02,423 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/litespeed-cache.5.3.3.zip
2023-03-29 16:35:03,132 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wordpress-importer.0.8.zip
2023-03-29 16:35:04,776 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/updraftplus.1.23.3.zip
2023-03-29 16:35:06,768 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/google-analytics-for-wordpress.8.14.0.zip
2023-03-29 16:35:16,758 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/all-in-one-seo-pack.4.3.3.zip
2023-03-29 16:35:18,662 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/wp-mail-smtp.3.7.0.zip
2023-03-29 16:35:20,727 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/google-site-kit.1.96.0.zip
2023-03-29 16:35:21,385 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/duplicate-page.zip
2023-03-29 16:35:22,984 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/tinymce-advanced.5.6.0.zip
2023-03-29 16:35:24,649 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/redirection.5.3.9.zip
2023-03-29 16:35:25,651 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/mailchimp-for-wp.4.9.2.zip
2023-03-29 16:35:26,988 - wordpress-plugin-grep.lib.download_plugins - INFO - Writing plugin to data/limit-login-attempts-reloaded.2.25.13.zip
2023-03-29 16:35:26,989 - wordpress-plugin-grep - INFO - Extracting plugins.
2023-03-29 16:35:26,989 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracting plugins to data/extracted_plugins
2023-03-29 16:35:26,990 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/classic-editor.1.6.2.zip to data/extracted_plugins.
2023-03-29 16:35:26,993 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/all-in-one-seo-pack.4.3.3.zip to data/extracted_plugins.
2023-03-29 16:35:26,993 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/duplicate-page.zip to data/extracted_plugins.
2023-03-29 16:35:26,994 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/contact-form-7.5.7.5.1.zip to data/extracted_plugins.
2023-03-29 16:35:26,995 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/limit-login-attempts-reloaded.2.25.13.zip to data/extracted_plugins.
2023-03-29 16:35:26,995 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/akismet.5.1.zip to data/extracted_plugins.
2023-03-29 16:35:26,996 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/all-in-one-wp-migration.7.73.zip to data/extracted_plugins.
2023-03-29 16:35:27,001 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordpress-seo.20.4.zip to data/extracted_plugins.
2023-03-29 16:35:27,001 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordpress-importer.0.8.zip to data/extracted_plugins.
2023-03-29 16:35:27,006 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/updraftplus.1.23.3.zip to data/extracted_plugins.
2023-03-29 16:35:27,007 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/mailchimp-for-wp.4.9.2.zip to data/extracted_plugins.
2023-03-29 16:35:27,007 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/redirection.5.3.9.zip to data/extracted_plugins.
2023-03-29 16:35:27,010 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordfence.7.9.2.zip to data/extracted_plugins.
2023-03-29 16:35:27,013 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wpforms-lite.1.8.0.2.zip to data/extracted_plugins.
2023-03-29 16:35:27,023 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/jetpack.11.9.1.zip to data/extracted_plugins.
2023-03-29 16:35:27,025 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/litespeed-cache.5.3.3.zip to data/extracted_plugins.
2023-03-29 16:35:27,026 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/really-simple-ssl.6.2.3.zip to data/extracted_plugins.
2023-03-29 16:35:27,031 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/google-site-kit.1.96.0.zip to data/extracted_plugins.
2023-03-29 16:35:27,032 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/google-analytics-for-wordpress.8.14.0.zip to data/extracted_plugins.
2023-03-29 16:35:27,037 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wp-mail-smtp.3.7.0.zip to data/extracted_plugins.
2023-03-29 16:35:27,041 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/elementor.3.12.0.zip to data/extracted_plugins.
2023-03-29 16:35:27,058 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/woocommerce.7.5.1.zip to data/extracted_plugins.
2023-03-29 16:35:27,058 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/duplicate-post.4.5.zip to data/extracted_plugins.
2023-03-29 16:35:27,059 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/tinymce-advanced.5.6.0.zip to data/extracted_plugins.
```

## Download plugins with >= 4M active installs.

```
(venv-test) cs@host:~/PycharmProjects/wordpress-plugin-grep$ python run.py -d
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

# Extract plugins

```
(venv-test) cs@host:~/PycharmProjects/wordpress-plugin-grep$ python run.py -e
2023-03-29 16:33:25,106 - wordpress-plugin-grep - INFO - Extracting already downloaded plugins.
2023-03-29 16:33:25,107 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracting plugins to data/extracted_plugins
2023-03-29 16:33:25,108 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/classic-editor.1.6.2.zip to data/extracted_plugins.
2023-03-29 16:33:25,212 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/all-in-one-seo-pack.4.3.3.zip to data/extracted_plugins.
2023-03-29 16:33:25,213 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/duplicate-page.zip to data/extracted_plugins.
2023-03-29 16:33:25,223 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/contact-form-7.5.7.5.1.zip to data/extracted_plugins.
2023-03-29 16:33:25,242 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/limit-login-attempts-reloaded.2.25.13.zip to data/extracted_plugins.
2023-03-29 16:33:25,244 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/akismet.5.1.zip to data/extracted_plugins.
2023-03-29 16:33:25,262 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/all-in-one-wp-migration.7.73.zip to data/extracted_plugins.
2023-03-29 16:33:25,373 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordpress-seo.20.4.zip to data/extracted_plugins.
2023-03-29 16:33:25,374 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordpress-importer.0.8.zip to data/extracted_plugins.
2023-03-29 16:33:25,523 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/updraftplus.1.23.3.zip to data/extracted_plugins.
2023-03-29 16:33:25,537 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/mailchimp-for-wp.4.9.2.zip to data/extracted_plugins.
2023-03-29 16:33:25,572 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/redirection.5.3.9.zip to data/extracted_plugins.
2023-03-29 16:33:25,665 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wordfence.7.9.2.zip to data/extracted_plugins.
2023-03-29 16:33:25,768 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wpforms-lite.1.8.0.2.zip to data/extracted_plugins.
2023-03-29 16:33:26,047 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/jetpack.11.9.1.zip to data/extracted_plugins.
2023-03-29 16:33:26,075 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/litespeed-cache.5.3.3.zip to data/extracted_plugins.
2023-03-29 16:33:26,104 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/really-simple-ssl.6.2.3.zip to data/extracted_plugins.
2023-03-29 16:33:26,203 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/google-site-kit.1.96.0.zip to data/extracted_plugins.
2023-03-29 16:33:26,280 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/google-analytics-for-wordpress.8.14.0.zip to data/extracted_plugins.
2023-03-29 16:33:26,380 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/wp-mail-smtp.3.7.0.zip to data/extracted_plugins.
2023-03-29 16:33:26,530 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/elementor.3.12.0.zip to data/extracted_plugins.
2023-03-29 16:33:26,879 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/woocommerce.7.5.1.zip to data/extracted_plugins.
2023-03-29 16:33:26,885 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/duplicate-post.4.5.zip to data/extracted_plugins.
2023-03-29 16:33:26,892 - wordpress-plugin-grep.lib.extract_plugins - INFO - Extracted data/tinymce-advanced.5.6.0.zip to data/extracted_plugins.
```

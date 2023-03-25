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
```

```
ls data
akismet.5.0.2.zip                 duplicate-page.zip                         google-site-kit.1.96.0.zip                 really-simple-ssl.6.2.2.zip  wordfence.7.9.1.zip
all-in-one-seo-pack.4.3.3.zip     duplicate-post.4.5.zip                     jetpack.11.9.zip                           redirection.5.3.9.zip        wordpress-importer.0.8.zip
all-in-one-wp-migration.7.72.zip  elementor.3.11.5.zip                       limit-login-attempts-reloaded.2.25.13.zip  tinymce-advanced.5.6.0.zip   wordpress-seo.20.3.zip
classic-editor.1.6.2.zip          extracted_plugins                          litespeed-cache.5.3.3.zip                  updraftplus.1.23.3.zip       wpforms-lite.1.8.0.2.zip
contact-form-7.5.7.4.zip          google-analytics-for-wordpress.8.13.1.zip  mailchimp-for-wp.4.9.1.zip                 woocommerce.7.5.0.zip        wp-mail-smtp.3.7.0.zip
```
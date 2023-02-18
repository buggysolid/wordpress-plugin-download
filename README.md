# wordpress-plugin-grep
Download and extract wordpress plugins grepping their contents for specific strings.

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
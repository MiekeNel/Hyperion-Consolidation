# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'mySite'
copyright = '2023, Mieke Nel'
author = 'Mieke Nel'
release = '1.0.0'

import os
import sys
import django

# Add the parent directory of your Django project to the sys.path.
sys.path.insert(0, os.path.abspath('..'))

# Set the DJANGO_SETTINGS_MODULE to your Django project's settings.
os.environ['DJANGO_SETTINGS_MODULE'] = 'mySite.settings'

# Initialize Django to work with autodoc.
django.setup()

# -- General configuration ---------------------------------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'TrueLearn'
# pylint: disable=redefined-builtin
copyright = '2023, KD-7,sahanbull,yuxqiu,deniselezi,aaneelshalman'
author = 'KD-7,sahanbull,yuxqiu,deniselezi,aaneelshalman'

# pylint: disable=wrong-import-position
import truelearn

version = truelearn.__version__
release = truelearn.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Install autoapi with pip install sphinx-autoapi
extensions = ['sphinx.ext.viewcode','autoapi.extension']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for autoapi extension -------------------------------------------
autoapi_dirs = ['../truelearn']
autoapi_options = ['members', 'show-inheritance']
autoapi_type = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Install furo theme with pip install furo
html_theme = 'furo'
html_static_path = ['_static']

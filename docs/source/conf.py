# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import glob
import sphinx_rtd_theme

# Add swspy path:
sys.path.insert(0, os.path.abspath(os.path.join("..","..")))


# -- Project information -----------------------------------------------------

project = 'swspy'
copyright = '2021, Tom S Hudson'
author = 'Tom S Hudson'

# The full version:
# from swspy import __version__ 
# release = __version__
release = "1.0.3"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    'sphinx.ext.autosummary',
]

# Specify master doc:
master_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Automatically generate submodule docs:
autosummary_generate = glob.glob("submodules" + os.sep + "*.rst")

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add a logo:
html_logo = os.path.join("images", "swspy_logo.png")
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

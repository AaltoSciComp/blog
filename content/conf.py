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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

blog_baseurl = 'https://aaltoscicomp.github.io/blog/'
blog_feed_fulltext = True
post_date_format = '%Y %b %d'
blog_feed_length = 50
html_sidebars = {
   '**': [#'postcard.html',
          'recentposts.html',
          #'tagcloud.html',
          #'categories.html',
          'archives.html', ]
}


# -- Project information -----------------------------------------------------

project = 'Aalto Scientific Computing Blog'
copyright = '2021, Aalto Scientific Computing'
author = 'Aalto Scientific Computing'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'ablog',
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'sphinx_rtd_theme_ext_color_contrast',
    ]

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
html_theme = 'alabaster'#sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

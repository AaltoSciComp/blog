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

blog_title = "Aalto Scientific Computing Blog"
blog_baseurl = 'https://aaltoscicomp.github.io/blog/'
#blog_path = '.'
blog_feed_fulltext = True
post_date_format = '%Y %b %d'
blog_feed_length = 50
post_auto_excerpt = 1000 # number of paragraphs in excerpt, overrideable.
html_sidebars = {
   '**': ['asc.html',
          'ablog/postcard.html',
          'ablog/recentposts.html',
          'ablog/tagcloud.html',
          'ablog/categories.html',
          'ablog/archives.html', ]
}


# -- Project information -----------------------------------------------------

project = 'Aalto Scientific Computing Blog'
copyright = '2021-2023, Aalto Scientific Computing'
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
    'sphinx_aaltoscicomp_branding',
    'sphinxext.opengraph',
    'sphinx_togglebutton',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


ogp_site_url = "https://aaltoscicomp.github.io/blog/"
ogp_site_name = "Aalto SciComp Blog"
ogp_image = "https://scicomp.aalto.fi/_static/asc-socialshare-02.png"
ogp_image_alt = "ASC hexagon logo; Aalto Scientific Computing; Data, Software, Computing, HPC, and Training."
ogp_custom_meta_tags = ['<meta property="twitter:creator" content="@SciCompAalto" />']


import os
if (
    'GITHUB_ACTION' in os.environ
    and os.environ.get('GITHUB_REPOSITORY', '').lower() == 'aaltoscicomp/blog'
    and os.environ.get('GITHUB_REF') == 'refs/heads/main'
    ):
    html_js_files = [
        ('https://plausible.cs.aalto.fi/js/script.js', {"data-domain": "aaltoscicomp.github.io", "defer": "defer"}),
    ]


intersphinx_mapping = {
    'scicomp': ('https://scicomp.aalto.fi/', None),
    }
# Note: for docs, use :external:doc`rse/index`.  Use :external: and do NOT use leading `/`.
    #intersphinx_disabled_reftypes = []

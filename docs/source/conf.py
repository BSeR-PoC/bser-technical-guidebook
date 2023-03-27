# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BSeR Technical Guidebook'
copyright = '2023, GTRI'
author = 'GTRI'

version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_immaterial'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_static_path = ["_static"]
html_theme = 'sphinx_immaterial'
html_title = 'BSeR Technical Guidebook'
html_logo = "_static/site-logo.svg"

html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://bsertechguide.readthedocs.io/",
    "repo_url": "https://github.com/BSeR-PoC/bser-technical-guidebook/",
    "repo_name": "bser-technical-guidebook",
    "repo_type": "github",
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ]
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

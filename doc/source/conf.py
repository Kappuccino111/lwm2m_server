# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import re
import subprocess

sys.path.insert(0, os.path.abspath('../../src/'))  
master_doc = "index"

project = 'Flow Nexus'
copyright = '2024, Jonas Remmert, Akarshan Kapoor'
author = 'Jonas Remmert, Akarshan Kapoor'

try:
    version = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()
except subprocess.CalledProcessError:
    version = "0.1"  
release = version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  
    'sphinxcontrib.plantuml',  
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages', 
    'sphinxcontrib.newsfeed',
]

templates_path = ['_templates']

exclude_patterns = []

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_logo = '_static/logo_sidebar.png'

html_theme_options = {
    'repository_url': 'https://github.com/jonas-rem/lwm2m_server',
    'repository_branch': 'main',
    'path_to_docs': 'docs/source/',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
    'use_download_button': True,
    'show_navbar_depth': 100,
    'home_page_in_toc': True,
    'navigation_with_keys': False,
    "announcement": "🚧 This repository is currently in active development. Some features may not be fully functional or may change significantly.🚧",

}

html_context = {
    "display_github": True,  
    "github_user": "jonas-rem",  
    "github_repo": "lwm2m_server",  
    "github_version": "main", 
    "conf_py_path": "/docs/source/",  
}

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage{microtype}
        \setcounter{tocdepth}{2}
        \usepackage{tocbibind} % Adds LoT and LoF to the ToC
    ''',
}

latex_documents = [
    (master_doc, f'flow_nexus_{version}.tex', 'Flow Nexus Documentation',
     'Jonas Remmert, Akarshan Kapoor', 'manual'),
]

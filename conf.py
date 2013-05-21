# -*- coding: utf-8 -*-
import sys, os

language = 'en'

master_doc = 'index'
if language == 'ja':
    project = u'ドキュメントジェネレータ Sphinx'
else:
    project = u'Introduction to Sphinx documentation generator'
copyright = u'2013, Takayuki SHIMIZUKAWA'
version = release = '1.0'
exclude_patterns = ['_build']
locale_dirs = ['locale']
pygments_style = 'sphinx'
extensions = [
    'sphinxjp.themecore',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.blockdiag',
]
html_logo = 'sphinx-logo.png'
html_static_path = ['_static']
html_use_index = False
html_theme = 's6'

# for intersphinx
if language != 'ja':
    intersphinx_mapping = {
       'sphinx': ('http://sphinx-doc.org/', None),
       'py': ('http://docs.python.org/2/', None),
       'blockdiag': ('http://blockdiag.com/en/', None),
    }
else:
    intersphinx_mapping = {
       'sphinx': ('http://docs.sphinx-users.jp/', None),
       'py': ('http://docs.python.jp/2/', None),
       'blockdiag': ('http://blockdiag.com/ja/', None),
    }


def setup(app):
    app.add_stylesheet('custom.css')


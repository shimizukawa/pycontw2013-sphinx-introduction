# -*- coding: utf-8 -*-
import sys, os

language = 'ja'

source_suffix = '.rst'
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
extensions = ['sphinxjp.themecore']
html_logo = 'sphinx-logo.png'
html_static_path = ['_static']
html_use_index = False
html_theme = 's6'


def setup(app):
    app.add_stylesheet('custom.css')


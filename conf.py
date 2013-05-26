# -*- coding: utf-8 -*-
import sys, os
sys.path.append('.')
sys.path.append('_ext')

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
    'sphinx.ext.autodoc',
    'sphinx.ext.pngmath',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'demo',
]
todo_include_todos = True
html_logo = 'images/sphinx-logo.png'
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


# -- directive/role definition ------------------------------------------------>

from docutils.parsers.rst.directives.admonitions import Admonition
from sphinx.util.compat import make_admonition


class SpeechDirective(Admonition):
    css_class = 'speech'
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        title = u'[speech]'
        if self.arguments:
            title += self.arguments[0]

        if 'class' in self.options:
            self.options['class'].append(self.css_class)
        else:
            self.options['class'] = [self.css_class]

        ret = make_admonition(
            self.node_class, self.name, [title], self.options,
            self.content, self.lineno, self.content_offset, self.block_text,
            self.state, self.state_machine)
        ret[0].attributes['name'] = self.name
        return ret


def setup(app):
    app.add_stylesheet('custom.css')
    app.add_javascript('custom.js')
    app.add_directive('speech', SpeechDirective)

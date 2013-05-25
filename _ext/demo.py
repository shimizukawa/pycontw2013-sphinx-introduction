# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import set_source_info

class rstdemo(nodes.Element):
    """reST demonstration block"""


class RstDemo(Directive):

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        code = u'\n'.join(self.content)

        wrapper = rstdemo()
        literal = nodes.literal_block(code, code)
        literal['language'] = 'rst'
        rendered = nodes.compound(classes=['rstdemo-rendered'])
        self.state.nested_parse(self.content, self.content_offset, rendered)
        set_source_info(self, literal)
        set_source_info(self, rendered)
        set_source_info(self, wrapper)
        wrapper.extend([literal, rendered])
        return [wrapper]


def visit_rstdemo_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='rstdemo'))


def depart_rstdemo_node(self, node=None):
    self.body.append('</div>\n')


#def on_doctree_resolved(self, doctree, docname):
#    if self.builder.name in ('singlehtml', 'html'):
#        return
#
#    for node in doctree.traverse(directives.s6_node):
#        node.parent.remove(node)



def setup(app):
    app.add_node(rstdemo, html=(visit_rstdemo_node, depart_rstdemo_node))
    app.add_directive('rstdemo', RstDemo)
#    app.connect("doctree-resolved", on_doctree_resolved)


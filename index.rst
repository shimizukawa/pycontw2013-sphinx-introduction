===================================================
Introduction to **Sphinx** documentation generator
===================================================

Who are you?
=============

.. figure:: face.png

http://about.me/shimizukawa,
@shimizukawa

* Activity:

  * Sphinx co-maintainer
  * Sphinx-users.jp chairman
  * PyCon JP 2011,2012 vice-chairman

* Books:

  * Expert Python Programming (translation by 4 members)
  * Python Professional Programming (Chap 4,7)

.. s6:: effect slide

.. s6:: styles

    'ul': {fontSize:'65%'},
    'div[0]': {width:'15%', position:'absolute', top:'0'},

.. speech::

   Hi everyone.

   My name is Takayuki Shimizukawa, I came from Japan.
   I joined the PyConTW last year, came to Taiwan is the second time.
   Activity.
   I'm member of the Sphinx co-maintainers from last November.
   And I have served as chairman of the Sphinx-users.jp community this year.
   And and, I served as vice chairman of the PyConJP last year.
   Books.
   The "Expert Python Programming" that written by Tarek Ziade in 2008.
   I and other 3 members translated in 2010, about 3 years ago.
   The "Python Professional Programming" was written by 14 colleagues of the company I belong in 2012.
   These 2 books mentions to Sphinx and Documentation.
   "Python Professional Programming" was already translated into 'simple chineese charactors' and was published maybe.


.. Important!
.. =============
.. 
.. .. s6:: effect slide
.. 
.. .. s6:: styles
.. 
..    'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}

PyCon APAC 2013 in Japan
==========================

.. figure:: pyconapac2013.png

* Schedule:

  * Conference: Sep, 14(Sat) 15(Sun)
  * Sprint: Sep, 16(Mon)

* Location:

  * Tokyo Shinjuku, Japan

* Registration:

  * Start at middle of June, (maybe)

.. speech::

   I'd like to introduce PyCon APAC 2013 in this autumn.
   We will hold 3-days event at September 14, 15, 16.
   Registration will start at middle of June, maybe.


.. s6:: styles

    'div[0]': {width:'17%', position:'absolute', top:'4em', right:'0'},

.. s6:: effect slide

Sphinx-users.jp
================

.. figure:: sphinxusers.jpg

.. figure:: SphinxConJP2012-logo.png

* Managing http://sphinx-users.jp

  * Full-translated reference : http://docs.sphinx-users.jp/
  * Original tutorial contents
  * Reverse dictionary

* Holding events

  * Sphinx & translation hack-a-thon
  * SphinxCon JP

.. speech::

   And I'd like to introduce sphinx-users community group in Japan that was called "spinx users jp".
   Sphinx-users.jp manage original site that contains full-translated reference, original tutorials and reverse dictionary.
   Also we holding monthly event "Sphinx & translation hack-a-thon" and annual event "SphinxCon JP"

.. s6:: styles

    'div[0]': {width:'45%', position:'absolute', top:'0.3em', right:'0'},
    'div[1]': {width:'50%', position:'absolute', bottom:'1em', right:'1em'},

.. s6:: effect slide

SphinxCon JP in PyCon JP 2012
==============================

.. figure:: sphinxconjp2013-atendees.jpg

.. figure:: standing-atendees.jpg

.. figure:: sphinxconjp2012-speakers.jpg

The first Sphinx event in the world!

.. todo:: photos

.. todo:: 今年のPyConAPACでもSphinx何かやるかも

.. speech::

   SphinxCon JP 2012 was very exciting.
   I think it is the first Sphinx event in the world!
   About 70 people were gathered on this event.
   We would like to do something in PyCon APAC of this year.


.. s6:: styles

    'div[0]': {width:'50%', position:'absolute', top:'3em', left:'0em'},
    'div[1]': {width:'30%', position:'absolute', top:'2.5em', right:'0em'},
    'div[2]': {width:'60%', position:'absolute', bottom:'0em', right:'1em'},

anyway.
=========


.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}


The Sphinx
============

.. figure:: sphinx-logo.png

.. speech::

   The Sphinx.
   Today, I'll talk about documentation generator that called "Sphinx".


.. s6:: effect fadeScaleFromUp

.. s6:: styles

   'h2': {fontSize:'120%', textAlign:'center'},
   'div[0]/img': {margin:'20% 10%', width:'90%'},
   'div/img': {border:'0.1em gray outset'},

Table of contents
==================

1. Introduction
2. Demonstration
3. Case studies

.. s6:: effect slide

Table of contents
====================
1. Introduction

   * Introduces the Sphinx and reStructuredText.
   * Sphinx extensions.
   * Comparison with other documentation tools.

2. Demonstration
3. Case studies

.. s6:: styles

   'ol': {color: 'gray'},
   'ol/li[0]/ul/li[0]': {color: 'white'},


What **IS** Sphinx?
=====================

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. Sphinx generates various formats such as HTML, ePub, PDF from the documentation of reStructuredText (reST) markup like Wiki and/or Python source code.

.. s6:: effect slide

Hummm???
==========

.. figure:: hummm.png

.. s6:: styles

   'h2': {display: 'none'},
   'div[0]': {width: '100%', margin:'1em'},


Sphinx **IS**
===============

* Documentation generator.
* Sphinx generate documentation from reStructuredText markup.
* Extensible.

.. figure:: sphinx-generate-several-formats.png

.. s6:: styles

   'div': {width:'55%', position:'absolute', right:'0', bottom:'1em', backgroundColor:'white'}

.. s6:: effect slide

and reStructuredText(reST) **IS**
==================================

* Markup language.
* Similer to several wiki markups.
* Written with plain text.
* Extensible **(important!)**

.. s6:: effect slide

Sphinx provides
================
Useful *reST extensions*

* Many useful **directives**.
* Many language **roles**.

.. s6:: effect slide

Sphinx provides
================
Powerful *code highlighting*

.. directive.


.. code-block:: rst

   .. code-block:: python
      :linenos:

      SPAM = 'spam'  #: nice meat.

      class Egg(object):
          "Delicious egg!"

          def __init__(self, ham):
              self.ham = ham


.. code-block:: python
   :linenos:

   SPAM = 'spam'  #: nice meat.

   class Egg(object):
       "Delicious egg!"

       def __init__(self, ham):
           self.ham = ham

.. s6:: styles

   'div[0]': {width:'80%', fontSize: '90%'},
   'div[0]/div':     {backgroundColor: '#fff'},
   'div[0]/div/pre': {backgroundColor: '#fff'},
   'div[1]': {position:'absolute', right:'0em', bottom:'0.5em'},

.. s6:: effect slide


Sphinx provides
================
*Internal links*

.. role.

* Linking between internal pages.

.. todo:: glossary, doc, ref

.. s6:: effect slide

Sphinx provides
================
*Language domains*

.. directive & role.

* C, C++, JavaScript, Python, reST.

What is domain?

.. s6:: effect slide

Sphinx provides
================
*External links*

.. extension.

* Linking to other published Sphinx document.

.. todo:: intersphinx の例

.. s6:: effect slide


Sphinx generates
=================
several output formats as:

* HTML
* PDF
* ePub
* htmlhelp
* latex
* man

.. s6:: effect slide

Sphinx includes
====================

* Simple and beautiful html themes.

.. todo:: テーマの例をいくつか

.. s6:: effect slide


.. Document generation example
.. ============================
.. 
.. .. code-block:: rst
.. 
..    reStructuredText(reST) is
..    ===========================
.. 
..    * Markup language.
..    * Similer to several wiki markups.
..    * Written with plain text.
..    * Extensible **(important!)**
.. 
.. 
.. .. figure:: sphinx-sample.jpg
.. 
.. .. s6:: styles
.. 
..    'div[0]': {width: '50%', position:'absolute', left:'0', marginTop:'0.3em'},
..    'div[0]/div/pre': {fontSize:'35%', padding:'1em'},
..    'div[1]/img': {width:'70%', position:'absolute', right:'-1em', top:'2.5em'}

Table of contents
====================
1. Introduction

   * Introduces the Sphinx and reStructuredText.
   * Sphinx extensions.
   * Comparison with other documentation tools.

2. Demonstration
3. Case studies

.. s6:: styles

   'ol': {color: 'gray'},
   'ol/li[0]/ul/li[1]': {color: 'white'},


Sphinx include official extensions
====================================

* autodoc: 
* pngmath or jsmath: 
* intersphinx: 
* graphviz: 
* todo: 
* doctest: 
* coverage: 

.. s6:: effect slide

There are many 3rd-party extensions
====================================

* Rendering diagrams from plain-text.
* Some type of html theme.
* Language domains: ada, coffee, erlan, http, php, ruby.

.. s6:: effect slide

Table of contents
====================
1. Introduction

   * Introduces the Sphinx and reStructuredText.
   * Sphinx extensions.
   * Comparison with other documentation tools.

2. Demonstration
3. Case studies

.. s6:: styles

   'ol': {color: 'gray'},
   'ol/li[0]/ul/li[2]': {color: 'white'},

.. s6:: effect slide

Compare with other tools
=========================

.. s6:: effect fadeScaleFromUp

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}

Compare with other tools
=========================

* Word
* Excel
* Wiki

.. s6:: effect slide

Sphinx vs Word
================

TBD

.. todo:: write

.. s6:: effect slide

Sphinx vs Excel
=================

TBD

.. todo:: write

.. s6:: effect slide

Sphinx vs Wiki
================

TBD

.. todo:: write

.. s6:: effect slide



By The Way
============

.. s6:: effect fadeScaleFromUp

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}


What **IS NOT** Sphinx?
========================

* Are there *GUI frontend editor?*
   * **NO!**

.. s6:: effect slide

What **IS NOT** Sphinx?
========================

* Are there a way to import *Word*?
   * **NO!!**

.. s6:: effect slide

What **IS NOT** Sphinx?
========================

* Are there a way to export to *PowerPoint*?
   * **NO!!!**

.. s6:: effect slide

What **IS NOT** Sphinx?
========================

* Are there a way to export to *Excel*?
   * **What are you saying???**

.. s6:: effect slide


Table of contents
====================
1. Introduction
2. Demonstration
3. Case studies

.. s6:: styles

   'ol': {color: 'gray'},
   'ol/li[1]': {color: 'white'},

.. s6:: effect slide


Sphinx installation
=====================

Install from PyPI:

.. code-block:: bash

  $ easy_install Sphinx
  Searching for Sphinx
  Reading http://pypi.python.org/simple/Sphinx/
  Best match: Sphinx 1.2b1
  ...
  Finished processing dependencies for Sphinx

Sphinx and other dependency packages are installed.
Sphinx 1.2b1 is current newest version.

.. speech::

   easy_install is defacto standard package installer.
   There are other installation methods: pip, buildout or invoke setup.py.

.. s6:: styles

   'p': {fontSize:'70%'},
   'div': {fontSize:'70%'},

.. s6:: effect slide

Sphinx quick start
=====================

Generate scaffold by sphinx-quickstart:

.. code-block:: bash

  $ sphinx-quickstart sample
  (many interactive questions)

Make html:

.. code-block:: bash

  $ cd sample
  $ make html

.. s6:: styles

   'p': {fontSize:'70%'},
   'div': {fontSize:'70%'},


.. s6:: effect slide


*demo:* menu
==============

* Bullet list
* Numbered list
* Code highlight
* Link to other files
* Numerical formula
* autodoc extension
* blockdiag extension

.. s6:: effect slide

*demo:* Bullet list
=====================

.. code-block:: rst

   Some text line.
   Second line will joined to 1st line.

   * item 1
   * item 2

     * item 2-1
     * item 2-2

   * item 3

.. tip:: Need blank line before and after nested items. And nested items need 2 spaces before ``*``.

.. s6:: styles

   'p': {fontSize:'70%'},
   'div': {fontSize:'70%'},

.. s6:: effect slide


*demo:* Numbered list
=====================

.. code-block:: rst

   1. item 1
   2. item 2

      #. item 2-1
      #. item 2-2

   3. item 3


.. tip:: `#.` rendering auto numbered list. but it is not human readable.

.. speech::

   "number plus dot" or "sharp plus dot" render numbered list.

.. s6:: effect slide


*demo:* Code highlight
======================

Use ``code-block`` directive to rendering code with highlighting.

.. code-block:: rst

   .. code-block:: ruby

      class Foo
        def initialize(value)
          puts "value = #{value}"
        end
      end

.. note:: This directive was provided by sphinx. Since docutils-0.9 provides :rst:dir:`code` directive that provides same feature.

.. s6:: styles

   'p': {fontSize:'70%'},
   'div': {fontSize:'70%'},

.. s6:: effect slide


*demo:* Link to other files
===========================

Use :rst:dir:`toctree` directive to build a tree structure.

.. code-block:: rst

   .. toctree::
      :numbered:
      :maxdepth: 2

      spam
      egg

.. note:: This directive was provided by sphinx.

.. s6:: effect slide

*demo:* Numerical formula
=========================

Use :rst:dir:`math` directive to rendering numerical formula.

.. code-block:: rst

   Pythagoras theorem is :math:`a^2 + b^2 = c^2`.

   .. math:: (a + b)^2 = a^2 + 2ab + b^2

   .. math::
      :nowrap:

      \begin{eqnarray}
         y    & = & ax^2 + bx + c \\
         f(x) & = & x^2 + 2xy + y^2
      \end{eqnarray}

.. note:: This directive was provided by sphinx. Same name directive was provided by docutils-0.8 or later, but it is bit different.

.. s6:: styles

   'p': {fontSize:'60%'},
   'div': {fontSize:'70%'},

.. s6:: effect slide


*demo:* todo extension
=========================

Add :mod:`sphinx.ext.todo` extention in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.todo',
   ]

Then you can use :rst:dir:`todo` directive:

.. code-block:: rst

   .. todo:: write test for this function.

and  :rst:dir:`todolist` directive:

.. code-block:: rst

   .. todolist::


.. s6:: effect slide


*demo:* autodoc extension
=========================

Add :mod:`sphinx.ext.autodoc` extention in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
   ]

Then you can use :rst:dir:`automodule` directive:

.. code-block:: rst

   .. automodule:: person
      :members:

.. s6:: effect slide

*demo:* blockdiag extensions
=============================

Blockdiag extensions is 3rd party extension for sphinx.
Install :ref:`sphinxcontrib-blockdiag` extension:

.. code-block:: bash

   $ easy_install Pillow
   $ easy_install sphinxcontrib-blockdiag
   $ easy_install sphinxcontrib-seqdiag
   $ easy_install sphinxcontrib-actdiag
   $ easy_install sphinxcontrib-nwdiag


.. note::

   Pillow is successor of PIL (Python Imaging Library) that support
   Python3 and 64bit binary distributions.

.. s6:: styles

   'p': {fontSize:'70%'},
   'div': {fontSize:'70%'},

.. s6:: effect slide

*demo:* blockdiag extension
===========================

Add ``sphinxcontrib.blockdiag`` extention in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinxcontrib.blockdiag',  #<- added
   ]

Then you can use ``blockdiag`` directive:

.. code-block:: rst

   .. blockdiag::

      {
          A [label="自己"];
          A -> B [label="Open"];
          A -> C;

          O -> P -> C;
      }

.. s6:: styles

   'p': {fontSize:'60%'},
   'div': {fontSize:'70%'},

.. s6:: effect slide


*demo:* seqdiag extension
===========================

Add ``sphinxcontrib.seqdiag`` extention in conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinxcontrib.blockdiag',
       'sphinxcontrib.seqdiag',  #<- added
   ]

Then you can use ``seqdiag`` directive:

.. code-block:: rst

   .. seqdiag::

      {
          A  => B;
          A  -> B;
          A <-- B;

          A => C => D;
      }

.. s6:: styles

   'p': {fontSize:'60%'},
   'div': {fontSize:'60%'},

.. s6:: effect slide

















さいごに
=========

.. s6:: styles

   'h2': {textAlign:'center', margin:'30% auto', background:'none'}


PyCon APAC 2013 in Japan
===========================

Sep, 14(Sat), 15(Sun), 16(Mon)

.. s6:: effect fadeScaleFromUp




.. Sphinx 1.2b1 リリース
.. ========================
.. 
.. * **3/31に1年ぶりにリリース！**
.. 
.. * 複数メンテナ体制で最初のリリース
.. * 国際化(i18n)機能の大幅強化
.. * マルチバイト言語対応強化
.. 
.. .. s6:: effect fadeScale
.. 
.. .. s6:: styles
.. 
..    'ul/li[0]': {fontSize: '120%'},
.. 
.. 
.. Sphinxの国際化(i18n)機能の強化
.. ===============================
.. 
.. * 翻訳対象となっていなかった多くの箇所の対応
.. * 公式ドキュメント多言語化(進行中)
..   Sphinx国際化機能の **モデルケース**
.. 
.. .. s6:: effect slide
.. 
.. 
.. 公式ドキュメント多言語化計画
.. =============================
.. 
.. * 日本語公式ドキュメントは今まで直接書き換えていました:
.. 
..   .. code-block:: rst
.. 
..       .. Available builders
..       .. ==================
.. 
..       利用可能なビルダー
..       ==================
.. 
.. 
.. * 今は翻訳を Transifex_ で行っています
.. 
.. .. _Transifex: https://www.transifex.com/projects/p/sphinx-doc-1_2_0/
.. 
.. .. s6:: effect slide
.. 
.. デモ
.. ======
.. 
.. .. s6:: effect slide
.. 
.. .. s6:: styles
.. 
..    'h2': {textAlign:'center', margin:'30% auto', lineHeight:'1.5em'}




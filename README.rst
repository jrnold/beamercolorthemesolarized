Beamer Color Theme Solarized
===============================

A color theme for `Beamer
<http://www.ctan.org/tex-archive/macros/latex/contrib/beamer/>`_ using
the `Solarized <http://ethanschoonover.com/solarized>`_ palette, and
inspired by the css stylesheet of `ethanshoover.com
<https://github.com/altercation/ethanschoonover.com/blob/master/resources/css/style.css>`_.

See the `Solarized homepage <http://ethanschoonover.com/solarized>`_
and its `github page
<https://github.com/altercation/ethanschoonover.com>`_ more
information about the color palette and themes for Vim, Mutt, and
Emacs among others.

Installation
===============

Get the theme from https://github.com/jrnold/beamercolortheme and
place it in either the same folder as your presentation .tex file or
in the LaTeX installation tree.

Documentation
================

To load the color theme, add the following line to your document,

::

  \usecolortheme[<options>]{solarized}

The following *<options>* may be given

- ``light`` Use the light theme (default).
- ``dark`` Use the dark theme.

- ``accent``  The accent color. This can be any of the
    non-base Solarized colors: ``yellow`` (default), ``orange``,
    ``red``, ``magenta``, ``violet``, ``blue``, ``cyan``, or
    ``green``.


In addition to the beamer colors that it sets, this package defines
colors which can be used elsewhere.
 
The package defines the sixteen colors of the Solarized palette.

:: 

    solarized@base03    #002b36 
    solarized@base02    #073642 
    solarized@base01    #586e75 
    solarized@base00    #657b83 
    solarized@base0     #839496 
    solarized@base1     #93a1a1 
    solarized@base2     #eee8d5 
    solarized@base3     #fdf6e3 
    solarized@yellow    #b58900 
    solarized@orange    #cb4b16 
    solarized@red       #dc322f 
    solarized@magenta   #d33682 
    solarized@violet    #6c71c4 
    solarized@blue      #268bd2 
    solarized@cyan      #2aa198 
    solarized@green     #859900 

Additionally, it defines these colors, whose values are
dependent on options specified when the theme is loaded.

- ``solarized@accent`` Accent color.
- ``solarized@rebase03`` - ``00`` Dark colors if dark theme, light colors if light theme.
- ``solarized@rebase0`` - ``03`` Light colors if dark theme, dark colors if light theme.
  



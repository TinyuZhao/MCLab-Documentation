.. _uiflow1-blockly-generic-emoji:

.. currentmodule:: emoji

.. include:: ../refs/emoji.ref

Emoji
=====

``emoji.Emoji`` draws a pixel-art emoji on the display as a grid of coloured
squares.

Compatibility
-------------

``emoji.Emoji`` draws through the board's LVGL display, so the display must
already be initialized before construction.

MicroPython Examples
--------------------

Draw a custom emoji map
^^^^^^^^^^^^^^^^^^^^^^^

Open the |emoji_example.m5f| project in MCLab.

This example creates a 7 by 7 emoji grid and draws a custom pattern in red.

MCLab Code Block:

    |emoji_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/emoji/emoji_example.py
        :language: python

**API**
-------

.. autoclass:: Emoji
    :members: draw_square, show_map
    :member-order: bysource

.. _uiflow1-blockly-ui-screen:

.. currentmodule:: MakerAndCoder_ui

.. include:: ../refs/MakerAndCoder_ui.ref

Screen
======

``MCScreen`` manages a screen's LVGL background and backlight. The MCLab
screen blocks also show older ``lcd`` drawing calls; the Ednex UI object uses
``MCScreen`` and ``power.setLCDBrightness`` instead of an ``lcd.setBrightness``
method.

Compatibility
-------------

``MakerAndCoder_ui.MCScreen`` uses the board's LVGL display. Board startup
initializes the screen and backlight. The example requires a running display and cannot run on a
headless MicroPython port.

MicroPython Examples
--------------------

Change the background color
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |screen_example.m5f| project in MCLab.

This example creates a UI screen and alternates its background color between red and teal once per second.

MCLab Code Block:

    |screen_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/ui/screen/screen_example.py
        :language: python

**API**
-------

.. currentmodule:: MakerAndCoder_ui

.. autoclass:: MCScreen
    :members: clean_screen, set_screen_bg_color, set_screen_brightness
    :member-order: bysource

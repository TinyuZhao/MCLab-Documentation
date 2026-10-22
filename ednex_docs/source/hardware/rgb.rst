.. _uiflow1-blockly-hardware-rgb:

.. currentmodule:: units._rgb_multi

.. include:: ../refs/hardware.rgb.ref

RGB
===

The ``unit.Rgb`` object controls the board RGB strip. Colors are represented as packed ``0xRRGGBB`` integers.

MicroPython Examples
--------------------

Set the RGB strip
^^^^^^^^^^^^^^^^^

Open the |rgb_example.m5f| project in MCLab.

This example sets the whole RGB strip to one color and lowers the brightness.

MCLab Code Block:

    |rgb_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/rgb/rgb_example.py
        :language: python

**API**
-------

.. currentmodule:: units._rgb_multi

.. autoclass:: Rgb_multi
    :members: setColor, setColorFrom, setColorAll, setBrightness
    :no-index:

.. _uiflow1-blockly-hardware-power:

.. currentmodule:: hardware.axp192

.. include:: ../refs/hardware.axp192.ref

Power
=====

The board ``power`` object reports battery and bus measurements and controls
power-management outputs.

MicroPython Examples
--------------------

Monitor power
^^^^^^^^^^^^^

Open the |power_example.m5f| project in MCLab.

This example sets the screen brightness and the power LED, then prints the VBus voltage.

MCLab Code Block:

    |power_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/power/power_example.py
        :language: python

**API**
-------

.. currentmodule:: hardware.axp192

.. automodule:: hardware.axp192
    :members:
    :member-order: bysource

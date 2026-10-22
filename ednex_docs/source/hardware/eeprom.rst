.. _uiflow1-blockly-hardware-eeprom:

.. currentmodule:: libs.nvs

.. include:: ../refs/libs.nvs.ref

EEPROM
======

The ``nvs`` helpers store small values in non-volatile storage using a string
key.

MicroPython Examples
--------------------

Store and read a value
^^^^^^^^^^^^^^^^^^^^^^

Open the |eeprom_example.m5f| project in MCLab.

This example writes a value under a key and reads it back as text.

MCLab Code Block:

    |eeprom_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/eeprom/eeprom_example.py
        :language: python

**API**
-------

.. currentmodule:: libs.nvs

.. automodule:: libs.nvs
    :members:
    :member-order: bysource

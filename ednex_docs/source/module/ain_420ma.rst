.. currentmodule:: modules._ain_420ma

AIN4-20mA Module
================

.. include:: ../refs/modules._ain_420ma.ref

This page documents the public API for the ain_420ma driver.

MicroPython Examples
--------------------

Read Analog Current
^^^^^^^^^^^^^^^^^^^

Open the |ain_420ma_example.m5f| project in MCLab.

This example initializes the 4-20 mA module at I2C address 0x55 and continuously prints the current reading from channel 1.

MCLab Code Block:

    |ain_420ma_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/module/ain_420ma/ain_420ma_example.py
        :language: python

**API**
-------

.. currentmodule:: modules._ain_420ma

.. automodule:: modules._ain_420ma
    :members:
    :member-order: bysource

.. _uiflow1-blockly-hardware-i2c_master:

.. currentmodule:: i2c_bus

.. include:: ../refs/i2c_bus.ref

I2C Master
==========

The ``i2c_bus`` helpers open an I2C bus for a board port and provide
register-oriented reads and writes through ``easyI2C``.

MicroPython Examples
--------------------

Check an I2C address
^^^^^^^^^^^^^^^^^^^^

Open the |i2c_master_example.m5f| project in MCLab.

This example sets the slave address and prints whether the device responds.

MCLab Code Block:

    |i2c_master_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/i2c_master/i2c_master_example.py
        :language: python

**API**
-------

.. currentmodule:: i2c_bus

.. automodule:: i2c_bus
    :members:
    :member-order: bysource

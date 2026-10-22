.. _uiflow1-blockly-advanced-modbus_master:

.. currentmodule:: libs.modbus.master.uModBusSerial

.. include:: ../refs/advanced.modbus_master.ref

Modbus Master
=============


The serial Modbus master class provides register and coil operations for a configured bus.

MicroPython Examples
--------------------

Read holding registers
^^^^^^^^^^^^^^^^^^^^^^

Open the |modbus_master_example.m5f| project in MCLab.

This example configures a Modbus RTU master on UART 2 and displays three holding registers read on button A.

MCLab Code Block:

    |modbus_master_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/modbus_master/modbus_master_example.py
        :language: python

**API**
-------

.. automodule:: libs.modbus.master.uModBusSerial
    :members:
    :exclude-members: uModBusSerial

.. autoclass:: uModBusSerial
    :members: read_coils, read_discrete_inputs, read_holding_registers, read_input_registers, write_single_coil, write_single_register, write_multiple_coils, write_multiple_registers, close
    :member-order: bysource

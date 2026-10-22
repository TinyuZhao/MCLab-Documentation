.. _uiflow1-blockly-advanced-modbus_slave:

.. currentmodule:: libs.modbus.slave.rtu

.. include:: ../refs/advanced.modbus_slave.ref

Modbus Slave
============


The Modbus slave class exposes register operations and the update loop used by a slave endpoint.

MicroPython Examples
--------------------

Run a Modbus RTU slave
^^^^^^^^^^^^^^^^^^^^^^

Open the |modbus_slave_example.m5f| project in MCLab.

This example starts a Modbus RTU slave on UART 2 and publishes three holding registers that button A updates.

MCLab Code Block:

    |modbus_slave_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/modbus_slave/modbus_slave_example.py
        :language: python

**API**
-------

.. automodule:: libs.modbus.slave.rtu
    :members:
    :exclude-members: ModbusSlave

.. autoclass:: ModbusSlave
    :members: read_coils, read_discrete_inputs, read_holding_registers, read_input_registers, write_single_coil, write_single_register, write_multiple_coils, write_multiple_registers, update_process, get_datavalue, set_datavalue, function_init
    :member-order: bysource

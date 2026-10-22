.. _uiflow1-blockly-hardware-system:

.. currentmodule:: machine

.. include:: ../refs/hardware.system.ref

System
======

The System Blockly group exposes a device reset through ``machine.reset``.
A reset restarts the firmware and does not resume execution after this call.

Compatibility
-------------

``machine.reset`` is exported by this firmware's ``machine`` module. Save
important state before resetting; open connections and in-memory values are
lost.

MicroPython Examples
--------------------

Restart the device
^^^^^^^^^^^^^^^^^^

Open the |system_example.m5f| project in MCLab.

This example restarts the board when button B is pressed.

MCLab Code Block:

    |system_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/system/system_example.py
        :language: python

**API**
-------

Function
--------

.. function:: reset() -> None

    Reset the device immediately. This call does not return to the current
    program.

    MCLab Code Block:

        |reset.png|

    MicroPython Code Block:

        .. code-block:: python

            machine.reset()

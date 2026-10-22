.. currentmodule:: ubt_controller

GamePad
=======

.. include:: ../refs/ubt_controller.ref

``UBTBLECentral`` provides Bluetooth GamePad discovery, connection, and input callbacks.

MicroPython Examples
--------------------

Open the |gamepad_example.m5f| project in MCLab.

The example scans for and connects to a GamePad, then reports joystick updates.

MCLab Code Block:

    .. image:: ../static/mclab/gamepad/gamepad_example.png

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/gamepad/gamepad_example.py
        :language: python

**API**
-------

.. autoclass:: UBTBLECentral
    :members: __init__, set_event, is_connected, scan, connect, disconnect,
        get_button_state, get_joystick_pos
    :member-order: bysource

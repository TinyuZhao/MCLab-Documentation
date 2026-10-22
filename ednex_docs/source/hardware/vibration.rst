.. _uiflow1-blockly-hardware-vibration:

.. currentmodule:: hardware.axp192

.. include:: ../refs/hardware.axp192.ref

Vibration
=========

The board power controller exposes vibration motor enable and intensity
controls. The startup singleton is available as ``power``.

MicroPython Examples
--------------------

Pulse the motor
^^^^^^^^^^^^^^^

Open the |vibration_example.m5f| project in MCLab.

This example switches the vibration motor on and off once per second.

MCLab Code Block:

    |vibration_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/vibration/vibration_example.py
        :language: python

**API**
-------

.. currentmodule:: hardware.axp192

.. autoclass:: Axp192
    :members: setVibrationEnable, setVibrationIntensity
    :no-index:

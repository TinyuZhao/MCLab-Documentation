.. _uiflow1-blockly-advanced-pin_servo:

.. currentmodule:: libs.servo

.. include:: ../refs/advanced.pin_servo.ref

Pin Servo
=========


The ``Servo`` class controls hobby-servo pulse width or angle and can release its PWM resource.

MicroPython Examples
--------------------

Sweep a servo
^^^^^^^^^^^^^

Open the |pin_servo_example.m5f| project in MCLab.

This example moves a servo to 0 and 180 degrees, then to 500 and 2500 microsecond pulses, once per second.

MCLab Code Block:

    |pin_servo_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/pin_servo/pin_servo_example.py
        :language: python

**API**
-------

.. automodule:: libs.servo
    :members:
    :exclude-members: Servo

.. autoclass:: Servo
    :members: write_us, write_angle, deinit
    :member-order: bysource

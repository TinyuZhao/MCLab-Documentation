.. currentmodule:: units._watering

Watering Unit
=============

.. include:: ../refs/units._watering.ref

This page documents the public API for the Watering driver.

MicroPython Examples
--------------------

Monitor Soil Moisture and Control the Pump
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |Watering_example.m5f| project in MCLab.

This example reads the moisture ADC value and turns the pump on below 1000 or off at and above 1000.

MCLab Code Block:

    |Watering_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/unit/Watering/Watering_example.py
        :language: python

**API**
-------

.. currentmodule:: units._watering

.. automodule:: units._watering
    :members:
    :member-order: bysource

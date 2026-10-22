.. _uiflow1-blockly-hardware-rtc:

.. currentmodule:: hardware.bm8563

.. include:: ../refs/hardware.bm8563.ref

RTC
===

The board ``rtc`` object reads and writes the BM8563 real-time clock and can
set its time from an NTP host.

MicroPython Examples
--------------------

Synchronize and read the clock
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |rtc_example.m5f| project in MCLab.

This example sets the clock from an NTP host and prints the RTC time.

MCLab Code Block:

    |rtc_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/rtc/rtc_example.py
        :language: python

**API**
-------

.. currentmodule:: hardware.bm8563

.. automodule:: hardware.bm8563
    :members:
    :member-order: bysource

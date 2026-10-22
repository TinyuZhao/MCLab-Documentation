.. _uiflow1-blockly-hardware-wdt:

.. currentmodule:: machine

.. include:: ../refs/hardware.wdt.ref

Watch Dog Timer
===============

``machine.WDT`` resets the controller if software fails to feed the watchdog
before its timeout. Create it only after the program is ready to feed it.

Compatibility
-------------

This firmware accepts watchdog ID 0 and a timeout in milliseconds. The timeout is truncated to whole seconds;
values below 1000 ms are rejected. A watchdog cannot be disabled after it is
started, so test with a safe timeout.

MicroPython Examples
--------------------

Feed the watchdog
^^^^^^^^^^^^^^^^^

Open the |wdt_example.m5f| project in MCLab.

This example starts the watchdog and feeds it every three seconds.

MCLab Code Block:

    |wdt_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/wdt/wdt_example.py
        :language: python

**API**
-------

WDT
---

.. class:: WDT(id=0, timeout=5000)

    Start the ESP32 task watchdog. The constructor accepts only ID 0. The
    watchdog cannot be stopped after construction.

    :param int id: Watchdog identifier; only 0 is valid.
    :param int timeout: Timeout in milliseconds, rounded down to whole seconds.

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            from machine import WDT
            wdt = WDT(timeout=5000)

    .. method:: WDT.feed() -> None

        Restart the watchdog countdown. Call this regularly while the program
        is operating normally.

        MCLab Code Block:

            |feed.png|

        MicroPython Code Block:

            .. code-block:: python

                wdt.feed()

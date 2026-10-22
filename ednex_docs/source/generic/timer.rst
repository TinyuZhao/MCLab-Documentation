.. _uiflow1-blockly-generic-timer:

.. currentmodule:: time

Timer
=====

.. include:: ../refs/generic.timer.ref

The ``time`` module provides blocking delays and a wrapping millisecond
counter. Use ``ticks_diff`` rather than ordinary subtraction when measuring
elapsed time across a counter wraparound.

MicroPython Examples
--------------------

Read the millisecond counter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |timer_example.m5f| project in MCLab.

This example prints the millisecond counter once per second.

MCLab Code Block:

    |timer_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/timer/timer_example.py
        :language: python

**API**
-------

Function
--------

.. function:: ticks_ms() -> int

    Read the wrapping millisecond tick counter. The value is useful for
    intervals, not as a calendar timestamp.

    :return: Current millisecond counter.
    :rtype: int

    MCLab Code Block:

        |ticks_ms.png|

    MicroPython Code Block:

        .. code-block:: python

            started = time.ticks_ms()

.. function:: ticks_diff(ticks1, ticks2) -> int

    Return the signed difference between two tick values, accounting for
    counter wraparound within the supported interval.

    :param int ticks1: More recent tick value.
    :param int ticks2: Earlier tick value.
    :return: Elapsed milliseconds as a signed integer.
    :rtype: int

    MicroPython Code Block:

        .. code-block:: python

            elapsed = time.ticks_diff(time.ticks_ms(), started)

.. function:: sleep_ms(ms) -> None

    Block execution for approximately ``ms`` milliseconds.

    :param int ms: Delay in milliseconds.

    MCLab Code Block:

        |sleep_ms.png|

    MicroPython Code Block:

        .. code-block:: python

            time.sleep_ms(100)

.. function:: sleep(seconds) -> None

    Block execution for approximately ``seconds`` seconds.

    :param seconds: Delay in seconds.
    :type seconds: int or float

    MCLab Code Block:

        |sleep.png|

    MicroPython Code Block:

        .. code-block:: python

            time.sleep(1)

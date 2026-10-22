.. _uiflow1-blockly-generic-loops:

.. currentmodule:: builtins

Loops
=====

.. include:: ../refs/generic.loops.ref

``for`` and ``while`` statements repeat a block of MicroPython code. Indent
the body consistently and use ``break`` or ``continue`` to control iteration.

MicroPython Examples
--------------------

Iterate over a range
^^^^^^^^^^^^^^^^^^^^

Open the |loops_example.m5f| project in MCLab.

This example iterates over an even range and prints each value once per second.

MCLab Code Block:

    |loops_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/loops/loops_example.py
        :language: python

**API**
-------

``for``, ``while``, ``break`` and ``continue`` are language syntax, not
callable functions. The ``range`` built-in produces the iterable used by a
``for`` loop.

Function
--------

.. function:: range(stop)
              range(start, stop[, step])

    Return an iterable of integers. With one argument the values run from
    ``0`` up to, but not including, ``stop``; an explicit ``start`` and
    ``step`` control the sequence.

    :param int start: First value; defaults to 0.
    :param int stop: Exclusive upper bound.
    :param int step: Increment between values; defaults to 1.
    :return: Iterable integer range.
    :rtype: range

    MCLab Code Block:

        |range.png|

    MicroPython Code Block:

        .. code-block:: python

            for number in range(3):
                print(number)

Repeat a block
--------------

The ``repeat`` block runs its body a fixed number of times. Iterate over
``range`` when the counter is not used.

MCLab Code Block:

    |repeat.png|

MicroPython Code Block:

    .. code-block:: python

        for _ in range(10):
            print("tick")

Iterate over an iterable
------------------------

The ``for each`` block walks every item of a list, tuple, string or other
iterable.

MCLab Code Block:

    |forEach.png|

MicroPython Code Block:

    .. code-block:: python

        total = 0
        for number in (5, 6, 7):
            total += number

Conditional loops
-----------------

The ``while`` block repeats while its condition remains true. Ensure that the
loop condition eventually changes when running on a device.

MCLab Code Block:

    |while.png|

MicroPython Code Block:

    .. code-block:: python

        count = 0
        while count < 3:
            count += 1

Loop control
------------

``break`` leaves the loop immediately and ``continue`` skips to the next
iteration.

MCLab Code Block:

    |flow_statements.png|

MicroPython Code Block:

    .. code-block:: python

        for number in range(10):
            if number == 2:
                continue
            if number == 5:
                break

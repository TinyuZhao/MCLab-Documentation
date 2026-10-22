.. _uiflow1-blockly-generic-functions:

.. currentmodule:: builtins

Functions
=========

.. include:: ../refs/generic.functions.ref

A function groups reusable statements and receives values through parameters.
``def`` and ``return`` are Python language syntax, not callable APIs.

Compatibility
-------------

The examples use core MicroPython syntax and do not require peripheral
hardware. Names introduced by ``def`` exist only after their definition runs.

MicroPython Examples
--------------------

Define and call a function
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |functions_example.m5f| project in MCLab.

This example defines a function with one parameter and calls it with random values.

MCLab Code Block:

    |functions_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/functions/functions_example.py
        :language: python

**API**
-------

Function definition
-------------------

.. function:: add(left, right) -> int

    This is the example function defined above, not a preinstalled Ednex API.
    ``def`` names a function and ``return`` supplies its result. Omitting
    ``return`` produces ``None``.

    :param int left: First integer to add.
    :param int right: Second integer to add.
    :return: Sum of the operands.
    :rtype: int

    MCLab Code Block:

        |defnoreturn.png|

        |defreturn.png|

    MicroPython Code Block:

        .. code-block:: python

            def add(left, right):
                return left + right

Return a value
--------------

A ``return`` statement ends the function and supplies its result. A
conditional ``return`` exits early when a condition holds.

MCLab Code Block:

    |ifreturn.png|

MicroPython Code Block:

    .. code-block:: python

        def absolute(value):
            if value < 0:
                return -value
            return value

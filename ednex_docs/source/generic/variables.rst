.. _uiflow1-blockly-generic-variables:

.. currentmodule:: builtins

.. include:: ../refs/generic.variables.ref

Variables
=========

Variables bind names to values. The examples on this page use ordinary
MicroPython assignment and augmented-assignment syntax; no device-specific
module is required.

MicroPython Examples
--------------------

Assign and print a variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |variables_example.m5f| project in MCLab.

This example assigns a string to a variable and prints it.

MCLab Code Block:

    |variables_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/variables/variables_example.py
        :language: python

**API**
-------

The blocks in this section represent Python language syntax, not callable
functions or class methods.

Assignment
^^^^^^^^^^

Assign a value with ``=``, then use an augmented assignment such as ``+=`` or
``-=`` to update the existing value. A name can be rebound to a different
type, as in normal Python code.

MCLab Code Block:

    |variables_set.png|

MicroPython Code Block:

    .. code-block:: python

        value = 10
        value = value + 1
        value += 2
        print(value)

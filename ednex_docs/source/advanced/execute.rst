.. _uiflow1-blockly-advanced-execute:

.. currentmodule:: uiflow

.. include:: ../refs/advanced.execute.ref

Execute
=======





The Execute block inserts Python statements directly into the generated program. It does not provide a separate firmware function.

MicroPython Examples
--------------------

Execute Python text
^^^^^^^^^^^^^^^^^^^

Open the |execute_example.m5f| project in MCLab.

This example runs the Python text stored in the execute block, which prints a message.

MCLab Code Block:

    |execute_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/execute/execute_example.py
        :language: python

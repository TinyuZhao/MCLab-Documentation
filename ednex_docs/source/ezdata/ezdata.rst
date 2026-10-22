.. _uiflow1-blockly-ezdata-ezdata:

.. currentmodule:: flow.ezdata

.. include:: ../refs/flow.ezdata.ref

EzData
======


The ``flow.ezdata`` module provides synchronous and callback-based operations for storing, retrieving, and removing values.

MicroPython Examples
--------------------

Store, read, and remove a value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |ezdata_example.m5f| project in MCLab.

The ``flow.ezdata`` module provides synchronous and callback-based operations for storing, retrieving, and removing values. This example connects Wi-Fi, writes a value to a topic, reads it back, prints the current ISO date and time, and removes the value.

MCLab Code Block:

    |ezdata_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/ezdata/ezdata/ezdata_example.py
        :language: python

**API**
-------

.. automodule:: flow.ezdata
    :members: setData, setDataAsync, getData, getDataAsync, removeData, removeDataAsync, addToList, addToListAsync, getCurrentISODateTime, getCurrentISODateTimeAsync, startQueue
    :exclude-members: __dict__, __weakref__

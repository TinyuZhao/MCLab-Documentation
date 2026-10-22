.. _uiflow1-blockly-generic-json:

.. currentmodule:: json

JSON
====

.. include:: ../refs/generic.json.ref

The standard ``json`` module serializes supported Python values to text and
parses JSON text back into Python values. Object and key access use ordinary
dictionary operations; see the Map page. The ``json_py`` helpers behind the
MCLab JSON blocks accept either a parsed record or JSON text.

MicroPython Examples
--------------------

Create a record and read its fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |json_example.m5f| project in MCLab.

This example builds a record from key/value pairs and prints the encoded form, its keys, its values, and the number of keys.

MCLab Code Block:

    |json_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/json/json_example.py
        :language: python

**API**
-------

Function
--------

.. function:: dumps(obj) -> str

    Serialize a JSON-compatible Python value to a string. Dictionaries,
    lists, strings, numbers, booleans and ``None`` can be serialized.

    :param obj: JSON-compatible value to serialize.
    :type obj: dict or list or str or int or float or bool or None
    :return: JSON-formatted text.
    :rtype: str

    MCLab Code Block:

        |dumps.png|

    MicroPython Code Block:

        .. code-block:: python

            encoded = json.dumps({"count": 2})

.. function:: loads(s)

    Parse a JSON-formatted string and return the corresponding Python value.
    Object keys become strings.

    :param str s: JSON text to parse.
    :return: Parsed Python value.
    :rtype: dict or list or str or int or float or bool or None

    MCLab Code Block:

        |loads.png|

    MicroPython Code Block:

        .. code-block:: python

            decoded = json.loads('{"count": 2}')

JSON helpers
------------

.. include:: ../refs/json_py.ref

The ``json_py`` module provides the helpers behind the MCLab JSON blocks.

.. currentmodule:: json_py

.. automodule:: json_py
    :members: py_2_json, json_2_py, get_json_key, get_json_keys,
        get_json_values, get_json_keys_len, set_json_elements,
        delete_json_elements
    :member-order: bysource

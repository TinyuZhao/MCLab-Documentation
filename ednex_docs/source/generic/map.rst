.. _uiflow1-blockly-generic-map:

.. currentmodule:: builtins

Map
===

.. include:: ../refs/generic.map.ref

A Python dictionary maps hashable keys to values. It can be modified in
place; a key selects one stored value.

MicroPython Examples
--------------------

Read dictionary values
^^^^^^^^^^^^^^^^^^^^^^

Open the |map_example.m5f| project in MCLab.

This example reads two values from a dictionary by key.

MCLab Code Block:

    |map_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/map/map_example.py
        :language: python

**API**
-------

Dictionary
----------

.. class:: dict(mapping=())

    Construct a dictionary from a mapping or key-value pairs. ``{}`` is
    literal syntax for an empty dictionary.

    :param mapping: Initial key-value pairs.
    :type mapping: mapping or iterable

    MCLab Code Block:

        |create.png|

    MicroPython Code Block:

        .. code-block:: python

            record = {"a": 1, "b": 2}

    .. method:: dict.get(key, default=None)

        Return the value of ``key`` or ``default`` if it does not exist.

        :param key: Key to look up.
        :type key: object
        :param default: Fallback for a missing key.
        :type default: object
        :return: Found value or fallback.
        :rtype: object

        MCLab Code Block:

            |get.png|

        MicroPython Code Block:

            .. code-block:: python

                value = record.get("missing", 0)

    .. method:: dict.pop(key)

        Remove ``key`` and return its value. A missing key raises
        ``KeyError`` unless a fallback argument is supplied.

        :param key: Key to remove.
        :type key: object
        :return: Removed value.
        :rtype: object

        MCLab Code Block:

            |delete_key.png|

        MicroPython Code Block:

            .. code-block:: python

                removed = record.pop("b")

    .. method:: dict.clear() -> None

        Remove all items from the dictionary.

        MCLab Code Block:

            |clear.png|

        MicroPython Code Block:

            .. code-block:: python

                record.clear()

    .. method:: dict.items()

        Return an iterable of key-value pairs for iteration.

        :return: Key-value pairs.
        :rtype: iterable

        MicroPython Code Block:

            .. code-block:: python

                for key, value in record.items():
                    print(key, value)

Membership and assignment
-------------------------

``key in record`` tests whether a key exists. ``record[key] = value``
creates or replaces an entry; accessing a missing key with ``record[key]``
raises ``KeyError``.

MCLab Code Block:

    |contains_key.png|

    |add_key.png|

    |set_key.png|

MicroPython Code Block:

    .. code-block:: python

        present = "a" in record
        record["c"] = 3

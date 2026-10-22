.. _uiflow1-blockly-generic-bytearray:

.. currentmodule:: builtins

.. include:: ../refs/generic.bytearray.ref

Bytearray
=========

``bytearray`` is a mutable sequence of integers in the range 0--255. Use it
for binary buffers whose contents change before transmission or decoding.

Compatibility
-------------

``bytearray`` is a MicroPython built-in. The example uses only built-in
operations and does not require a particular external device.

MicroPython Examples
--------------------

Append bytes and print the buffer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |bytearray_example.m5f| project in MCLab.

This example appends two bytes and prints the buffer length and every element.

MCLab Code Block:

    |bytearray_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/bytearray/bytearray_example.py
        :language: python

**API**
-------

Bytearray
---------

.. class:: bytearray(source=b"")

    Construct a mutable byte sequence from bytes or an iterable of integers
    from 0 through 255. Passing an integer creates a zero-filled buffer of
    that length.

    :param source: Initial bytes, iterable, or number of zero bytes.
    :type source: bytes or iterable or int

    MicroPython Code Block:

        .. code-block:: python

            payload = bytearray(5)

    .. method:: bytearray.append(value) -> None

        Add one byte at the end of the buffer.

        :param int value: Byte to add, in the range 0--255.

        MCLab Code Block:

            |append.png|

        MicroPython Code Block:

            .. code-block:: python

                payload.append(33)

    .. method:: bytearray.extend(iterable) -> None

        Append every byte of another sequence to the buffer.

        :param iterable: Bytes or an iterable of byte values.

        MCLab Code Block:

            |extend.png|

        MicroPython Code Block:

            .. code-block:: python

                payload.extend(b" world")

    .. method:: bytearray.decode(encoding="utf-8") -> str

        Decode the buffer as text using the requested character encoding.

        :param str encoding: Character encoding, such as ``"utf-8"``.
        :return: Decoded text.
        :rtype: str

        MCLab Code Block:

            |decode.png|

        MicroPython Code Block:

            .. code-block:: python

                text = payload.decode("utf-8")

Indexing and slicing
--------------------

An indexed element is read or written with Python indexing syntax, and a
range of elements with a slice. These are language constructs rather than
method calls.

MCLab Code Block:

    |getIndex.png|

    |setIndex.png|

    |getSublist.png|

MicroPython Code Block:

    .. code-block:: python

        first = payload[0]
        payload[0] = 104
        head = payload[0:4]

.. _uiflow1-blockly-generic-text:

.. currentmodule:: builtins

Text
====

.. include:: ../refs/generic.text.ref

MicroPython strings are immutable sequences of Unicode characters. Methods
create new strings instead of changing an existing string in place.

MicroPython Examples
--------------------

Transform a string
^^^^^^^^^^^^^^^^^^

Open the |text_example.m5f| project in MCLab.

This example converts a string to uppercase and prints it.

MCLab Code Block:

    |text_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/text/text_example.py
        :language: python

**API**
-------

String
------

.. class:: str(object="")

    Convert an object to text. Strings are immutable; methods return a new
    string rather than changing the original.

    :param object: Value to convert.
    :type object: object

    MCLab Code Block:

        |to_str.png|

    MicroPython Code Block:

        .. code-block:: python

            text = str(2500)

    .. method:: str.upper() -> str

        Return a copy of the string with all characters converted to upper
        case. ``str.lower`` performs the inverse conversion.

        :return: Upper-case copy.
        :rtype: str

        MCLab Code Block:

            |changeCase.png|

        MicroPython Code Block:

            .. code-block:: python

                name = "ednex".upper()

    .. method:: str.count(sub[, start[, end]]) -> int

        Return the number of non-overlapping occurrences of ``sub``.

        :param str sub: Substring to count.
        :return: Number of occurrences.
        :rtype: int

        MCLab Code Block:

            |count.png|

        MicroPython Code Block:

            .. code-block:: python

                hits = "hello world".count("o")

    .. method:: str.replace(old, new[, count]) -> str

        Return a copy with every occurrence of ``old`` replaced by ``new``.

        :param str old: Substring to replace.
        :param str new: Replacement text.
        :return: Updated copy.
        :rtype: str

        MCLab Code Block:

            |replace.png|

        MicroPython Code Block:

            .. code-block:: python

                changed = "hello world".replace("world", "MicroPython")

    .. method:: str.strip([chars]) -> str

        Return a copy with leading and trailing whitespace removed, or with
        the characters in ``chars`` removed when supplied.

        :param str chars: Optional set of characters to remove.
        :return: Trimmed copy.
        :rtype: str

        MCLab Code Block:

            |trim.png|

            |trim_string.png|

        MicroPython Code Block:

            .. code-block:: python

                trimmed = "  value  ".strip()

    .. method:: str.format(*args, **kwargs) -> str

        Build a string from a replacement-field template. A format
        specification such as ``{:.2f}`` limits a number to a fixed number of
        decimal places.

        :return: Formatted string.
        :rtype: str

        MCLab Code Block:

            |format_decimals.png|

        MicroPython Code Block:

            .. code-block:: python

                text = "{:.2f}".format(3.14159)

    .. method:: str.encode(encoding="utf-8") -> bytes

        Encode the string to bytes using the requested character encoding.

        :param str encoding: Character encoding; defaults to ``"utf-8"``.
        :return: Encoded bytes.
        :rtype: bytes

        MCLab Code Block:

            |encode.png|

        MicroPython Code Block:

            .. code-block:: python

                data = "ednex".encode()

Characters and indexing
-----------------------

``text[index]`` returns a one-character string. Indexing begins at zero and
negative indices count from the end; a slice ``text[start:stop]`` returns a
substring.

MCLab Code Block:

    |charAt.png|

MicroPython Code Block:

    .. code-block:: python

        first = "hello"[0]
        part = "hello"[1:3]

Length and emptiness
--------------------

``len(text)`` returns the number of characters in the string; a string is
empty when its length is ``0``.

MCLab Code Block:

    |length.png|

    |isEmpty.png|

MicroPython Code Block:

    .. code-block:: python

        size = len("hello")
        empty = len("hello") == 0

Working with bytes
------------------

.. method:: bytes.decode(encoding="utf-8") -> str

    Decode bytes to a string using the requested character encoding.

    :param str encoding: Character encoding; defaults to ``"utf-8"``.
    :return: Decoded text.
    :rtype: str

    MCLab Code Block:

        |decode.png|

    MicroPython Code Block:

        .. code-block:: python

            text = b"hello".decode("utf-8")

.. currentmodule:: binascii

.. function:: hexlify(data) -> bytes

    Return the hexadecimal representation of the bytes in ``data``.

    :param data: Data to encode.
    :type data: bytes
    :return: Hexadecimal bytes.
    :rtype: bytes

    MCLab Code Block:

        |bytestr_to_hexstr.png|

    MicroPython Code Block:

        .. code-block:: python

            import binascii

            encoded = binascii.hexlify(b"hello")

.. function:: unhexlify(data) -> bytes

    Decode hexadecimal text back to bytes.

    :param data: Hexadecimal text.
    :type data: bytes or str
    :return: Decoded bytes.
    :rtype: bytes

    MCLab Code Block:

        |hexstr_to_bytestr.png|

    MicroPython Code Block:

        .. code-block:: python

            decoded = binascii.unhexlify(b"68656c6c6f")

Concatenation and printing
--------------------------

The ``+`` operator joins two strings and ``print`` writes values to the
console.

MCLab Code Block:

    |add.png|

    |print.png|

MicroPython Code Block:

    .. code-block:: python

        message = "value=" + str(2500)
        print(message)

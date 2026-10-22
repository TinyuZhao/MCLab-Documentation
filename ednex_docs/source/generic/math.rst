.. _uiflow1-blockly-generic-math:

.. currentmodule:: math

Math
====

.. include:: ../refs/generic.math.ref

MicroPython offers numeric operators, built-in numeric functions, the
``math`` module and the ``random`` module. This page documents the callable
numeric APIs behind the MCLab Blockly math blocks; MCLab-specific helper
names without a verified Ednex implementation are not documented as public
APIs.

MicroPython Examples
--------------------

Generate random numbers
^^^^^^^^^^^^^^^^^^^^^^^

Open the |math_example.m5f| project in MCLab.

This example prints a random integer in the range 0 to 255 once per second.

MCLab Code Block:

    |math_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/math/math_example.py
        :language: python

**API**
-------

Arithmetic and bitwise operators
--------------------------------

``+``, ``-``, ``*``, ``/``, ``//``, ``%`` and ``**`` are language operators,
not functions. Bitwise integer operators are ``&``, ``|``, ``^``, ``~``,
``<<`` and ``>>``, and ``%`` also yields the remainder of a division.

MCLab Code Block:

    |arithmetic.png|

    |modulo.png|

    |bit_operation.png|

MicroPython Code Block:

    .. code-block:: python

        remainder = 9 % 2
        power = 2 ** 3
        bit = (0b0101 >> 2) & 1

Constants
---------

.. data:: pi

    Ratio of a circle's circumference to its diameter.

    MCLab Code Block:

        |constants.png|

    MicroPython Code Block:

        .. code-block:: python

            circumference = 2 * math.pi * radius

.. data:: e

    Base of the natural logarithm.

Functions
---------

.. function:: sqrt(x) -> float

    Return the nonnegative square root of ``x``.

    :param x: Nonnegative number.
    :type x: int or float
    :return: Square root of ``x``.
    :rtype: float

    MCLab Code Block:

        |sqrt.png|

    MicroPython Code Block:

        .. code-block:: python

            root = math.sqrt(9)

.. function:: sin(x) -> float

    Return the sine of an angle in radians.

    :param x: Angle in radians.
    :type x: int or float
    :return: Sine value.
    :rtype: float

    MCLab Code Block:

        |sin.png|

    MicroPython Code Block:

        .. code-block:: python

            value = math.sin(math.pi / 2)

Built-in functions
------------------

``round``, ``int``, ``float`` and ``sum`` are built-ins rather than members of
``math``. They can be combined with operators and module functions in
expressions.

.. currentmodule:: builtins

.. function:: round(value, ndigits=None)

    Round ``value`` to ``ndigits`` decimal places, or to the nearest integer
    when ``ndigits`` is omitted.

    :param value: Number to round.
    :type value: int or float
    :param int ndigits: Optional number of decimal places.
    :return: Rounded value.
    :rtype: int or float

    MCLab Code Block:

        |round.png|

    MicroPython Code Block:

        .. code-block:: python

            rounded = round(2.4)

.. function:: int(value) -> int

    Convert a number or numeric string to an integer.

    :param value: Number or numeric string to convert.
    :type value: int or float or str
    :return: Integer value.
    :rtype: int

    MCLab Code Block:

        |to_int.png|

    MicroPython Code Block:

        .. code-block:: python

            count = int("12")

.. function:: float(value) -> float

    Convert a number or numeric string to a float.

    :param value: Number or numeric string to convert.
    :type value: int or float or str
    :return: Floating-point value.
    :rtype: float

    MCLab Code Block:

        |to_float.png|

    MicroPython Code Block:

        .. code-block:: python

            ratio = float("1.5")

.. function:: sum(iterable, start=0)

    Add the items of ``iterable`` from left to right.

    :param iterable: Values to add.
    :type iterable: iterable
    :param start: Value added to the running total.
    :return: Sum of the items.
    :rtype: int or float

    MCLab Code Block:

        |on_list.png|

    MicroPython Code Block:

        .. code-block:: python

            total = sum([1, 2, 3])

Random numbers
--------------

.. currentmodule:: random

.. function:: randint(a, b) -> int

    Return a random integer ``n`` such that ``a <= n <= b``.

    :param int a: Lower bound.
    :param int b: Upper bound.
    :return: Random integer in the inclusive range.
    :rtype: int

    MCLab Code Block:

        |random_int.png|

    MicroPython Code Block:

        .. code-block:: python

            import random

            value = random.randint(0, 255)

.. function:: random() -> float

    Return a random float in the half-open interval ``[0.0, 1.0)``.

    :return: Random fraction.
    :rtype: float

    MCLab Code Block:

        |random_float.png|

    MicroPython Code Block:

        .. code-block:: python

            fraction = random.random()

Constrain a value
-----------------

Clamp a value to an inclusive range by combining the ``min`` and ``max``
built-ins.

MCLab Code Block:

    |constrain.png|

MicroPython Code Block:

    .. code-block:: python

        value = 50
        bounded = max(1, min(value, 100))

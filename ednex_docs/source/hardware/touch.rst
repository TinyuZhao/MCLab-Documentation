.. _uiflow1-blockly-hardware-touch:

.. currentmodule:: MakerAndCoder

.. include:: ../refs/hardware.touch.ref

Touch
=====

The board ``touch`` object reports the latest touch coordinates and whether
the display is currently pressed.

MicroPython Examples
--------------------

Read touch state
^^^^^^^^^^^^^^^^

Open the |touch_example.m5f| project in MCLab.

This example prints the touch coordinate while the display is pressed.

MCLab Code Block:

    |touch_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/touch/touch_example.py
        :language: python

**API**
-------

.. function:: touch.read() -> tuple

    Return the latest touch coordinates.

    :return: Coordinate pair.
    :rtype: tuple

    MCLab Code Block:

        |read.png|

        |read_x.png|

        |read_y.png|

    MicroPython Code Block:

        .. code-block:: python

            x, y = touch.read()

.. function:: touch.status() -> bool

    Return whether the display is currently being touched.

    :return: ``True`` while pressed.
    :rtype: bool

    MCLab Code Block:

        |status.png|

    MicroPython Code Block:

        .. code-block:: python

            pressed = touch.status()

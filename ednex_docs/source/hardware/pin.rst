.. _uiflow1-blockly-hardware-pin:

.. currentmodule:: machine

.. include:: ../refs/hardware.pin.ref

Pin
===

``machine.Pin`` configures a GPIO and reads or drives its digital level.

MicroPython Examples
--------------------

Configure and drive a pin
^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |pin_example.m5f| project in MCLab.

This example configures pin 0 as an input with a pull-up and drives it high in a loop.

MCLab Code Block:

    |pin_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/pin/pin_example.py
        :language: python

**API**
-------

.. class:: Pin(id, mode=-1, pull=None, *, value=None)

    Configure a GPIO pin.

    :param int id: GPIO identifier.
    :param int mode: ``IN``, ``OUT`` or another supported pin mode.
    :param pull: Optional pull-up or pull-down selection.

    Options:

        - ``machine.Pin.IN``: Input mode.
        - ``machine.Pin.OUT``: Push-pull output mode.
        - ``machine.Pin.PULL_UP``: Enable pull-up.
        - ``machine.Pin.PULL_DOWN``: Enable pull-down.

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            pin0 = machine.Pin(2, mode=machine.Pin.OUT)

    .. method:: Pin.on() -> None

        Drive an output high.

        MCLab Code Block:

            |on.png|

        MicroPython Code Block:

            .. code-block:: python

                pin0.on()

    .. method:: Pin.off() -> None

        Drive an output low.

        MCLab Code Block:

            |off.png|

        MicroPython Code Block:

            .. code-block:: python

                pin0.off()

    .. method:: Pin.value(value=None)

        Read the digital level when called without an argument, or set it when
        passed 0 or 1.

        :param int value: Optional output level.
        :return: Current level when reading.
        :rtype: int

        MCLab Code Block:

            |set_value.png|

            |get_value.png|

        MicroPython Code Block:

            .. code-block:: python

                level = pin0.value()

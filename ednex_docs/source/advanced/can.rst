.. _uiflow1-blockly-advanced-can:

.. currentmodule:: machine

.. include:: ../refs/advanced.can.ref

CAN
===





The ``machine.CAN`` controller sends and receives CAN frames, manages filters, and exposes controller state and queue operations. The pins and bit rate in the example are the MCLab Blockly settings, not universal board defaults.

MicroPython Examples
--------------------

Send and receive CAN frames
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |can_example.m5f| project in MCLab.

This example configures a 25 kbit/s extended-frame CAN controller. Button A sends a frame, button B clears both queues, button C restarts the controller, and every received frame is shown on screen.

MCLab Code Block:

    |can_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/can/can_example.py
        :language: python

**API**
-------

CAN
---

.. class:: CAN(id:int, extframe:bool=True, mode:int=CAN.NORMAL, baudrate:int=CAN.BAUDRATE_25K, tx_io:int=17, rx_io:int=16, auto_restart:bool=False)

    Construct the ESP32 CAN controller.

    :param int id: CAN controller number.
    :param bool extframe: Enable extended identifiers.
    :param int mode: Controller operating mode.
    :param int baudrate: CAN bit rate.
    :param int tx_io: Transmit pin.
    :param int rx_io: Receive pin.
    :param bool auto_restart: Restart automatically after bus errors.

    Options:

        - ``CAN.NORMAL``: normal mode.
        - ``CAN.BAUDRATE_25K``: 25 kbit/s.

    MCLab Code Block:

        |can_init.png|

    MicroPython Code Block:

        .. code-block:: python

            from machine import CAN
            can = CAN(0, extframe=True, mode=CAN.NORMAL, baudrate=CAN.BAUDRATE_25K, tx_io=17, rx_io=16, auto_restart=False)

    .. method:: CAN.any() -> bool

        Report whether a received frame is available.

        MCLab Code Block:

            |can_any.png|

        MicroPython Code Block:

            .. code-block:: python

                can.any()

    .. method:: CAN.recv(list=None, *, timeout:int=5000) -> tuple

        Receive a frame as identifier, RTR flag, status, and data bytes. A supplied list must have at least four elements with a writable memoryview in its fourth slot.

        MCLab Code Block:

            |can_recv.png|

        MicroPython Code Block:

            .. code-block:: python

                frame = can.recv()

    .. method:: CAN.send(data, id:int, *, timeout:int=0, rtr:bool=False) -> None

        Transmit up to eight data bytes using the selected CAN identifier.

        MCLab Code Block:

            |can_send.png|

        MicroPython Code Block:

            .. code-block:: python

                can.send([0, 1, 2, 3, 4, 5, 6, 7], 0)

    .. method:: CAN.setfilter(bank:int, mode:int, params, *, rtr:bool=False) -> None

        Set a hardware filter; params must contain an identifier and mask.

        MCLab Code Block:

            |can_set_filter.png|

        MicroPython Code Block:

            .. code-block:: python

                can.setfilter(0, CAN.FILTER_RAW_SINGLE, [0, 0xFFFFFFFF])

    .. method:: CAN.clearfilter() -> None

        Clear the configured hardware filters.

        MCLab Code Block:

            |can_clearfilter.png|

        MicroPython Code Block:

            .. code-block:: python

                can.clearfilter()

    .. method:: CAN.state() -> int

        Return the current controller state.

        MCLab Code Block:

            |can_state.png|

        MicroPython Code Block:

            .. code-block:: python

                can.state()

    .. method:: CAN.clear_rx_queue() -> bool

        Clear pending received frames.

        MCLab Code Block:

            |can_clear_rx_queue.png|

        MicroPython Code Block:

            .. code-block:: python

                can.clear_rx_queue()

    .. method:: CAN.clear_tx_queue() -> bool

        Clear pending transmit frames.

        MCLab Code Block:

            |can_clear_tx_queue.png|

        MicroPython Code Block:

            .. code-block:: python

                can.clear_tx_queue()

    .. method:: CAN.restart() -> None

        Restart the CAN controller.

        MCLab Code Block:

            |can_restart.png|

        MicroPython Code Block:

            .. code-block:: python

                can.restart()

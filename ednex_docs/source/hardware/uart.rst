.. _uiflow1-blockly-hardware-uart:

.. currentmodule:: machine

.. include:: ../refs/hardware.uart.ref

UART
====

``machine.UART`` provides asynchronous serial communication. Configure the
port, then use stream methods to exchange bytes.

MicroPython Examples
--------------------

Read and write serial data
^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |uart_example.m5f| project in MCLab.

This example configures a UART port, writes a short string, and prints received data.

MCLab Code Block:

    |uart_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/uart/uart_example.py
        :language: python

**API**
-------

.. class:: UART(id, baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None)

    Create a UART port. Call :meth:`UART.init` to configure an existing port
    with explicit communication settings.

    :param int id: UART identifier.
    :param int baudrate: Baud rate.
    :param int bits: Number of data bits.
    :param parity: Parity selection or ``None``.
    :param int stop: Number of stop bits.
    :param tx: Optional transmit GPIO.
    :param rx: Optional receive GPIO.

    MCLab Code Block:

        |init.png|

        |init_pins.png|

    MicroPython Code Block:

        .. code-block:: python

            uart1 = machine.UART(1, tx=1, rx=3)
            uart1.init(115200, bits=8, parity=None, stop=1)

    .. method:: UART.write(buf) -> int

        Write bytes or a string to the transmit buffer.

        :param buf: Data to send.
        :type buf: bytes or str
        :return: Number of bytes written.
        :rtype: int

        MCLab Code Block:

            |write.png|

            |write_raw_data.png|

        MicroPython Code Block:

            .. code-block:: python

                uart1.write(b"hello\r\n")

    .. method:: UART.read(nbytes=-1)

        Read available bytes, optionally limiting the number of bytes.

        :param int nbytes: Maximum number of bytes, or -1 for available data.
        :return: Bytes read, or ``None`` when no data is available.
        :rtype: bytes or None

        MCLab Code Block:

            |read.png|

            |read_characters.png|

        MicroPython Code Block:

            .. code-block:: python

                data = uart1.read(10)

    .. method:: UART.readline()

        Read through the next newline and return the line bytes.

        :return: A line of bytes, or ``None`` when unavailable.
        :rtype: bytes or None

        MCLab Code Block:

            |readline.png|

        MicroPython Code Block:

            .. code-block:: python

                line = uart1.readline()

    .. method:: UART.any() -> int

        Return the number of bytes waiting in the receive buffer.

        :return: Number of bytes available.
        :rtype: int

        MCLab Code Block:

            |any.png|

        MicroPython Code Block:

            .. code-block:: python

                if uart1.any():
                    data = uart1.read()

    .. method:: UART.deinit() -> None

        Deinitialize the UART port and release its resources.

        MicroPython Code Block:

            .. code-block:: python

                uart1.deinit()

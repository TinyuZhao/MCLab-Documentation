.. _uiflow1-blockly-hardware-spi:

.. currentmodule:: machine

.. include:: ../refs/hardware.spi.ref

SPI
===

``machine.SPI`` provides synchronous serial transfers using clock, input and
output pins.

**API**
-------

.. class:: SPI(id, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None)

    Construct an SPI bus with the selected clock and data pins.

    :param int id: SPI controller identifier.
    :param int baudrate: Clock rate in hertz.
    :param int polarity: Clock polarity.
    :param int phase: Clock phase.
    :param int bits: Bits per transfer.
    :param int firstbit: Bit order.
    :param sck: Clock pin.
    :param mosi: Master-out pin.
    :param miso: Master-in pin.

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            spi = machine.SPI(1, 500000, sck=machine.Pin(18),
                              miso=machine.Pin(19), mosi=machine.Pin(23))

    .. method:: SPI.write(buf) -> int

        Write bytes to the SPI bus.

        :param buf: Buffer to send.
        :return: Number of bytes written.
        :rtype: int

        MCLab Code Block:

            |write.png|

        MicroPython Code Block:

            .. code-block:: python

                spi.write(b"hello")

    .. method:: SPI.read(nbytes, write=0) -> bytes

        Read bytes from the SPI bus.

        :param int nbytes: Number of bytes to read.
        :param int write: Optional byte value sent while reading.
        :return: Received bytes.
        :rtype: bytes

        MCLab Code Block:

            |read.png|

            |readinto.png|

        MicroPython Code Block:

            .. code-block:: python

                data = spi.read(4)

    .. method:: SPI.write_readinto(write_buf, read_buf) -> None

        Transfer while writing and reading into separate buffers.

        :param write_buf: Bytes to send.
        :param read_buf: Writable receive buffer.

        MCLab Code Block:

            |write_readinto.png|

        MicroPython Code Block:

            .. code-block:: python

                spi.write_readinto(b"abcd", bytearray(4))

    .. method:: SPI.deinit() -> None

        Release the SPI bus.

        MCLab Code Block:

            |deinit.png|

        MicroPython Code Block:

            .. code-block:: python

                spi.deinit()

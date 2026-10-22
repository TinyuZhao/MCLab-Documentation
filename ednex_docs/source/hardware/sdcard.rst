.. _uiflow1-blockly-hardware-sdcard:

.. currentmodule:: hardware.sdcard

.. include:: ../refs/hardware.sdcard.ref

SDCard
======

The ``hardware.sdcard.SDCard`` helper mounts the board SD card at ``/sd`` using the selected bus frequency. Files are then accessed with standard MicroPython file and ``os`` APIs.

MicroPython Examples
--------------------

Read a file from the card
^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |sdcard_example.m5f| project in MCLab.

This example mounts the SD card and prints the contents of a file.

MCLab Code Block:

    |sdcard_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/sdcard/sdcard_example.py
        :language: python

**API**
-------

.. function:: SDCard(freq) -> None

    Mount the SD card at ``/sd`` using the requested bus frequency.

    :param int freq: SD-card bus frequency in hertz.

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            from hardware import sdcard
            sdcard.SDCard(20000000)

.. function:: open(path, mode)

    Open a file on the mounted SD-card filesystem. Standard MicroPython modes
    such as ``r``, ``w``, ``a``, and their ``+`` variants apply.

    MCLab Code Block:

        |open.png|

    MicroPython Code Block:

        .. code-block:: python

            with open("/sd/test.txt", "r") as fs:
                data = fs.read()

.. function:: os.listdir(path)

    List directory entries below the mounted SD-card path.

    MCLab Code Block:

        |listdir.png|

    MicroPython Code Block:

        .. code-block:: python

            print(os.listdir("/sd"))

.. function:: os.mkdir(path)

    Create a directory on the mounted SD-card filesystem.

    MCLab Code Block:

        |mkdir.png|

    MicroPython Code Block:

        .. code-block:: python

            os.mkdir("/sd/new")

.. function:: os.remove(path)

    Remove a file from the mounted SD-card filesystem.

    MCLab Code Block:

        |remove.png|

    MicroPython Code Block:

        .. code-block:: python

            os.remove("/sd/test.txt")

.. function:: os.rmdir(path)

    Remove an empty directory from the mounted SD-card filesystem.

    MCLab Code Block:

        |rmdir.png|

    MicroPython Code Block:

        .. code-block:: python

            os.rmdir("/sd/new")

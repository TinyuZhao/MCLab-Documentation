.. _uiflow1-blockly-advanced-socket:

.. currentmodule:: socket

.. include:: ../refs/advanced.socket.ref

Socket
======





The MicroPython ``socket`` module creates TCP or UDP sockets for network send and receive operations.

MicroPython Examples
--------------------

Send UDP datagrams
^^^^^^^^^^^^^^^^^^

Open the |socket_udp_client.m5f| project in MCLab.

This example opens a UDP socket and sends a datagram to a fixed address and port in a loop.

MCLab Code Block:

    |socket_udp_client.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/socket/socket_udp_client.py
        :language: python

Receive UDP datagrams
^^^^^^^^^^^^^^^^^^^^^

Open the |socket_udp_server.m5f| project in MCLab.

This example connects Wi-Fi, binds UDP port 5000, and prints every datagram it receives.

MCLab Code Block:

    |socket_udp_server.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/socket/socket_udp_server.py
        :language: python

**API**
-------

The firmware socket interface provides TCP and UDP transport.

.. class:: socket(family:int=AF_INET, type:int=SOCK_STREAM)

    Create a socket with address family and transport type.

    MCLab Code Block:

        |udp_client_start.png|

    MicroPython Code Block:

        .. code-block:: python

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

.. method:: socket.bind(address) -> None

    Bind a socket to a local address and port.

    MCLab Code Block:

        |udp_server_start.png|

    MicroPython Code Block:

        .. code-block:: python

            sock.bind(("0.0.0.0", 5000))

.. method:: socket.recv(bufsize:int) -> bytes

    Read at most bufsize bytes from a connected socket.

    MCLab Code Block:

        |udp_server_recv.png|

    MicroPython Code Block:

        .. code-block:: python

            data = sock.recv(1024)

.. method:: socket.sendto(data:bytes, address) -> int

    Send UDP data to an address.

    MCLab Code Block:

        |udp_client_sendto.png|

    MicroPython Code Block:

        .. code-block:: python

            sock.sendto(data, ("192.168.1.10", 5000))

.. method:: socket.close() -> None

    Close the socket and release its resources.

    MCLab Code Block:

        |udp_client_close.png|

    MicroPython Code Block:

        .. code-block:: python

            sock.close()

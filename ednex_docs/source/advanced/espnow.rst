.. _uiflow1-blockly-advanced-espnow:

.. currentmodule:: libs.mc_espnow

.. include:: ../refs/libs.mc_espnow.ref

ESP-NOW
========


The ``MCESPNOW`` class exposes peer management, callbacks, and data transfer for ESP-NOW workflows.

MicroPython Examples
--------------------

Send ESP-NOW data
^^^^^^^^^^^^^^^^^

Open the |espnow_send.m5f| project in MCLab.

This example initializes ESP-NOW, looks up the peer named ``M5_Slave``, and sends an incrementing counter once per second after button A starts it. Button C stops the loop and the send callback counts successful transmissions.

MCLab Code Block:

    |espnow_send.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/espnow/espnow_send.py
        :language: python

Receive ESP-NOW data
^^^^^^^^^^^^^^^^^^^^

Open the |espnow_received.m5f| project in MCLab.

This example receives ESP-NOW packets in a callback and shows the sender MAC address and payload.

MCLab Code Block:

    |espnow_received.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/espnow/espnow_received.py
        :language: python

**API**
-------

.. automodule:: libs.mc_espnow
    :members:
    :exclude-members: MCESPNOW

.. autoclass:: MCESPNOW
    :members: espnow_init, espnow_add_peer, espnow_send_data, espnow_broadcast_data, espnow_set_pmk, espnow_send_cb, espnow_recv_cb, espnow_recv_str, espnow_get_mac, espnow_scan, espnow_set_ap, espnow_deinit
    :member-order: bysource

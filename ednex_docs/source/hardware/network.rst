.. _uiflow1-blockly-hardware-network:

.. currentmodule:: wifiCfg

.. include:: ../refs/wifiCfg.ref

Network
=======

The ``wifiCfg`` helpers connect the board's station interface to a Wi-Fi
network and expose the underlying ``network.WLAN`` status methods.

MicroPython Examples
--------------------

Connect to Wi-Fi
^^^^^^^^^^^^^^^^

Open the |network_example.m5f| project in MCLab.

This example connects the board to a Wi-Fi network.

MCLab Code Block:

    |network_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/network/network_example.py
        :language: python

**API**
-------

.. currentmodule:: wifiCfg

.. automodule:: wifiCfg
    :members:
    :member-order: bysource

Wi-Fi interface
---------------

The Wi-Fi blocks also drive the firmware's ``network`` module directly. The
station object is usually obtained from ``wifiCfg``, but it can be created
here as well.

.. currentmodule:: network

.. class:: WLAN(interface)

    Create a Wi-Fi interface.

    :param int interface: Interface to create.

    Options:

        - ``network.STA_IF``: Station interface.
        - ``network.AP_IF``: Access-point interface.

    MCLab Code Block:

        |wlan_create_station.png|

    MicroPython Code Block:

        .. code-block:: python

            wlan = network.WLAN(network.STA_IF)

    .. method:: WLAN.active(is_active=None)

        Enable or disable the interface.

        :param bool is_active: ``True`` activates the interface, ``False``
                               deactivates it.

        MCLab Code Block:

            |wlan_active.png|

        MicroPython Code Block:

            .. code-block:: python

                wlan.active(True)

    .. method:: WLAN.connect(ssid, key=None)

        Join a network. The call returns before the connection is complete;
        poll :meth:`isconnected` or :meth:`status` for the result.

        :param str ssid: Network name.
        :param str key: Network password, or ``None`` for an open network.

        MCLab Code Block:

            |wlan_connect.png|

        MicroPython Code Block:

            .. code-block:: python

                wlan.connect('ssid', 'password')

    .. method:: WLAN.disconnect()

        Leave the current network.

        MCLab Code Block:

            |disconnect.png|

        MicroPython Code Block:

            .. code-block:: python

                wlan.disconnect()

    .. method:: WLAN.isconnected()

        :returns: ``True`` when the station has a connection.
        :rtype: bool

        MCLab Code Block:

            |wlan_isconnected.png|

        MicroPython Code Block:

            .. code-block:: python

                if wlan.isconnected():
                    print('online')

    .. method:: WLAN.scan()

        :returns: One tuple per access point found: ``(ssid, bssid, channel,
                  rssi, security, hidden)``.
        :rtype: list

        MCLab Code Block:

            |wlan_scan.png|

        MicroPython Code Block:

            .. code-block:: python

                for network_info in wlan.scan():
                    print(network_info[0])

    .. method:: WLAN.status()

        :returns: The connection status code.
        :rtype: int

        MCLab Code Block:

            |wlan_status.png|

            |wlan_state_define.png|

        MicroPython Code Block:

            .. code-block:: python

                print(wlan.status())

    .. method:: WLAN.ifconfig(config=None)

        Read or write the interface addresses. The block reads the addresses;
        writing accepts a four-item tuple.

        :param tuple config: ``(ip, netmask, gateway, dns)`` to set, or
                             ``None`` to read the current values.

        :returns: The current ``(ip, netmask, gateway, dns)`` tuple when
                  ``config`` is ``None``.
        :rtype: tuple or None

        MCLab Code Block:

            |wlan_ifconfig.png|

        MicroPython Code Block:

            .. code-block:: python

                print(wlan.ifconfig())

    .. method:: WLAN.config(param=None, **kwargs)

        Read one interface setting, or configure the access point. The block
        reads a single setting by name; the access-point form sets the name,
        password and authentication mode.

        :param str param: Name of the setting to read, for example ``'mac'``.
        :param dict \*\*kwargs: Settings to write, such as ``essid``,
                              ``password`` and ``authmode``.

        MCLab Code Block:

            |wlan_config.png|

            |wlan_config_ap.png|

        MicroPython Code Block:

            .. code-block:: python

                print(wlan.config('mac'))

SmartConfig
-----------

SmartConfig receives the network name and password from a phone application.

.. currentmodule:: smartconfig

.. function:: set_type(type)

    Select the SmartConfig protocol used by :func:`start`.

    :param int type: Protocol to use.

    Options:

        - ``smartconfig.ESPTOUCH``: ESPTouch protocol.
        - ``smartconfig.AIRKISS``: AirKiss protocol.
        - ``smartconfig.ESPTOUCH_AIRKISS``: Try both protocols.

    MCLab Code Block:

        |smartconfig_set_type.png|

    MicroPython Code Block:

        .. code-block:: python

            smartconfig.set_type(smartconfig.ESPTOUCH)

.. function:: start()

    Start listening for the configuration sent by the phone application.

    MCLab Code Block:

        |smartconfig_start.png|

    MicroPython Code Block:

        .. code-block:: python

            smartconfig.start()

.. function:: stop()

    Stop listening for configuration data.

    MCLab Code Block:

        |smartconfig_stop.png|

    MicroPython Code Block:

        .. code-block:: python

            smartconfig.stop()

.. function:: status()

    :returns: The SmartConfig status code.
    :rtype: int

    MCLab Code Block:

        |smartconfig_status.png|

        |smartconfig_state_define.png|

    MicroPython Code Block:

        .. code-block:: python

            print(smartconfig.status())

.. function:: get_ssid()

    :returns: The network name received from the phone application.
    :rtype: str

    MCLab Code Block:

        |smartconfig_get_ssid.png|

    MicroPython Code Block:

        .. code-block:: python

            print(smartconfig.get_ssid())

.. function:: get_password()

    :returns: The network password received from the phone application.
    :rtype: str

    MCLab Code Block:

        |smartconfig_get_password.png|

    MicroPython Code Block:

        .. code-block:: python

            print(smartconfig.get_password())

.. function:: get_phoneip()

    :returns: The address of the phone application that sent the configuration.
    :rtype: str

    MCLab Code Block:

        |smartconfig_get_phoneip.png|

    MicroPython Code Block:

        .. code-block:: python

            print(smartconfig.get_phoneip())

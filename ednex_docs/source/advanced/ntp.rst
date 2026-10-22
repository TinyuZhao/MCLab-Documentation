.. _uiflow1-blockly-advanced-ntp:

.. currentmodule:: ntptime

.. include:: ../refs/advanced.ntp.ref

NTP
===





The ``ntptime.client`` synchronizes the local RTC with an NTP server and formats date and time values. Its source requires Wi-Fi connectivity.

MicroPython Examples
--------------------

Read network time
^^^^^^^^^^^^^^^^^

Open the |ntp_example.m5f| project in MCLab.

This example connects to an NTP server, then prints the formatted date and time and the Unix timestamp once per second.

MCLab Code Block:

    |ntp_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/ntp/ntp_example.py
        :language: python

**API**
-------

NTP Client
----------

.. class:: client(host='cn.pool.ntp.org', timezone=8)

    Create an NTP client and synchronize the RTC using the configured server and timezone.

    MCLab Code Block:

        |init_timezone.png|


    MicroPython Code Block:

        .. code-block:: python

            from ntptime import client
            service = client()

    .. method:: client.getTimestamp()

        Return the current Unix timestamp, refreshing from the NTP server when needed.

        MCLab Code Block:

            |getTimestamp.png|


        MicroPython Code Block:

            .. code-block:: python

                service.getTimestamp()

    .. method:: client.updateTime()

        Refresh the RTC when the local time is stale.

        MicroPython Code Block:

            .. code-block:: python

                service.updateTime()

    .. method:: client.printtime()

        Print the current date and time.

        MicroPython Code Block:

            .. code-block:: python

                service.printtime()

    .. method:: client.formatDate(c='-')

        Return the current date with the selected delimiter.

        MCLab Code Block:

            |formatDate.png|


        MicroPython Code Block:

            .. code-block:: python

                service.formatDate()

    .. method:: client.formatTime(c=':')

        Return the current time with the selected delimiter.

        MCLab Code Block:

            |formatTime.png|


        MicroPython Code Block:

            .. code-block:: python

                service.formatTime()

    .. method:: client.formatDatetime(c1='-', c2=':')

        Return the date and time with their selected delimiters.

        MCLab Code Block:

            |formatDatetime.png|


        MicroPython Code Block:

            .. code-block:: python

                service.formatDatetime()

    .. method:: client.year()

        Return the year.

        MCLab Code Block:

            |year.png|


        MicroPython Code Block:

            .. code-block:: python

                service.year()

    .. method:: client.month()

        Return the month.

        MCLab Code Block:

            |month.png|


        MicroPython Code Block:

            .. code-block:: python

                service.month()

    .. method:: client.day()

        Return the day of the month.

        MCLab Code Block:

            |day.png|


        MicroPython Code Block:

            .. code-block:: python

                service.day()

    .. method:: client.hour()

        Return the hour.

        MCLab Code Block:

            |hour.png|


        MicroPython Code Block:

            .. code-block:: python

                service.hour()

    .. method:: client.minute()

        Return the minute.

        MCLab Code Block:

            |minute.png|


        MicroPython Code Block:

            .. code-block:: python

                service.minute()

    .. method:: client.second()

        Return the second.

        MCLab Code Block:

            |second.png|


        MicroPython Code Block:

            .. code-block:: python

                service.second()

    .. method:: client.weekday()

        Return the weekday abbreviation.

        MCLab Code Block:

            |weekday.png|


        MicroPython Code Block:

            .. code-block:: python

                service.weekday()

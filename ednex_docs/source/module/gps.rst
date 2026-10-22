.. currentmodule:: modules._gps

GPS Module
==========

.. include:: ../refs/modules._gps.ref

This page documents the public API for the gps driver.

MicroPython Examples
--------------------

Read GPS Position Data
^^^^^^^^^^^^^^^^^^^^^^

Open the |gps_example.m5f| project in MCLab.

This example sets the GPS time zone to 8 and continuously prints the time, date, latitude, longitude, and altitude.

MCLab Code Block:

    |gps_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/module/gps/gps_example.py
        :language: python

**API**
-------

.. currentmodule:: modules._gps

.. automodule:: modules._gps
    :members:
    :member-order: bysource

Position and time fields
------------------------

The blocks read the values the decoders store on the object. Each field below is filled by the
sentence named in its description.

.. currentmodule:: modules._gps

.. attribute:: Gps.latitude

    Latitude as encoded in the position sentence, for example ``2242.10772N``. Set by :meth:`decode_gga`.

    MCLab Code Block:

        |get_latitude.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.latitude)

.. attribute:: Gps.longitude

    Longitude as encoded in the position sentence. Set by :meth:`decode_gga`.

    MCLab Code Block:

        |get_longitude.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.longitude)

.. attribute:: Gps.latitude_decimal

    Latitude in decimal degrees, negative for the southern hemisphere. Set by :meth:`decode_gga`.

    MCLab Code Block:

        |get_latitude_decimal.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.latitude_decimal)

.. attribute:: Gps.longitude_decimal

    Longitude in decimal degrees, negative for the western hemisphere. Set by :meth:`decode_gga`.

    MCLab Code Block:

        |get_longitude_decimal.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.longitude_decimal)

.. attribute:: Gps.altitude

    Altitude in metres, as reported by the position sentence. Set by :meth:`decode_gga`.

    MCLab Code Block:

        |get_altitude.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.altitude)

.. attribute:: Gps.satellite_num

    Number of satellites used for the fix. Set by :meth:`decode_gga`.

    MCLab Code Block:

        |get_satellite_num.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.satellite_num)

.. attribute:: Gps.pos_quality

    Fix quality reported by the position sentence; ``'0'`` means no fix. Set by :meth:`decode_gga`.

    MCLab Code Block:

        |get_positioning_quality.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.pos_quality)

.. attribute:: Gps.course

    Course over ground in degrees. Set by :meth:`decode_vtg`.

    MCLab Code Block:

        |get_course.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.course)

.. attribute:: Gps.speed_kph

    Speed over ground in kilometres per hour. Set by :meth:`decode_vtg`.

    MCLab Code Block:

        |get_speed.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.speed_kph)

.. attribute:: Gps.speed_knot

    Speed over ground in knots. Set by :meth:`decode_vtg`.

    MCLab Code Block:

        |speed_knot.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.speed_knot)

.. attribute:: Gps.gps_date

    Date of the last fix as ``MM/DD/YY``. Set by :meth:`decode_rmc`.

    MCLab Code Block:

        |get_date.png|

    MicroPython Code Block:

        .. code-block:: python

            print(gps.gps_date)

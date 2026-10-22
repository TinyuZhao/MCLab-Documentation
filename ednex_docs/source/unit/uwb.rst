.. currentmodule:: units._uwb

UWB Unit
========

.. include:: ../refs/units._uwb.ref

This page documents the public API for the uwb driver.

MicroPython Examples
--------------------

.. Reserve one complete subsection for each example. Keep the MCLab project,
   description, MCLab Code Block, and MicroPython Code Block together.

Anchor Example
^^^^^^^^^^^^^^

Open the |uwb_anchor_example.m5f| project in MCLab.

This example configures the UWB unit as an anchor.

MCLab Code Block:

    |uwb_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/unit/uwb/uwb_anchor_example.py
        :language: python

Tag Example
^^^^^^^^^^^

Open the |uwb_tag_example.m5f| project in MCLab.

This example configures the UWB unit as a tag.

MCLab Code Block:

    |uwb_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/unit/uwb/uwb_tag_example.py
        :language: python

**API**
-------

.. currentmodule:: units._uwb

.. automodule:: units._uwb
    :members:
    :member-order: bysource


Positioning fields
------------------

The ranging values are read from the object's attributes.

.. currentmodule:: units._uwb

.. attribute:: Uwb.device_id

    Identifier reported by the module, for example the tag address read before continuous ranging.

    MCLab Code Block:

        |get_device_id.png|

    MicroPython Code Block:

        .. code-block:: python

            print(uwb.device_id)

.. attribute:: Uwb.get_distance_measure

    Distances measured for each tag, in metres, as a four-element list. :meth:`update_new_value_loop` fills it while continuous output is running.

    MCLab Code Block:

        |get_distance_measure.png|

    MicroPython Code Block:

        .. code-block:: python

            print(uwb.get_distance_measure[0])

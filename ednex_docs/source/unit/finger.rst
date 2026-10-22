.. currentmodule:: units._finger

Finger Unit
===========

.. include:: ../refs/units._finger.ref

This page documents the public API for the finger driver.

MicroPython Examples
--------------------

Enroll and Authenticate Fingerprints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |finger_example.m5f| project in MCLab.

This example adds or removes a fingerprint user with buttons A and B, updates the displayed state, and indicates successful recognition with the RGB LED.

MCLab Code Block:

    |finger_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/unit/finger/finger_example.py
        :language: python

**API**
-------

.. currentmodule:: units._finger

.. automodule:: units._finger
    :members:
    :member-order: bysource


Operation fields
----------------

The fingerprint operations store their results on the object.

.. currentmodule:: units._finger

.. attribute:: Finger.state

    Result of the most recent fingerprint operation as text, for example ``'Add user success'``, ``'Delete user finish'`` or ``'Got a known finger'``.

    MCLab Code Block:

        |state.png|

    MicroPython Code Block:

        .. code-block:: python

            print(finger.state)

.. attribute:: Finger.user_id_add

    User identifier used when a fingerprint is added with :meth:`addUser`.

    MCLab Code Block:

        |id.png|

    MicroPython Code Block:

        .. code-block:: python

            finger.user_id_add = 1

.. attribute:: Finger.access_add

    Access level used when a fingerprint is added with :meth:`addUser`.

    MCLab Code Block:

        |access.png|

    MicroPython Code Block:

        .. code-block:: python

            finger.access_add = 1

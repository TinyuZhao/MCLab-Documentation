.. _uiflow1-blockly-hardware-speaker:

.. currentmodule:: hardware.speaker

.. include:: ../refs/hardware.speaker.ref

Speaker
=======

``hardware.speaker.Speaker`` generates tones and plays WAV audio through the
board speaker. The startup singleton is exposed as ``speaker``.

MicroPython Examples
--------------------

Play a tone
^^^^^^^^^^^

Open the |speaker_example.m5f| project in MCLab.

This example plays two short tones through the board speaker.

MCLab Code Block:

    |speaker_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/speaker/speaker_example.py
        :language: python

**API**
-------

.. currentmodule:: hardware.speaker

.. automodule:: hardware.speaker
    :members:
    :member-order: bysource

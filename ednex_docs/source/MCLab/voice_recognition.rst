.. currentmodule:: MCLab.ai_tools

Voice Recognition
=================

.. include:: ../refs/MCLab.voice_recognition.ref

``MCLab.ai_tools`` provides voice recognition commands, wake-up status, and
voice recognition callbacks.

MicroPython Examples
--------------------

Voice recognition
^^^^^^^^^^^^^^^^^

Open the |voice_recognition.m5f| project in MCLab.

This example listens for wake-up words and voice commands, then displays the
recognized command and changes the screen or RGB output for selected commands.

MCLab Code Block:

    |voice_recognition_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/voice_recognition/voice_recognition.py
        :language: python
        :linenos:

**API**
-------

.. automodule:: MCLab.ai_tools
    :members:
    :exclude-members: FaceDetect, ColorDetect, ColorTrack, QRCode, BarCode, MotionDetect, TrafficSignal
    :member-order: bysource
    :no-index:

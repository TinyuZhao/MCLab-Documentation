.. currentmodule:: MCLab.ai_tools

AI Camera V1
============

.. include:: ../refs/MCLab.ai_camera_v1.ref

``MCLab.ai_tools`` provides the AI Camera V1 functions for face, color,
QR-code, barcode, motion, and traffic-signal detection.

MicroPython Examples
--------------------

Find faces
^^^^^^^^^^

Open the |ai_camera_v1_find_faces.m5f| project in MCLab.

This example initializes face detection and displays the first detected face.

MCLab Code Block:

    |ai_camera_v1_find_faces.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v1/ai_camera_v1_find_faces.py
        :language: python
        :linenos:

Get barcode
^^^^^^^^^^^

Open the |ai_camera_v1_get_barcode.m5f| project in MCLab.

This example displays the latest barcode text returned by the camera.

MCLab Code Block:

    |ai_camera_v1_get_barcode.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v1/ai_camera_v1_get_barcode.py
        :language: python
        :linenos:

Get color
^^^^^^^^^

Open the |ai_camera_v1_get_color.m5f| project in MCLab.

This example displays the detected color value.

MCLab Code Block:

    |ai_camera_v1_get_color.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v1/ai_camera_v1_get_color.py
        :language: python
        :linenos:

Get motion rate
^^^^^^^^^^^^^^^

Open the |ai_camera_v1_get_motion_rate.m5f| project in MCLab.

This example displays the motion-detection rate reported by the camera.

MCLab Code Block:

    |ai_camera_v1_get_motion_rate.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v1/ai_camera_v1_get_motion_rate.py
        :language: python
        :linenos:

Get QR code
^^^^^^^^^^^

Open the |ai_camera_v1_get_qrcode.m5f| project in MCLab.

This example displays the decoded QR-code version and content.

MCLab Code Block:

    |ai_camera_v1_get_qrcode.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v1/ai_camera_v1_get_qrcode.py
        :language: python
        :linenos:

Get traffic signal
^^^^^^^^^^^^^^^^^^^

Open the |ai_camera_v1_get_traffic_signal.m5f| project in MCLab.

This example displays the detected traffic-signal result.

MCLab Code Block:

    |ai_camera_v1_get_traffic_signal.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v1/ai_camera_v1_get_traffic_signal.py
        :language: python
        :linenos:

**API**
-------

.. automodule:: MCLab.ai_tools
    :members:
    :exclude-members: VoiceRecognize
    :member-order: bysource

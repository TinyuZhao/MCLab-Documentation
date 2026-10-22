.. currentmodule:: MCLab.ai_camera

AI Camera V2
=============

.. include:: ../refs/MCLab.ai_camera_v2.ref

``AiCamera`` provides recognition-mode selection, result queries, learning
commands, and fill-light control for the MCLab AI Camera.

MicroPython Examples
--------------------

Get color
^^^^^^^^^

Open the |ai_camera_v2_get_color.m5f| project in MCLab.

This example initializes the AI Camera and displays its detected RGB values
when the on-screen button is pressed.

MCLab Code Block:

    |ai_camera_v2_get_color_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_get_color.py
        :language: python
        :linenos:

Find face
^^^^^^^^^

Open the |ai_camera_v2_find_face.m5f| project in MCLab.

This example displays the position and size of the first detected face.

MCLab Code Block:

    |ai_camera_v2_find_face_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_find_face.py
        :language: python
        :linenos:

Find recognized face
^^^^^^^^^^^^^^^^^^^^

Open the |ai_camera_v2_find_recongized_face.m5f| project in MCLab.

This example starts face learning and displays the recognized face ID and
location.

MCLab Code Block:

    |ai_camera_v2_find_recongized_face_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_find_recongized_face.py
        :language: python
        :linenos:

Scan QR code
^^^^^^^^^^^^

Open the |ai_camera_v2_scan_qrcode.m5f| project in MCLab.

This example displays the decoded QR code and its location.

MCLab Code Block:

    |ai_camera_v2_scan_qrcode_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_scan_qrcode.py
        :language: python
        :linenos:

Track color
^^^^^^^^^^^

Open the |ai_camera_v2_track_color.m5f| project in MCLab.

This example tracks the selected color and displays its location.

MCLab Code Block:

    |ai_camera_v2_track_color_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_track_color.py
        :language: python
        :linenos:

Track lines
^^^^^^^^^^^

Open the |ai_camera_v2_track_lines.m5f| project in MCLab.

This example displays the position and size of a detected line.

MCLab Code Block:

    |ai_camera_v2_track_lines_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_track_lines.py
        :language: python
        :linenos:

Track objects
^^^^^^^^^^^^^

Open the |ai_camera_v2_track_objects.m5f| project in MCLab.

This example displays the ID and location of a detected object.

MCLab Code Block:

    |ai_camera_v2_track_objects_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_track_objects.py
        :language: python
        :linenos:

Track tag
^^^^^^^^^

Open the |ai_camera_v2_track_tag.m5f| project in MCLab.

This example displays the ID, rotation, and location of a detected tag.

MCLab Code Block:

    |ai_camera_v2_track_tag_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/ai_camera_v2/ai_camera_v2_track_tag.py
        :language: python
        :linenos:

**API**
-------

.. autoclass:: MCLab.ai_camera.AiCamera
    :members:
    :member-order: bysource

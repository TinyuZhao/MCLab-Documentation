.. _uiflow1-blockly-ui-image:

.. currentmodule:: ui.image

.. include:: ../refs/ui.image.ref

Image
=====

``MCImg`` displays a local or network image.

MicroPython Examples
--------------------

Show and Move an Image
^^^^^^^^^^^^^^^^^^^^^^

Open the |image_example.m5f| project in MCLab.

This example shows an image, then moves it to the top-left corner.

MCLab Code Block:

    |image_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/ui/image/image_example.py
        :language: python

**API**
-------

.. automodule:: ui.image
    :members:
    :exclude-members: set_pos
    :member-order: bysource

.. method:: MCImg.set_pos(x, y)

    Move the image to an absolute position.

    :param int x: Horizontal position in pixels.
    :param int y: Vertical position in pixels.

    MCLab Code Block:

        |set_pos.png|

        |set_position_x.png|

        |set_position_y.png|

    MicroPython Code Block:

        .. code-block:: python

            image.set_pos(0, 0)

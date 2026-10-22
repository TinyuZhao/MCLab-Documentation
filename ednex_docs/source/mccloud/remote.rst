.. _uiflow1-blockly-mccloud-remote:

.. currentmodule:: uiflow

.. include:: ../refs/mccloud.remote.ref

Remote
======

The Remote group builds a control page for the device on the MC Cloud service.
The page is created in the MCLab online editor and stored with the device API
key, so it keeps a fixed address that can be opened or shared. Every control
generates a callback in the program, and the label, image, gauge, and chart
controls also read data back from the device or from Ezdata.

MicroPython Examples
--------------------

Remote control page
^^^^^^^^^^^^^^^^^^^

Open the |remote_example.m5f| project in MCLab.

This example displays the Remote page QR code and registers callbacks for the
button, switch, slider, stepper, label, joystick, input, image, and gauge
controls.

MCLab Code Block:

    |remote_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/mccloud/remote/remote_example.py
        :language: python

**API**
-------

QR code
-------

.. function:: remoteInit() -> None

    Initialize the remote service before the control page URL is displayed.

    MicroPython Code Block:

        .. code-block:: python

            remoteInit()

.. function:: lcd.qrcode(url:str, x:int, y:int, size:int) -> None

    Display the URL of the generated control page as a QR code. The ``remote``
    parameter of the URL is filled in after the page is created, so run the
    program once in MCLab online mode before using the fixed link.

    :param url: URL supplied by the online editor.
    :type url: str
    :param x: Left display position.
    :type x: int
    :param y: Top display position.
    :type y: int
    :param size: QR code size in pixels.
    :type size: int

    MCLab Code Block:

        |set_qrcode.png|

    MicroPython Code Block:

        .. code-block:: python

            lcd.qrcode('http://mclab.ai/remote?id=undefined', 72, 32, 176)

.. note::

    This function requires the online version of MCLab. When the program is
    downloaded and run offline, add the Wi-Fi connection code to ``setup``, and
    push the program once before reading the page QR code or URL.

Button
------

.. function:: button_1_callback() -> None

    Run when the first button control is pressed. A callback is generated for
    each button added to the page.

    The properties set the title text and whether it is shown, the title color
    and background, the edge style (sharp or pill), and the fill style (outline
    or solid).

    MCLab Code Block:

        |button_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def button_1_callback():
              print('Button Press')

Switch
------

.. function:: switch_1_callback(switch_value:int) -> None

    Run when the first switch control changes. A callback is generated for each
    switch added to the page.

    :param switch_value: Switch state, ``1`` for on and ``0`` for off.
    :type switch_value: int

    The properties set the title text and whether it is shown, the off and on
    labels, the off and on font colors, and the off and on background colors.

    MCLab Code Block:

        |switch_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def switch_1_callback(switch_value):
              print(switch_value)

Slider
------

.. function:: slider_1_callback(slider_value:int) -> None

    Run when the first slider control changes. A callback is generated for each
    slider added to the page.

    :param slider_value: Current slider position.
    :type slider_value: int

    The properties set the title text and whether it is shown, whether the
    current value is displayed, the slider color, and the minimum and maximum
    values.

    MCLab Code Block:

        |slider_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def slider_1_callback(slider_value):
              print(slider_value)

Stepper
-------

.. function:: stepper_1_callback(stepper_value:int) -> None

    Run when the first stepper control changes. A callback is generated for
    each stepper added to the page.

    :param stepper_value: Current stepper value.
    :type stepper_value: int

    The properties set the title text and whether it is shown, the minimum and
    maximum values, and the step applied for each click.

    MCLab Code Block:

        |stepper_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def stepper_1_callback(stepper_value):
              print(stepper_value)

Label
-----

.. function:: label_1_callback() -> str

    Return the value displayed by the first label control. The callback runs at
    the configured interval (3000 ms by default) and its return value is
    uploaded and shown on the page.

    :return: Value shown by the label control.
    :rtype: str

    The properties set the title text and whether it is shown, the font size,
    the text color, and the reporting interval in milliseconds.

    MCLab Code Block:

        |label_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def label_1_callback():
              global rp_label1_data
              return str(rp_label1_data)

Joystick
--------

.. function:: joystick_1_callback(joystick_x_value:int, joystick_y_value:int) -> None

    Run when the first joystick control moves. A callback is generated for each
    joystick added to the page.

    :param joystick_x_value: Current X-axis position.
    :type joystick_x_value: int
    :param joystick_y_value: Current Y-axis position.
    :type joystick_y_value: int

    The properties set the title text and whether it is shown, the joystick
    color, whether the joystick returns to the home position when released, and
    the minimum and maximum values of both axes.

    MCLab Code Block:

        |joystick_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def joystick_1_callback(joystick_x_value, joystick_y_value):
              print(joystick_y_value)
              print(joystick_x_value)

Input
-----

.. function:: input_1_callback(input_value:str) -> None

    Run when the text of the first input control changes. A callback is
    generated for each input box added to the page.

    :param input_value: Text entered in the input box.
    :type input_value: str

    The properties set the title text and whether it is shown, the font size,
    the text color, the hint text, and the character limit (8 by default).

    MCLab Code Block:

        |input_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def input_1_callback(input_value):
              print(input_value)

Image
-----

.. function:: image_1_callback() -> str

    Return the image URL for the first image control. The callback runs at the
    configured interval (3000 ms by default) and the page updates the displayed
    image from the returned URL.

    :return: Image URL.
    :rtype: str

    The properties set the title text and whether it is shown, the reporting
    interval in milliseconds, and the fallback image URL.

    MCLab Code Block:

        |image_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def image_1_callback():
              global rp_img1_url
              return rp_img1_url

Gauge
-----

.. function:: gauge_1_callback() -> str

    Return the value displayed by the first gauge control. The callback runs at
    the configured interval (3000 ms by default) and its return value is
    uploaded and shown on the gauge.

    :return: Value shown on the gauge.
    :rtype: str

    The properties set the title text and whether it is shown, the gauge label,
    the gauge color, the value suffix, the minimum and maximum values, and the
    reporting interval in milliseconds.

    MCLab Code Block:

        |gauge_callback.png|

    MicroPython Code Block:

        .. code-block:: python

            def gauge_1_callback():
              global rp_gauge1_data
              return str(rp_gauge1_data)

Chart
-----

The chart takes its data from an Ezdata list instead of a device callback, and
supports a configurable refresh interval and basic styling.

.. note::

    Understand the basic use of Ezdata before adding a chart. The data must be
    stored in an Ezdata ``List`` (not a ``Topic``) and passed as a ``map`` whose
    keys match the ``X Data Source`` and ``Y Data Source`` fields of the chart.
    A field that is left empty is not plotted.

The properties set the title text and whether it is shown, the theme (light or
dark), the element color, the chart type (bar or line), the refresh interval,
whether the legend is shown, the dataset name, the Y-axis label suffix, the
Ezdata token, the Ezdata list, the X and Y data source fields, and the maximum
number of points displayed.

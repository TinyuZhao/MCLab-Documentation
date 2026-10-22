.. _uiflow1-blockly-hardware-adc:

.. currentmodule:: machine

.. include:: ../refs/hardware.adc.ref

ADC
===

``machine.ADC`` samples an analog input and exposes attenuation and conversion
width controls.

MicroPython Examples
--------------------

Read an analog channel
^^^^^^^^^^^^^^^^^^^^^^

Open the |adc_example.m5f| project in MCLab.

This example configures the conversion width and attenuation and prints one sample.

MCLab Code Block:

    |adc_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/adc/adc_example.py
        :language: python

**API**
-------

.. class:: ADC(pin)

    Create an ADC channel for the specified input pin.

    :param pin: ADC-capable GPIO.
    :type pin: int or machine.Pin

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            adc0 = machine.ADC(36)

    .. method:: ADC.width(width) -> None

        Select conversion width.

        :param int width: Conversion width.

        Options:

            - ``machine.ADC.WIDTH_9BIT``: 9-bit conversion.
            - ``machine.ADC.WIDTH_10BIT``: 10-bit conversion.
            - ``machine.ADC.WIDTH_11BIT``: 11-bit conversion.
            - ``machine.ADC.WIDTH_12BIT``: 12-bit conversion.

        MCLab Code Block:

            |width.png|

        MicroPython Code Block:

            .. code-block:: python

                adc0.width(machine.ADC.WIDTH_12BIT)

    .. method:: ADC.atten(attenuation) -> None

        Set input attenuation.

        :param int attenuation: Input attenuation setting.

        Options:

            - ``machine.ADC.ATTN_0DB``: 0 dB attenuation.
            - ``machine.ADC.ATTN_2_5DB``: 2.5 dB attenuation.
            - ``machine.ADC.ATTN_6DB``: 6 dB attenuation.
            - ``machine.ADC.ATTN_11DB``: 11 dB attenuation.

        MCLab Code Block:

            |atten.png|

        MicroPython Code Block:

            .. code-block:: python

                adc0.atten(machine.ADC.ATTN_11DB)

    .. method:: ADC.read() -> int

        Return the current raw ADC sample.

        :return: Raw conversion value.
        :rtype: int

        MCLab Code Block:

            |read.png|

        MicroPython Code Block:

            .. code-block:: python

                value = adc0.read()

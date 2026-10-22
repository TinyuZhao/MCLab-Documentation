.. _uiflow1-blockly-hardware-dac:

.. currentmodule:: machine

.. include:: ../refs/hardware.dac.ref

DAC
===

``machine.DAC`` drives an ESP32 analog output pin. The implementation also
supports tone and waveform generation on the same channel.

Compatibility
-------------

This ESP32 DAC accepts only GPIO 25 and 26. Those pins may already be assigned to board peripherals; check the board
schematic before using them. ``write`` accepts values from 0 to 255.

MicroPython Examples
--------------------

Change DAC output
^^^^^^^^^^^^^^^^^

Open the |dac_example.m5f| project in MCLab.

This example sets the DAC output to its minimum value.

MCLab Code Block:

    |dac_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/dac/dac_example.py
        :language: python

**API**
-------

DAC
---

.. class:: DAC(pin)

    Create an analog output channel on GPIO 25 or 26. The chosen pin must
    be available and connected to the desired external circuit.

    :param pin: DAC-capable GPIO.
    :type pin: int or machine.Pin

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            dac0 = machine.DAC(26)

    .. method:: DAC.write(value) -> None

        Set the eight-bit output value.

        :param int value: Output value from 0 to 255.

        MCLab Code Block:

            |write.png|

        MicroPython Code Block:

            .. code-block:: python

                dac0.write(255)

    .. method:: DAC.beep(freq, duration, scale=0) -> None

        Generate a tone for ``duration`` milliseconds, then restore the
        channel output to its midpoint. The driver permits 16--32000 Hz and
        10--2000 ms.

        :param int freq: Tone frequency in hertz.
        :param int duration: Tone duration in milliseconds.
        :param int scale: Two-bit attenuation value from 0 to 3.

        MCLab Code Block:

            |beep.png|

        MicroPython Code Block:

            .. code-block:: python

                dac0.beep(1800, 200, 0)

    .. method:: DAC.waveform(freq, type, *, duration=0, scale=0, offset=0, invert=2) -> None

        Start the selected waveform. Frequency limits depend on the waveform
        type and are checked by the driver.

        :param int freq: Waveform frequency in hertz.
        :param int type: Waveform selection constant.
        :param int duration: Optional duration used by the waveform driver.
        :param int scale: Waveform scale.
        :param int offset: Signed waveform offset.
        :param int invert: Waveform inversion mode.

        Options:

            - ``machine.DAC.SINE``: Hardware sine wave.
            - ``machine.DAC.TRIANGLE``: Triangle wave.
            - ``machine.DAC.RAMP``: Rising ramp.
            - ``machine.DAC.SAWTOOTH``: Sawtooth wave.
            - ``machine.DAC.NOISE``: Noise waveform.

        MCLab Code Block:

            |waveform.png|

        MicroPython Code Block:

            .. code-block:: python

                dac0.waveform(1800, dac0.SINE)

    .. method:: DAC.stopwave() -> None

        Stop ongoing waveform output.

        MCLab Code Block:

            |stopwave.png|

        MicroPython Code Block:

            .. code-block:: python

                dac0.stopwave()

    .. method:: DAC.freq(freq) -> None

        Change the frequency of an active waveform. The allowed range depends
        on the active generator.

        :param int freq: New frequency in hertz.

        MCLab Code Block:

            |freq.png|

        MicroPython Code Block:

            .. code-block:: python

                dac0.freq(1800)

    .. method:: DAC.deinit() -> None

        Release the DAC output pin after stopping waveform generation.

        MicroPython Code Block:

            .. code-block:: python

                dac0.deinit()

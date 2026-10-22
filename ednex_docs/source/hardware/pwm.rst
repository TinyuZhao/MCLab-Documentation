.. _uiflow1-blockly-hardware-pwm:

.. currentmodule:: machine

.. include:: ../refs/hardware.pwm.ref

PWM
===

``machine.PWM`` generates a pulse-width-modulated signal on a GPIO and lets
applications change its frequency or duty cycle.

MicroPython Examples
--------------------

Change frequency and duty
^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |pwm_example.m5f| project in MCLab.

This example configures a PWM channel, then changes its frequency and duty value.

MCLab Code Block:

    |pwm_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/hardware/pwm/pwm_example.py
        :language: python

**API**
-------

.. class:: PWM(pin, freq=5000, duty=0, timer=0)

    Create a PWM channel for a GPIO.

    :param pin: Output GPIO.
    :type pin: int or machine.Pin
    :param int freq: Initial frequency in hertz.
    :param int duty: Initial duty value.
    :param int timer: Hardware timer selection.

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            pwm0 = machine.PWM(26, freq=50, duty=3, timer=0)

    .. method:: PWM.freq(value=None)

        Read or set the PWM frequency.

        :param int value: New frequency when provided.
        :return: Current frequency when reading.
        :rtype: int

        MCLab Code Block:

            |freq.png|

        MicroPython Code Block:

            .. code-block:: python

                pwm0.freq(1000)

    .. method:: PWM.duty(value=None)

        Read or set the duty value.

        :param int value: New duty value when provided.
        :return: Current duty value when reading.
        :rtype: int

        MCLab Code Block:

            |duty.png|

        MicroPython Code Block:

            .. code-block:: python

                pwm0.duty(50)

    .. method:: PWM.pause() -> None

        Pause PWM generation.

        MCLab Code Block:

            |pause.png|

        MicroPython Code Block:

            .. code-block:: python

                pwm0.pause()

    .. method:: PWM.resume() -> None

        Resume a paused PWM channel.

        MCLab Code Block:

            |resume.png|

        MicroPython Code Block:

            .. code-block:: python

                pwm0.resume()

    .. method:: PWM.hold_us(duration) -> None

        Hold the current PWM output for a duration in microseconds.

        :param int duration: Hold duration in microseconds.

        MCLab Code Block:

            |hold_us.png|

        MicroPython Code Block:

            .. code-block:: python

                pwm0.hold_us(100)

    .. method:: PWM.deinit() -> None

        Release the PWM channel.

        MicroPython Code Block:

            .. code-block:: python

                pwm0.deinit()

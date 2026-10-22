.. _uiflow1-blockly-hardware-microphone:

.. currentmodule:: MicrophonePDM

.. include:: ../refs/hardware.microphone.ref

Microphone
==========

``MicrophonePDM`` captures audio from the board's PDM microphone. It is
normally imported as ``MIC`` and configured with :func:`begin` before
recording.


**API**
-------

.. function:: begin(pin_ws, pin_data, sample_rate_hz=16000, buffer_length_ms=1000, block_length_ms=100)

    Start the PDM microphone and allocate its recording buffer.

    :param int pin_ws: Word-select (clock) pin of the PDM microphone.
    :param int pin_data: Data pin of the PDM microphone.
    :param int sample_rate_hz: Recording sample rate in hertz.
    :param int buffer_length_ms: Length of the recording buffer in milliseconds.
    :param int block_length_ms: Length of each read block in milliseconds.

    MCLab Code Block:

        |init.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.begin(pin_ws=0, pin_data=34, sample_rate_hz=16000,
                      buffer_length_ms=1000)

.. function:: deinit(timeout)

    Stop the microphone and release its resources.

    :param int timeout: Maximum time to wait, in milliseconds.

    MCLab Code Block:

        |deinit.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.deinit(10000)

.. function:: recordStart(fs, time_ms)

    Start recording to a WAV file.

    :param str fs: Destination WAV file path.
    :param int time_ms: Recording length in milliseconds.

    MCLab Code Block:

        |record_start.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.recordStart("/sd/test.wav", 5000)

.. function:: recordStop()

    Stop the recording started by :func:`recordStart`.

    MCLab Code Block:

        |record_stop.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.recordStop()

.. function:: pause(timeout)

    Pause recording.

    :param int timeout: Maximum time to wait, in milliseconds.

    MCLab Code Block:

        |pause.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.pause(1000)

.. function:: resume()

    Resume a paused recording.

    MCLab Code Block:

        |resume.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.resume()

.. function:: waitDone(timeout)

    Wait until the pending recording operation finishes.

    :param int timeout: Maximum time to wait, in milliseconds.
    :returns: Whether the operation finished before the timeout.
    :rtype: bool

    MCLab Code Block:

        |waitdone.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.waitDone(1000)

.. function:: rewind(sample_count)

    Move the read index back by a number of samples.

    :param int sample_count: Number of samples to rewind.

    MCLab Code Block:

        |rewind.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.rewind(16000)

.. function:: rewindMS(time_ms)

    Move the read index back by a number of milliseconds.

    :param int time_ms: Number of milliseconds to rewind.

    MCLab Code Block:

        |rewindms.png|

    MicroPython Code Block:

        .. code-block:: python

            MIC.rewindMS(1000)

.. function:: getRMS()

    Return the RMS level of the current block.

    :returns: Current RMS level.
    :rtype: float

    MCLab Code Block:

        |get_rms.png|

    MicroPython Code Block:

        .. code-block:: python

            print(MIC.getRMS())

.. function:: read()

    Read a single sample from the current reading index.

    :returns: Current sample value.
    :rtype: int

    MCLab Code Block:

        |read.png|

    MicroPython Code Block:

        .. code-block:: python

            print(MIC.read())

.. function:: readToBuffer(buffer, sample_count)

    Read a number of samples into a caller-provided buffer.

    :param bytearray buffer: Destination buffer for the samples.
    :param int sample_count: Number of samples to read.

    MCLab Code Block:

        |read_to_buffer.png|

    MicroPython Code Block:

        .. code-block:: python

            buffer = bytearray(16000)
            MIC.readToBuffer(buffer, 16000)

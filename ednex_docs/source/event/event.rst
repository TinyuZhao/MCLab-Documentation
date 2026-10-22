.. _uiflow1-blockly-event-event:

.. currentmodule:: hardware.button

.. include:: ../refs/hardware.button.ref

.. currentmodule:: libs.timeSchedule

.. include:: ../refs/libs.timeSchedule.ref

Event
=====

Event blocks use a continuous program loop, board buttons, or software timer
callbacks. The button objects and scheduler are initialized by
``MakerAndCoder``; handlers run when the corresponding event occurs.

Compatibility
-------------

The board startup attaches the A, B, and C buttons and creates
``timerSch``. The button implementation reads
virtual touch buttons, so these callbacks require the board's touch hardware.
``timerSch`` uses ``machine.Timer(3)`` in this firmware.

MicroPython Examples
--------------------

Loop
^^^^

Open the |event_loop_example.m5f| project in MCLab.

This example prints a message from the startup loop.

MCLab Code Block:

    |event_loop_example.png|

MicroPython Code Block:

    .. code-block:: python

        from MakerAndCoder import *
        from MakerAndCoder_ui import *
        from uiflow import *

        while True:
            print("Hello MC")
            wait_ms(2)

Button event
^^^^^^^^^^^^

Open the |event_button_example.m5f| project in MCLab.

This example prints once for each button press.

MCLab Code Block:

    |event_button_example.png|

MicroPython Code Block:

    .. code-block:: python

        from MakerAndCoder import *
        from MakerAndCoder_ui import *
        from uiflow import *

        def buttonA_wasPressed():
            print("A wasPressed")

        btnA.wasPressed(buttonA_wasPressed)

        def buttonB_wasPressed():
            print("B wasPressed")

        btnB.wasPressed(buttonB_wasPressed)

        def buttonC_wasPressed():
            print("C wasPressed")

        btnC.wasPressed(buttonC_wasPressed)

        while True:
            wait_ms(2)

Software timer
^^^^^^^^^^^^^^

Open the |event_timer_example.m5f| project in MCLab.

This example starts a 100 ms periodic timer that prints the elapsed time.

MCLab Code Block:

    |event_timer_example.png|

MicroPython Code Block:

    .. code-block:: python

        from MakerAndCoder import *
        from MakerAndCoder_ui import *
        from uiflow import *

        @timerSch.event("timer1")
        def on_tick():
            print("tick")

        timerSch.run("timer1", 100, timerSch.PERIODIC)
        while True:
            wait_ms(20)

**API**
-------

.. currentmodule:: hardware.button

.. automodule:: hardware.button
    :members:
    :member-order: bysource

.. currentmodule:: libs.timeSchedule

.. automodule:: libs.timeSchedule
    :members:
    :member-order: bysource

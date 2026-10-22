.. currentmodule:: MCLab.robocar

Line Follower Sensor
============================

.. include:: ../refs/MCLab.robocar_line_sensor.ref

``Robocar`` exposes the verified motor, ultrasonic, or line-follower controls for the Ednex Robocar.

MicroPython Examples
--------------------

Line follower example
^^^^^^^^^^^^^^^^^^^^^

Open the |line_fololwer_example.m5f| project in MCLab.

This example demonstrates line-follower sensor control with the ``Robocar`` API.

MCLab Code Block:

    |line_fololwer_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/line_follower/line_fololwer_example.py
        :language: python
        :linenos:

**API**
-------

.. autoclass:: Robocar
    :members: ow_line_port_init, reset_line_sensor, set_line_sensor_mode,
        get_line_sensor_mode, get_line_sensor_values,
        ow_two_line_get_sensor_values,
        ow_two_line_get_sensor_value,
        ow_multi_line_get_sensor_values, ow_multi_line_get_sensor_value,
        ow_multi_line_led
    :exclude-members: __init__, init_motor_module,
        move_forward, move_backward, move_right, move_left, rotate_right,
        rotate_left, set_motor_angle,
        set_motor_speed, motor_stop, get_encoder_count,
        get_encoder_vin_voltage, clear_encoder_count, angle_task,
        ultrasonic_port_init, ultrasonic_rgb_sensor, ultrasonic_rgb_color,
        ultrasonic_rgb_color_from, ultrasonic_rgb_color_all
    :no-inherited-members:
    :member-order: bysource
    :no-index:


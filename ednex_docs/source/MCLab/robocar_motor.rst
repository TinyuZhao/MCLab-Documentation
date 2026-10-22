.. currentmodule:: MCLab.robocar

DC Motor
=====================

.. include:: ../refs/MCLab.robocar_motor.ref

``Robocar`` provides motor movement, speed, encoder, and stop controls for the
Ednex Robocar.

MicroPython Examples
--------------------

DC Motor Example
^^^^^^^^^^^^^^^^

Open the |dc_motor_example.m5f| project in MCLab.

This example provides a touchscreen interface for moving the Robocar by a
selected distance, rotation count, or duration, and includes a stop control.

MCLab Code Block:

    |dc_motor_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/dc_motor/dc_motor_example.py
        :language: python

**API**
-------

.. autoclass:: Robocar
    :members: init_motor_module, move_forward,
        move_backward, move_right, move_left, rotate_right, rotate_left,
        set_motor_angle, set_motor_speed,
        motor_stop, get_encoder_count, get_encoder_vin_voltage,
        clear_encoder_count, angle_task
    :exclude-members: __init__, ow_line_port_init, reset_line_sensor,
        set_line_sensor_mode, get_line_sensor_mode, get_line_sensor_values,
        ow_two_line_get_sensor_values,
        ow_two_line_get_sensor_value,
        ow_multi_line_get_sensor_values, ow_multi_line_get_sensor_value,
        ow_multi_line_led, ultrasonic_port_init, ultrasonic_rgb_sensor,
        ultrasonic_rgb_color, ultrasonic_rgb_color_from,
        ultrasonic_rgb_color_all
    :no-inherited-members:
    :member-order: bysource


.. currentmodule:: MCLab.gyro_imu

Gyro(IMU)
=========

.. include:: ../refs/MCLab.gyro_imu.ref

``Gyro`` provides accelerometer, gyroscope, and derived orientation readings
from the BMI270 sensor.

MicroPython Examples
--------------------

.. Reserve one complete subsection for each example. Keep the MCLab project,
   description, MCLab Code Block, and MicroPython Code Block together.

Gyro readings
^^^^^^^^^^^^^

Open the |gyro_example.m5f| project in MCLab.

This example reads accelerometer and gyroscope values from the ``Gyro`` unit.

MCLab Code Block:

    |gyro_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/MCLab/gyro/gyro_example.py
        :language: python
        :linenos:

**API**
-------

.. automodule:: MCLab.gyro_imu
    :members: LOW_POWER_MODE, NORMAL_MODE, PERFORMANCE_MODE, ACC_RANGE_2G,
        ACC_RANGE_4G, ACC_RANGE_8G, ACC_RANGE_16G, GYR_RANGE_2000,
        GYR_RANGE_1000, GYR_RANGE_500, GYR_RANGE_250, GYR_RANGE_125,
        ACC_ODR_1600, ACC_ODR_800, ACC_ODR_400, ACC_ODR_200,
        ACC_ODR_100, ACC_ODR_50, ACC_ODR_25, GYR_ODR_3200,
        GYR_ODR_1600, GYR_ODR_800, GYR_ODR_400, GYR_ODR_200,
        GYR_ODR_100, GYR_ODR_50, GYR_ODR_25
    :exclude-members: Gyro

.. autoclass:: Gyro
    :members:
    :member-order: bysource

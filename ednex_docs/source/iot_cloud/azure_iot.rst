.. _uiflow1-blockly-iot_cloud-azure-iot:

.. currentmodule:: IoTcloud.Azure

.. include:: ../refs/iot_cloud.azure_iot.ref

Azure IoT
=========

The ``IoT_Central`` class registers the device with Azure IoT Central device
provisioning and connects it to the assigned hub. The device publishes
telemetry, handles commands, and updates the properties defined by its model.

MicroPython Examples
--------------------

Register a device and publish telemetry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |azure_iot_example.m5f| project in MCLab.

This example registers with Azure IoT Central, publishes IMU telemetry, handles
the ``Screen`` brightness property and the ``RTC`` and ``Speaker`` commands, and
updates the ``DeviceInformation`` property.

MCLab Code Block:

    |azure_iot_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/iot_cloud/azure_iot/azure_iot_example.py
        :language: python

**API**
-------

.. autoclass:: IoT_Central
    :members:
    :exclude-members: register_device, loop_assignment, subscribe_C2D_message, subscribe_twin_reported_response, subscribe_twin_desired_response, retrieve_twin_properties, direct_method_cb, retrieve_twin_properties_cb, desired_twin_properties_cb
    :member-order: bysource

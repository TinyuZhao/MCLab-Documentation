.. _uiflow1-blockly-iot_cloud-azure-classic:

.. currentmodule:: IoTcloud.Azure

.. include:: ../refs/iot_cloud.azure_classic.ref

Azure Classic
=============

The ``IoT_Hub`` class connects the device to Azure IoT Hub over MQTT. It
publishes device-to-cloud telemetry, receives cloud-to-device messages, handles
direct methods, and reads and updates device-twin properties.

MicroPython Examples
--------------------

Publish telemetry and handle cloud messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |azure_classic_example.m5f| project in MCLab.

This example connects to Azure IoT Hub, publishes gyroscope data every five
seconds, receives cloud-to-device messages, handles an ``rgb`` direct method,
and updates the reported device-twin properties.

MCLab Code Block:

    |azure_classic_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/iot_cloud/azure_classic/azure_classic_example.py
        :language: python

**API**
-------

.. autoclass:: IoT_Hub
    :members:
    :exclude-members: subscribe_twin_reported_response, direct_method_cb, retrieve_twin_properties_cb, on_property_update, desired_twin_properties_cb
    :member-order: bysource

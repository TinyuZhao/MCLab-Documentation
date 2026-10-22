.. _uiflow1-blockly-iot_cloud-aws:

.. currentmodule:: IoTcloud.AWS

.. include:: ../refs/IoTcloud.AWS.ref

AWS IoT
========


The ``AWS`` class provides MQTT publish and subscription operations for an AWS IoT endpoint.

MicroPython Examples
--------------------

Publish to AWS IoT
^^^^^^^^^^^^^^^^^^

Open the |aws_example.m5f| project in MCLab.

This example connects to an AWS IoT endpoint and publishes a message every four seconds.

MCLab Code Block:

    |aws_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/iot_cloud/aws/aws_example.py
        :language: python

**API**
-------

.. automodule:: IoTcloud.AWS
    :members:
    :exclude-members: AWS

.. autoclass:: AWS
    :members: start, subscribe, publish
    :member-order: bysource

.. _uiflow1-blockly-iot_cloud-mqtt:

.. currentmodule:: libs.mcmqtt

.. include:: ../refs/libs.mcmqtt.ref

MQTT
====

The ``libs.mcmqtt.MCmqtt`` client connects to an MQTT broker and publishes and subscribes to topics.

MicroPython Examples
--------------------

Publish and subscribe
^^^^^^^^^^^^^^^^^^^^^

Open the |mqtt_example.m5f| project in MCLab.

This example subscribes to a topic, registers a last-will message, connects,
and keeps publishing to a topic.

MCLab Code Block:

    |mqtt_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/iot_cloud/mqtt/mqtt_example.py
        :language: python

**API**
-------

.. currentmodule:: libs.mcmqtt

.. automodule:: libs.mcmqtt
    :members:
    :member-order: bysource

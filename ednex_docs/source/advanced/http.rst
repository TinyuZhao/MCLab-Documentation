.. _uiflow1-blockly-advanced-http:

.. currentmodule:: urequests

.. include:: ../refs/urequests.ref

HTTP
====

The ``urequests`` HTTP client sends requests and exposes the response status and body. Network access is required for the example.

MicroPython Examples
--------------------

Send an HTTP request
^^^^^^^^^^^^^^^^^^^^

Open the |http_example.m5f| project in MCLab.

This example sends a GET request, prints the status code and response text, then releases the response.

MCLab Code Block:

    |http_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/advanced/http/http_example.py
        :language: python

**API**
-------

.. currentmodule:: urequests

.. autofunction:: request

.. autoclass:: Response
    :members: text
    :member-order: bysource

.. attribute:: Response.status_code

    Status code returned by the server. The attribute is set on the response
    object by :func:`request` and is not available before the request is sent.

    MCLab Code Block:

        |get_status_code.png|

    MicroPython Code Block:

        .. code-block:: python

            print(response.status_code)

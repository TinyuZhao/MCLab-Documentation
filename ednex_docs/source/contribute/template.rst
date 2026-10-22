**************************
API Documentation Template
**************************

.. note::

    1. Please follow the template below to write your API documentation;
    2. Strict use of reStructuredText syntax;
    3. Write strictly according to the various tags of the template
    4. When you are finished, delete all instructions (similar to this one) and any extra header information.

.. For a Python-backed driver, replace ``module_name`` with the importable
   module path. Keep the ``currentmodule`` directive near the top of the page.
   For a C-backed driver without a Python source file, use ``machine`` or the
   module that owns the public API instead.

.. currentmodule:: module_name

Device or Feature Name
======================

.. If the page has a generated public-API reference file, uncomment and
   replace the following directive. C-backed pages can omit it.
   ``.. include:: ../refs/module_name.ref``

``PublicClass`` provides a short overview of the device or feature. Describe
the sensor, peripheral, or service that the page documents, and mention any
important operating limits here.

MicroPython Examples
--------------------

.. note::

    Prepare one or more examples that fully demonstrate the API. Keep the
    MCLab project, its description, the MCLab Code Block, and the corresponding
    MicroPython source together in the same example subsection. Repeat the
    complete subsection for each additional example.

Example name
^^^^^^^^^^^^

Open the ``example_name.m5f`` project in MCLab.

Describe what the example does, which hardware it uses, and what the reader
should observe when it runs.

MCLab Code Block:

    .. Replace this placeholder with the image substitution from the page's
       reference file, for example: ``|example_name.png|``.

MicroPython Code Block:

    .. Replace this placeholder with the source file under ``examples/ednex/``.
       Use the following directive after the example file has been added:
       ``.. literalinclude:: ../../../examples/ednex/category/example_name/example_name.py``
       with ``:language: python`` and ``:linenos:`` options.


**API**
-------

For a driver without a corresponding Python source file, write the public API
manually with ``function``, ``class``, ``method``, ``property``, ``staticmethod``,
``classmethod``, ``attribute`` and ``data`` directives. Keep option constants
under the parameter that uses them; do not create a separate constant section.

Function
--------

.. All functions can be put under this heading.

.. function:: func1(arg1:int, arg2:int) -> int

    Function 1, please write a detailed description of the function.

    :param arg1: Parameter 1.
    :type arg1: int
    :param int arg2: Parameter 2.
    :type arg2: int

    :return: Return value.
    :rtype: int

    .. Add this block only when a parameter accepts named constants. The list
       items are indented four spaces further than ``Options:``.

    Options:

        - ``module.CONSTANT_A``: Meaning of the first option.
        - ``module.CONSTANT_B``: Meaning of the second option.

    .. Please note that the return value type of the function needs to be specified

    MCLab Code Block:

        .. Please place the Blockly image of the function and delete this line when you are done.

    MicroPython Code Block:

        .. code-block:: python

            pass # Please put the MicroPython code of the function, and delete this line when you are done


Class1
-------

.. Add a title to each class.

.. class:: Class1(arg1:int)

    Constructor.

    :param arg1: Parameter 1.
    :type arg1: int

    .. Please note that the type of the parameter needs to be specified


    .. method:: Class1.method1(arg1:int, arg2:int) -> int

        Method 1, please write a detailed description of the method.

        :param arg1: Parameter 1.
        :type arg1: int
        :param int arg2: Parameter 2.
        :type arg2: int
        :return: Return value.
        :rtype: int

        .. Please note that the return value type of the method needs to be specified.

        MCLab Code Block:

            .. Please place the Blockly image of the function and delete this line when you are done.

        MicroPython Code Block:

            .. code-block:: python

                pass # Please put the MicroPython code of the function, and delete this line when you are done.


    .. property:: Class1.property1
        :type: int

        Property 1, please write a detailed description of the property.

        .. Please note that the type of the property needs to be specified.

        MCLab Code Block:

            .. Please place the Blockly image of the function and delete this line when you are done.

        MicroPython Code Block:

            .. code-block:: python

                pass # Please put the MicroPython code of the function, and delete this line when you are done.


    .. staticmethod:: Class1.staticmethod1(arg1:int, arg2:int) -> int

        Static method 1, please write a detailed description of the static method.

        :param arg1: Parameter 1.
        :type arg1: int
        :param int arg2: Parameter 2.
        :type arg2: int
        :return: Return value.
        :rtype: int

        MCLab Code Block:

            .. Please place the Blockly image of the function and delete this line when you are done.

        MicroPython Code Block:

            .. code-block:: python

                pass # Please put the MicroPython code of the function, and delete this line when you are done.


    .. classmethod:: Class1.classmethod1(arg1:int, arg2:int) -> int

        Class method 1, please write a detailed description of the class method.

        :param arg1: Parameter 1.
        :type arg1: int
        :param int arg2: Parameter 2.
        :type arg2: int
        :return: Return value.
        :rtype: int

        MCLab Code Block:

            .. Please place the Blockly image of the function and delete this line when you are done.

        MicroPython Code Block:

            .. code-block:: python

                pass # Please put the MicroPython code of the function, and delete this line when you are done.


    .. attribute:: Class1.b
        :type: int

        Attribute b, please write a detailed description of the attribute.

        .. Please note that the type of the attribute needs to be specified.

        MCLab Code Block:

            .. Please place the Blockly image of the function and delete this line when you are done.

        MicroPython Code Block:

            .. code-block:: python

                pass # Please put the MicroPython code of the function, and delete this line when you are done.


    .. data:: Class1.CONSTANT1
        :type: int

        Constant 1, Please write a detailed description of the constant. Constants are named using uppercase letters.

        MCLab Code Block:

            .. Please place the Blockly image of the function and delete this line when you are done.

        MicroPython Code Block:

            .. code-block:: python

                pass # Please put the MicroPython code of the function, and delete this line when you are done.

Class2
-------

.. class:: Class2()

    Constructor.

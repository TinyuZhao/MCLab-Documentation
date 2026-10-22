.. _uiflow1-blockly-generic-logic:

.. currentmodule:: builtins

Logic
=====

.. include:: ../refs/generic.logic.ref

Conditional statements and Boolean operators select which MicroPython code is
executed. They are ordinary Python syntax rather than device APIs.

MicroPython Examples
--------------------

Choose a branch
^^^^^^^^^^^^^^^

Open the |logic_example.m5f| project in MCLab.

This example compares a random value and prints it only when it is greater than 127.

MCLab Code Block:

    |logic_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/logic/logic_example.py
        :language: python

**API**
-------

The blocks in this section describe Python language syntax rather than
preinstalled Ednex APIs. Each entry shows the operands the block accepts and
the value, if any, it produces.

Conditions
----------

.. function:: if(condition)

    Run the indented block only when the condition is true.

    :param expression condition: Expression evaluated before the block runs.

    MCLab Code Block:

        |if.png|

    MicroPython Code Block:

        .. code-block:: python

            value = 5
            if value < 10:
                value += 1

.. function:: else()

    Run the indented block when the ``if`` condition is false.

    MCLab Code Block:

        |ifelse.png|

    MicroPython Code Block:

        .. code-block:: python

            value = 5
            if value < 10:
                value += 1
            else:
                value -= 1

.. function:: compare(left, operator, right) -> bool

    Test two values and produce a Boolean result.

    :param object left: Value on the left side of the comparison.
    :param str operator: Comparison operator, one of ``==``, ``!=``, ``<``,
                         ``<=``, ``>`` or ``>=``.
    :param object right: Value on the right side of the comparison.
    :return: ``True`` when the comparison holds; otherwise ``False``.
    :rtype: bool

    MCLab Code Block:

        |compare.png|

    MicroPython Code Block:

        .. code-block:: python

            same = left == right
            inside = 0 <= value <= 10

Boolean operators
-----------------

.. function:: operation(first, operator, second) -> object

    Combine two conditions. The block's dropdown selects ``and`` or ``or``.

    :param object first: Condition evaluated first.
    :param str operator: ``and`` requires both conditions to be true; ``or``
                         accepts a value when either condition is true.
    :param object second: Condition evaluated only when it still affects the
                          result.
    :return: The value that decides the result, as with the ``and`` and ``or``
              operators.
    :rtype: object

    MCLab Code Block:

        |operation.png|

    MicroPython Code Block:

        .. code-block:: python

            ready = True
            enabled = ready and (value != 0)
            fallback = cached or default

.. function:: negate(value) -> bool

    Invert a condition.

    :param object value: Value to invert.
    :return: ``True`` when the value is false; otherwise ``False``.
    :rtype: bool

    MCLab Code Block:

        |negate.png|

    MicroPython Code Block:

        .. code-block:: python

            disabled = not enabled

.. function:: ternary(condition, value_if_true, value_if_false) -> object

    Choose between two values inside one expression.

    :param expression condition: Condition tested before a value is chosen.
    :param object value_if_true: Value produced when the condition is true.
    :param object value_if_false: Value produced when the condition is false.
    :return: The selected value.
    :rtype: object

    MCLab Code Block:

        |ternary.png|

    MicroPython Code Block:

        .. code-block:: python

            result = 0 if disabled else value

Literals
--------

.. data:: True

    The Boolean literals ``True`` and ``False``.

    :type: bool

    MCLab Code Block:

        |boolean.png|

    MicroPython Code Block:

        .. code-block:: python

            ready = True
            stopped = False

.. data:: None

    The null value, used when no result is available.

    :type: None

    MCLab Code Block:

        |null.png|

    MicroPython Code Block:

        .. code-block:: python

            current = None

Multiple branches
-----------------

.. function:: elif(condition)

    When a value selects exactly one of several cases, replace the ``switch``
    block with an ``if``/``elif``/``else`` chain.

    :param expression condition: Expression evaluated after every earlier
                                 condition was false.

    MCLab Code Block:

        |switch.png|

    MicroPython Code Block:

        .. code-block:: python

            state = 2
            if state == 0:
                name = "idle"
            elif state == 1:
                name = "run"
            else:
                name = "stop"

Exception handling
------------------

.. function:: try(exception)

    Catch a known exception type when an operation can fail. Avoid a bare
    ``except`` unless all exception types are intentionally handled.

    :param type exception: Exception type caught by the ``except`` clause.

    MCLab Code Block:

        |try_except.png|

    MicroPython Code Block:

        .. code-block:: python

            try:
                number = int("not a number")
            except ValueError:
                number = 0

Change detection
----------------

.. function:: when(condition)

    Compare the current value with the previous value and act only when the
    value differs.

    :param expression condition: Expression re-evaluated while the loop runs.

    MCLab Code Block:

        |when.png|

    MicroPython Code Block:

        .. code-block:: python

            previous = None
            current = 1
            if current != previous:
                previous = current

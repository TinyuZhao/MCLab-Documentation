.. _uiflow1-blockly-generic-lists:

.. currentmodule:: builtins

Lists
=====

.. include:: ../refs/generic.lists.ref

Lists are mutable ordered sequences. They can hold values of different types
and can be indexed or sliced to retrieve elements.

MicroPython Examples
--------------------

Print every list element
^^^^^^^^^^^^^^^^^^^^^^^^

Open the |lists_example.m5f| project in MCLab.

This example prints the length of a list and every element in it.

MCLab Code Block:

    |lists_example.png|

MicroPython Code Block:

    .. literalinclude:: ../../../examples/ednex/generic/lists/lists_example.py
        :language: python

**API**
-------

List
----

.. class:: list(iterable=())

    Construct a mutable sequence from an iterable. ``[]`` is the literal
    syntax for an empty list.

    :param iterable: Initial values.
    :type iterable: iterable

    MCLab Code Block:

        |create_empty.png|

        |create_with.png|

    MicroPython Code Block:

        .. code-block:: python

            values = [1, 2, 3]
            empty = []

    .. method:: list.append(value) -> None

        Add one value to the end of the list.

        :param value: Value to add.
        :type value: object

        MicroPython Code Block:

            .. code-block:: python

                values.append(4)

    .. method:: list.index(value) -> int

        Return the index of the first matching element. An absent value
        raises ``ValueError``.

        :param value: Value to find.
        :type value: object
        :return: Zero-based index.
        :rtype: int

        MCLab Code Block:

            |indexOf.png|

        MicroPython Code Block:

            .. code-block:: python

                position = values.index(2)

    .. method:: list.reverse() -> None

        Reverse the elements of the list in place.

        MCLab Code Block:

            |reverse.png|

        MicroPython Code Block:

            .. code-block:: python

                values.reverse()

    .. method:: list.pop(index=-1)

        Remove and return the element at ``index``; by default, remove the
        last element.

        :param int index: Position to remove.
        :return: Removed element.
        :rtype: object

        MicroPython Code Block:

            .. code-block:: python

                last = values.pop()

Indexing and slicing
--------------------

``values[index]`` retrieves or replaces one element; ``values[start:stop]``
creates a slice. Indexing begins at zero and negative indices count from the
end.

MCLab Code Block:

    |getIndex.png|

    |setIndex.png|

    |getSublist.png|

MicroPython Code Block:

    .. code-block:: python

        values = [1, 2, 3]
        values[0] = 10
        part = values[1:3]

Length and emptiness
--------------------

``len(values)`` returns the number of elements in the list; a list is empty
when its length is ``0``.

MCLab Code Block:

    |length.png|

    |isEmpty.png|

MicroPython Code Block:

    .. code-block:: python

        size = len(values)
        empty = len(values) == 0

Repeating a list
----------------

``[value] * count`` builds a list containing ``value`` repeated ``count``
times.

MCLab Code Block:

    |repeat.png|

MicroPython Code Block:

    .. code-block:: python

        zeros = [0] * 5

Splitting text into a list
--------------------------

``str.split`` divides a string on a delimiter and returns the parts as a
list.

MCLab Code Block:

    |split.png|

MicroPython Code Block:

    .. code-block:: python

        fields = "1,2,3".split(",")

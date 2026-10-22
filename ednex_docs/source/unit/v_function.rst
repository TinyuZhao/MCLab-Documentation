.. currentmodule:: units.VFunction._apriltag_code

V Function Unit
===============

The V Function Unit exposes the vision functions built into a StickV or UnitV
camera. In MicroPython, create the loader with
``unit.get(unit.V_FUNCTION, port)`` and select a function with
``.init('function_name')``; the block palette provides one init block per
function listed below.

.. toctree::
    :maxdepth: 1

    v_function_apriltag
    v_function_bar_code
    v_function_color_track
    v_function_dm_code
    v_function_face_detect
    v_function_line_tracker
    v_function_motion
    v_function_qr_code
    v_function_tag_reader
    v_function_target_track

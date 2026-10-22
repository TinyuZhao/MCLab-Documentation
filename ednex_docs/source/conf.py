#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


_docs_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(_docs_root, "_autodoc_stubs"))
sys.path.insert(0, os.path.join(_docs_root, "_api_stubs"))


project = "Ednex MC4 MicroPython"
copyright = "2026, Ednex"
author = "Ednex"
version = release = "MCLab-V2.1.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

# These modules exist only in the firmware.  Keeping the list here also makes
# the documentation build tolerant of examples that import hardware modules.
autodoc_mock_imports = [
    "machine",
    "bluetooth",
    "_onewire",
    "uos",
    "utime",
    "ustruct",
    "simpleOTA",
    "MakerAndCoder",
    "display",
    "lvgl",
    "lvesp32",
    "espidf",
    "rtch",
    "deviceCfg",
]

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
}
autodoc_typehints = "description"
autodoc_docstring_signature = True

master_doc = "index"
source_suffix = ".rst"
exclude_patterns = ["build", "_autodoc_stubs", "_api_stubs"]
pygments_style = "sphinx"

html_theme = "sphinx_rtd_theme"
html_title = "Ednex MC4 MicroPython Documentation"
htmlstatic_path = ["static"]

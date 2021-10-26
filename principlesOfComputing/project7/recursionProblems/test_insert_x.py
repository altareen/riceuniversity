###
#-------------------------------------------------------------------------------
# test_insert_x.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_insert_x.py
#
# Description:
# This program implements the test bench for insert_x.py
#
##

import insert_x as inx
import pytest

@pytest.mark.parametrize("my_string, expected", [
    ("catdog", "cxaxtxdxoxg"),
    ("mouse", "mxoxuxsxe"),
    ("elephant", "exlxexpxhxaxnxt"),
    ("crocodile", "cxrxoxcxoxdxixlxe"),
    ("zebra", "zxexbxrxa"),
    ("antelope", "axnxtxexlxoxpxe"),
    ("pelican", "pxexlxixcxaxn"),
    ("swan", "sxwxaxn"),
    ("pigeon", "pxixgxexoxn"),
    ("ox", "oxx")
])

def test_insert_x(my_string, expected):
    actual = inx.insert_x(my_string)
    assert expected == actual


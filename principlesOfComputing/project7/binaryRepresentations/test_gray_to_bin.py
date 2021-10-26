###
#-------------------------------------------------------------------------------
# test_gray_to_bin.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_gray_to_bin.py
#
# Description:
# This program implements the test bench for gray_to_bin.py
#
##

import gray_to_bin as gtb
import pytest

@pytest.mark.parametrize("num, expected", [
    ("100", "111"),
])

def test_gray_to_bin(num, expected):
    actual = gtb.gray_to_bin(num)
    assert expected == actual


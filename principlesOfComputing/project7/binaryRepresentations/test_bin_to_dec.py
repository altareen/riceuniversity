###
#-------------------------------------------------------------------------------
# test_bin_to_dec.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_bin_to_dec.py
#
# Description:
# This program implements the test bench for bin_to_dec.py
#
##

import bin_to_dec as btd
import pytest

@pytest.mark.parametrize("num, expected", [
    ("1", 1),
    ("10", 2),
    ("11", 3),
    ("100", 4),
    ("101", 5),
    ("111", 7),
    ("1000", 8),
    ("1010", 10),
    ("10000", 16),
    ("1010101", 85),
])

def test_bin_to_dec(num, expected):
    actual = btd.bin_to_dec(num)
    assert expected == actual


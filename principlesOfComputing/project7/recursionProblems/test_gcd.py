###
#-------------------------------------------------------------------------------
# test_gcd.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_gcd.py
#
# Description:
# This program implements the test bench for gcd.py
#
##

import gcd as g
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
    (270, 192, 6),
    (842, 96, 2),
    (938, 74, 2),
    (1094, 62, 2),
    (2200, 132, 44),
    (5238, 268, 2),
    (9142, 380, 2),
    (12230, 438, 2),
    (15092, 736, 4),
    (30892, 998, 2)
])

def test_gcd(num1, num2, expected):
    actual = g.gcd(num1, num2)
    assert expected == actual


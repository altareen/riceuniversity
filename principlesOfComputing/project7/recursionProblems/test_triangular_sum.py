###
#-------------------------------------------------------------------------------
# test_triangular_sum.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_triangular_sum.py
#
# Description:
# This program implements the test bench for triangular_sum.py
#
##

import triangular_sum as tri
import pytest

@pytest.mark.parametrize("num, expected", [
    (3, 6),
    (4, 10),
    (5, 15),
    (23, 276),
    (41, 861),
    (75, 2850),
    (89, 4005),
    (103, 5356),
    (231, 26796),
    (587, 172578)
])

def test_triangular_sum(num, expected):
    actual = tri.triangular_sum(num)
    assert expected == actual


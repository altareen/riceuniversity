###
#-------------------------------------------------------------------------------
# test_make_gray.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_make_gray.py
#
# Description:
# This program implements the test bench for make_gray.py
#
##

import make_gray as mak
import pytest

@pytest.mark.parametrize("n, expected", [
    (1, ['0', '1']),
    (2, ['00', '01', '11', '10']),
    (3, ['000', '001', '011', '010', '110', '111', '101', '100']),
    (4, ['0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100', '1100', '1101', '1111', '1110', '1010', '1011', '1001', '1000'])
])

def test_make_gray(n, expected):
    actual = mak.make_gray(n)
    assert expected == actual


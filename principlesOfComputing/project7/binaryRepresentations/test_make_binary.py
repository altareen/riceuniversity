###
#-------------------------------------------------------------------------------
# test_make_binary.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_make_binary.py
#
# Description:
# This program implements the test bench for make_binary.py
#
##

import make_binary as mak
import pytest

@pytest.mark.parametrize("n, expected", [
    (1, ['0', '1']),
    (2, ['00', '01', '10', '11']),
    (3, ['000', '001', '010', '011', '100', '101', '110', '111']),
    (4, ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'])
])

def test_make_binary(n, expected):
    actual = mak.make_binary(n)
    assert expected == actual


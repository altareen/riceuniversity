###
#-------------------------------------------------------------------------------
# test_number_of_threes.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_number_of_threes.py
#
# Description:
# This program implements the test bench for number_of_threes.py
#
##

import number_of_threes as thr
import pytest

@pytest.mark.parametrize("num, expected", [
    (34534, 2),
    (2335334, 4),
    (23874328, 2),
    (983293839, 3),
    (8237632833, 4),
    (28376423873, 3),
    (987239872332, 3),
    (9283749238472, 2),
    (82736483276423, 3),
    (872364283746328, 3)
])

def test_number_of_threes(num, expected):
    actual = thr.number_of_threes(num)
    assert expected == actual


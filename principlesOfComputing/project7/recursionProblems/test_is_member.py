###
#-------------------------------------------------------------------------------
# test_is_member.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_is_member.py
#
# Description:
# This program implements the test bench for is_member.py
#
##

import is_member as mem
import pytest

@pytest.mark.parametrize("my_list, elem, expected", [
    (['c', 'a', 't'], 'a', True),
    (['d', 'o', 'g'], 'h', False),
    (['m', 'o', 'u', 's', 'e'], 'u', True),
    (['e', 'l', 'e', 'p', 'h', 'a', 'n', 't'], 's', False),
    (['c', 'r', 'o', 'c', 'o', 'd', 'i', 'l', 'e'], 'c', True),
    ([2, 9, 3, 8], 5, False),
    ([2, 8, 3, 7, 4], 8, True),
    ([9, 2, 8, 3, 7, 6], 4, False),
    ([2, 8, 3, 7, 4, 2, 3], 8, True),
    ([2, 9, 3, 8, 4, 7, 2, 3], 1, False)
])

def test_is_member(my_list, elem, expected):
    actual = mem.is_member(my_list, elem)
    assert expected == actual


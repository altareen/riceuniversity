###
#-------------------------------------------------------------------------------
# test_list_reverse.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_list_reverse.py
#
# Description:
# This program implements the test bench for list_reverse.py
#
##

import list_reverse as rev
import pytest

@pytest.mark.parametrize("my_list, expected", [
    ([2, 3, 1], [1, 3, 2]),
    ([2, 9, 3, 8], [8, 3, 9, 2]),
    ([8, 3, 4, 7, 5], [5, 7, 4, 3, 8]),
    ([9, 2, 3, 8, 7, 4], [4, 7, 8, 3, 2, 9]),
    ([3, 8, 9, 7, 2, 9, 1], [1, 9, 2, 7, 9, 8, 3]),
    (['o', 'x'], ['x', 'o']),
    (['c', 'a', 't'], ['t', 'a', 'c']),
    (['s', 'w', 'a', 'n'], ['n', 'a', 'w', 's']),
    (['m', 'o', 'u', 's', 'e'], ['e', 's', 'u', 'o', 'm']),
    (['a', 'n', 't', 'e', 'l', 'o', 'p', 'e'], ['e', 'p', 'o', 'l', 'e', 't', 'n', 'a'])
])

def test_list_reverse(my_list, expected):
    actual = rev.list_reverse(my_list)
    assert expected == actual


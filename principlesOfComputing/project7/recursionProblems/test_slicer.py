###
#-------------------------------------------------------------------------------
# test_slicer.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_slicer.py
#
# Description:
# This program implements the test bench for slicer.py
#
##

import slicer as sli
import pytest

@pytest.mark.parametrize("my_list, first, last, expected", [
    (['a', 'b', 'c', 'd', 'e'], 2, 4, ['c', 'd']),
    (['a', 'b', 'c', 'd', 'e'], 0, 5, ['a', 'b', 'c', 'd', 'e']),
    (['m', 'o', 'u', 's', 'e'], 1, 3, ['o', 'u']),
    (['a', 'n', 't', 'e', 'l', 'o', 'p', 'e'], 2, 7, ['t', 'e', 'l', 'o', 'p']),
    (['c', 'h', 'o', 'c', 'o', 'l', 'a', 't', 'e'], 3, 7, ['c', 'o', 'l', 'a']),
    ([2, 9, 3, 8, 4, 7, 2, 3], 2, 6, [3, 8, 4, 7]),
    ([9, 8, 3, 4, 7, 5, 3, 4, 9, 8, 2], 4, 9, [7, 5, 3, 4, 9]),
    ([9, 3, 8, 4, 7, 5, 3, 2, 9, 8, 7, 4, 2], 6, 10, [3, 2, 9, 8]),
    ([9, 8, 3, 2, 7, 4, 3, 9, 8, 7, 4, 9, 2, 3, 8], 5, 11, [4, 3, 9, 8, 7, 4]),
    ([9, 2, 8, 3, 7, 5, 2, 3, 9, 8, 4, 7, 2, 3, 9, 4, 7, 2, 3], 7, 14, [3, 9, 8, 4, 7, 2, 3])
])

def test_slicer(my_list, first, last, expected):
    actual = sli.slicer(my_list, first, last)
    assert expected == actual


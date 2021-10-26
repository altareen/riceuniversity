###
#-------------------------------------------------------------------------------
# test_manhattan_distance.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 29, 2021
# Run:      pytest -q test_manhattan_distance.py
#
# Description:
# This program implements the test bench for manhattan_distance.py
#
##

import manhattan_distance as man
import pytest

@pytest.mark.parametrize("entity_list, expected", [
    ([[4, 0],[2, 5]], [[4, 5, 5, 4, 3, 2, 3, 4], [3, 4, 4, 3, 2, 1, 2, 3], [2, 3, 3, 2, 1, 0, 1, 2], [1, 2, 3, 3, 2, 1, 2, 3], [0, 1, 2, 3, 3, 2, 3, 4], [1, 2, 3, 4, 4, 3, 4, 5]])
])

def test_create_distance_field(entity_list, expected):
    actual = man.create_distance_field(entity_list)
    assert expected == actual


###
#-------------------------------------------------------------------------------
# test_greedy_boss.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 26, 2021
# Run:      pytest -q test_greedy_boss.py
#
# Description:
# This program implements the test bench for greedy_boss.py
#
##

import greedy_boss as sim
import pytest

@pytest.mark.parametrize("days_in_simulation, bribe_cost_increment, expected", [
    (35, 100, [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]),
    (35, 0, [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)])
])

def test_greedy_boss(days_in_simulation, bribe_cost_increment, expected):
    actual = sim.greedy_boss(days_in_simulation, bribe_cost_increment)
    assert expected == actual



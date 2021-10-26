###
#-------------------------------------------------------------------------------
# test_game_yahtzee.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 24, 2021
# Run:      pytest -q test_game_yahtzee.py
#
# Description:
# This program implements the test bench for game_yahtzee.py
#
##

import game_yahtzee as game
import pytest

@pytest.mark.parametrize("hand, expected", [
    ((2, 3, 3, 3, 4), 9),
    ((1, 1, 1, 5, 6), 6),
    ((4, 4, 5, 5, 6), 10)
])

def test_score(hand, expected):
    actual = game.score(hand)
    assert expected == actual

@pytest.mark.parametrize("held_dice, num_die_sides, num_free_dice, expected", [
    ((2, 2), 6, 2, 5.83),
    ((5, 5, 6), 6, 2, 12.33),
    ((3, 3, 4, 6), 6, 1, 7.83),
])

def test_expected_value(held_dice, num_die_sides, num_free_dice, expected):
    actual = game.expected_value(held_dice, num_die_sides, num_free_dice)
    assert expected == pytest.approx(actual, 0.01)

@pytest.mark.parametrize("hand, expected", [
    ((1,), {(), (1,)}),
    ((1, 2), {(), (1,), (1, 2), (2,)}),
    ((1, 2, 3), {(2,), (1, 2), (1, 2, 3), (2, 3), (1,), (3,), (), (1, 3)})
])

def test_gen_all_holds(hand, expected):
    actual = game.gen_all_holds(hand)
    assert expected == actual

@pytest.mark.parametrize("hand, num_die_sides, expected", [
    ((1, 2, 2, 5, 5), 6, (12.657407407407417, (5, 5))),
    ((1, 3, 3, 4, 6), 6, (10.691358024691507, (6,))),
    ((4, 4, 4, 5, 5), 6, (13.33333333333334, (4, 4, 4))),
])

def test_strategy(hand, num_die_sides, expected):
    actual = game.strategy(hand, num_die_sides)
    assert expected == actual


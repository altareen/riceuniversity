###
#-------------------------------------------------------------------------------
# test_solitaire_mancala.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 12, 2021
# Run:      pytest -q test_solitaire_mancala.py
#
# Description:
# This program implements the test bench for solitaire_mancala.py
#
##

from solitaire_mancala import SolitaireMancala
import pytest

@pytest.fixture
def game():
    return SolitaireMancala()

def test_set_board(game):
    game.set_board([0, 5, 3, 1, 1, 0, 0])
    expected = str([0, 5, 3, 1, 1, 0, 0])
    actual = str(game)
    assert expected == actual

def test_get_num_seeds(game):
    game.set_board([0, 5, 3, 1, 1, 0, 0])
    expected = 5
    actual = game.get_num_seeds(1)
    assert expected == actual

def test_is_legal_move(game):
    game.set_board([2, 1, 1, 0, 1])
    expected = False
    actual = game.is_legal_move(2)
    assert expected == actual

def test_apply_move(game):
    game.set_board([0, 1, 2, 3])
    game.apply_move(1)
    expected = str([1, 0, 2, 3])
    actual = str(game)
    assert expected == actual

def test_choose_move(game):
    game.set_board([0, 1, 2, 3])
    expected = 1
    actual = game.choose_move()
    assert expected == actual

def test_is_game_won(game):
    game.set_board([0, 1, 2, 3])
    expected = False
    actual = game.is_game_won()
    assert expected == actual

def test_plan_moves(game):
    game.set_board([0, 1, 2, 3])
    expected = [1, 2, 1, 3, 1]
    actual = game.plan_moves()
    assert expected == actual


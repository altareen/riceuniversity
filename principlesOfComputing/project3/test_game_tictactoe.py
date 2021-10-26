###
#-------------------------------------------------------------------------------
# test_game_tictactoe.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 23, 2021
# Run:      pytest -q test_game_tictactoe.py
#
# Description:
# This program implements the test bench for game_tictactoe.py
#
##

import game_tictactoe as game
import poc_ttt_provided as provided
import pytest

#def test_mc_trial():
#    expected = 
#    actual = 
#    assert expected == actual

@pytest.mark.parametrize("board_one, expected_one", [
    (provided.TTTBoard(3, False,
    [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
    [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
    [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]),
    [[1.0, 1.0, -1.0], [-1.0, 1.0, 0], [0, 1.0, -1.0]])
])

def test_mc_update_scores(board_one, expected_one):
    scores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game.mc_update_scores(scores, board_one, 2)
    actual = scores
    assert expected_one == actual

@pytest.mark.parametrize("board_two, expected_two", [
    (provided.TTTBoard(3, False,
    [[provided.EMPTY, provided.PLAYERX, provided.EMPTY],
    [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
    [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]),
    [(0, 2), (2, 1)])
])

def test_get_best_move(board_two, expected_two):
    actual = game.get_best_move(board_two, [[-3, 6, -2], [8, 0, -3], [3, -2, -4]])
    assert actual in expected_two

#def test_mc_move():
#    expected = 
#    actual = 
#    assert expected == actual


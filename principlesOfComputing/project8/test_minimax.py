###
#-------------------------------------------------------------------------------
# test_minimax.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 10, 2021
# Run:      pytest -q test_minimax.py
#
# Description:
# This program implements the test bench for minimax.py
#
##

import minimax as mini
import poc_ttt_provided as provided
import pytest

@pytest.mark.parametrize("board, player, expected", [
    (provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, (-1, (2, 1))),
    (provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), provided.PLAYERX, (1, (0, 0))),
    (provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERX, (1, (2, 1)))
])

def test_mm_move(board, player, expected):
    actual = mini.mm_move(board, player)
    assert expected == actual






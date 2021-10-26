###
#-------------------------------------------------------------------------------
# test_fifteen_puzzle.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 19, 2021
# Run:      pytest -q test_fifteen_puzzle.py
#
# Description:
# This program implements the test bench for fifteen_puzzle.py
#
##

import fifteen_puzzle as fift
import pytest

#lower_row_invariant(i, j)
#-------------------------

@pytest.mark.parametrize("target_row, target_col, expected", [
    (3, 1, True),
    (2, 2, False),
    (0, 1, False)
])

def test_lower_row_invariant(target_row, target_col, expected):
    game = fift.Puzzle(4, 4, [[4, 12, 1, 3], [5, 10, 2, 7], [8, 13, 6, 11], [9, 0, 14, 15]])
    actual = game.lower_row_invariant(target_row, target_col)
    assert expected == actual


# solve_interior_tile(i, j)
#--------------------------

@pytest.mark.parametrize("game, target_row, target_col, expected", [
    (fift.Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]]), 2, 2, "uulldrruldrulddruld"),
    (fift.Puzzle(3, 3, [[6, 7, 8], [5, 4, 3], [2, 1, 0]]), 2, 2, "uulddruld"),
    (fift.Puzzle(3, 3, [[6, 7, 2], [5, 4, 3], [8, 1, 0]]), 2, 2, "llurrdl"),
    (fift.Puzzle(3, 3, [[8, 7, 2], [5, 4, 3], [6, 1, 0]]), 2, 2, "uulldrruldrulddruld"),
    (fift.Puzzle(4, 4, [[4, 12, 1, 3], [5, 10, 2, 7], [8, 13, 6, 11], [9, 0, 14, 15]]), 3, 1, "uld"),
    (fift.Puzzle(4, 4, [[4, 12, 1, 3], [5, 10, 2, 7], [8, 9, 6, 11], [13, 0, 14, 15]]), 3, 1, "l"),
    (fift.Puzzle(4, 4, [[4, 12, 1, 3], [5, 10, 2, 7], [13, 9, 6, 11], [8, 0, 14, 15]]), 3, 1, "lurdl"),
    (fift.Puzzle(4, 4, [[4, 13, 1, 3], [5, 10, 2, 7], [8, 12, 6, 11], [9, 0, 14, 15]]), 3, 1, "uuulddrulddruld"),
    (fift.Puzzle(4, 4, [[4, 13, 1, 3], [5, 10, 2, 7], [8, 12, 6, 11], [14, 9, 0, 15]]), 3, 2, "llurrdl"),
    (fift.Puzzle(4, 4, [[14, 13, 1, 3], [5, 10, 2, 7], [8, 12, 6, 11], [4, 9, 0, 15]]), 3, 2, "uuulldrruldrulddrulddruld"),
    (fift.Puzzle(4, 4, [[9, 3, 1, 11], [5, 10, 2, 7], [8, 12, 6, 13], [4, 0, 14, 15]]), 3, 1, "urrulldrullddruld"),
    (fift.Puzzle(4, 4, [[9, 3, 1, 13], [5, 10, 2, 7], [8, 12, 6, 11], [4, 0, 14, 15]]), 3, 1, "uuurrdllurdlulddrulddruld")
])

def test_solve_interior_tile(game, target_row, target_col, expected):
    actual = game.solve_interior_tile(target_row, target_col)
    assert expected == actual


# solve_col0_tile(i)
#-------------------

@pytest.mark.parametrize("game, target_row, expected", [
    (fift.Puzzle(3, 3, [[5, 1, 2], [6, 4, 3], [0, 7, 8]]), 2, "urr"),
    (fift.Puzzle(3, 3, [[5, 6, 2], [1, 4, 3], [0, 7, 8]]), 2, "uurdlurdlruldrdlurdluurddlurr"),
    (fift.Puzzle(3, 3, [[5, 2, 6], [1, 4, 3], [0, 7, 8]]), 2, "uurrdllurdlurdlruldrdlurdluurddlurr"),
    (fift.Puzzle(4, 5, [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]]), 2, "uurrdllurdlurdlruldrdlurdluurddlurrrr"),
    (fift.Puzzle(4, 5, [[8, 2, 10, 9, 1], [7, 6, 5, 4, 3], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]), 2, "uurrdllurdlurdlruldrdlurdluurddlurrrr"),
    (fift.Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]]), 2, "urr"),
])

def test_solve_col0_tile(game, target_row, expected):
    actual = game.solve_col0_tile(target_row)
    assert expected == actual


# solve_row1_tile(j)
#-------------------

@pytest.mark.parametrize("game, target_col, expected", [
    (fift.Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]]), 2, "uldru"),
    (fift.Puzzle(4, 5, [[7, 6, 5, 3, 4], [2, 1, 0, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]), 2, "ulldrruldru"),
    (fift.Puzzle(4, 5, [[7, 6, 5, 3, 2], [4, 1, 9, 8, 0], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]), 4, "llurrdlur")
])

def test_solve_row1_tile(game, target_col, expected):
    actual = game.solve_row1_tile(target_col)
    assert expected == actual


# solve_row0_tile(j)
#-------------------

@pytest.mark.parametrize("game, target_col, expected", [
    (fift.Puzzle(3, 3, [[4, 2, 0], [1, 3, 5], [6, 7, 8]]), 2, "ld"),
    (fift.Puzzle(3, 3, [[4, 1, 0], [3, 2, 5], [6, 7, 8]]), 2, "lldurdlurrdluldrruld"),
    (fift.Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]]), 2, "ldlurdlurrdluldrruld"),
    (fift.Puzzle(4, 5, [[7, 6, 5, 3, 0], [4, 8, 2, 1, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]), 4, "ldlllurrdlurrdlurdlurrdluldrruld"),
])

def test_solve_row0_tile(game, target_col, expected):
    actual = game.solve_row0_tile(target_col)
    assert expected == actual


# solve_2x2()
#------------

@pytest.mark.parametrize("game, expected", [
    (fift.Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]]), "ulrdlurdlu"),
    (fift.Puzzle(3, 3, [[3, 1, 2], [4, 0, 5], [6, 7, 8]]), "lu")
])

def test_solve_2x2(game, expected):
    actual = game.solve_2x2()
    assert expected == actual


# solve_puzzle()
#---------------

@pytest.mark.parametrize("game, expected", [
    (fift.Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]]), "uulldrruldrulddrulduulddrulduurrdllurdlurdlruldrdlurdluurddlurrllurrdlurldlu"),
    (fift.Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]]), "lddduuurdlulddrulddrulduuurdlurddlurdlruldrdlurdluurddlurrrrlllluurdlruldrdlurdluurddlurrrrlurldlurlduldlurdlurrdluldrruldulrdlurdlu"),
    (fift.Puzzle(5, 4, [[5, 4, 2, 3], [1, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19]]), "ulrdlurdlu"),
    (fift.Puzzle(3, 6, [[16, 7, 13, 17, 5, 9], [3, 0, 14, 10, 12, 6], [4, 15, 2, 11, 8, 1]]), "rrrrduulldrruldrulddrulduulllldrruldrruldrruldrulddruldllurrdlulldrruldruldulduurrrdllurdllurdlurdlruldrdlurdluurddlurrrrrllurrdlurlldruldurdlurrdluldrruldllllurrdlurrdlurrdlurldllurrdlurdlurrdluldrrulduldllurrdlurdlurrdluldrruldulldurdlurrdluldrruldul"),
    (fift.Puzzle(2, 4, [[0, 3, 2, 7], [4, 5, 6, 1]]), "rrrduldrullldruldurrdlurdlurrdluldrruldlurldlu"),
])

def test_solve_puzzle(game, expected):
    actual = game.solve_puzzle()
    assert expected == actual


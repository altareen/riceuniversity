###
#-------------------------------------------------------------------------------
# test_zombie_apocalypse.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 29, 2021
# Run:      pytest -q test_zombie_apocalypse.py
#
# Description:
# This program implements the test bench for zombie_apocalypse.py
#
##

import zombie_apocalypse as zoma
import pytest

@pytest.mark.parametrize("row, col, expected", [
    (1, 1, 1)
])

def test_add_zombie(row, col, expected):
    game = zoma.Apocalypse(3, 3, [], [], [(1, 1)])
    game.add_zombie(row, col)
    actual = game.num_zombies()
    assert expected == actual

@pytest.mark.parametrize("row, col, expected", [
    (1, 1, 1)
])

def test_add_zombie(row, col, expected):
    game = zoma.Apocalypse(3, 3, [], [(1, 1)], [])
    game.add_human(row, col)
    actual = game.num_humans()
    assert expected == actual

@pytest.mark.parametrize("entity_type, expected", [
    (zoma.HUMAN, [[4, 3, 2],[3, 2, 1],[2, 1, 0]])
])

def test_compute_distance_field_human(entity_type, expected):
    game = zoma.Apocalypse(3, 3, [], [], [(2, 2)])
    actual = game.compute_distance_field(entity_type)
    assert expected == actual
 
@pytest.mark.parametrize("entity_type, expected", [
    (zoma.ZOMBIE, [[2, 1, 2],[1, 0, 1],[2, 1, 2]])
])

def test_compute_distance_field_zombie(entity_type, expected):
    game = zoma.Apocalypse(3, 3, [], [(1, 1)], [])
    actual = game.compute_distance_field(entity_type)
    assert expected == actual

@pytest.mark.parametrize("dist, expected", [
    ([[4, 3, 2], [3, 2, 1], [2, 1, 0]], [(0, 0)])
])

def test_move_humans(dist, expected):
    game = zoma.Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
    game.move_humans(dist)
    actual = list(game.humans())
    assert expected == actual
    
@pytest.mark.parametrize("dist, expected", [
    ([[2, 1, 2], [1, 0, 1], [2, 1, 2]], [(1, 1)])
])

def test_move_humans(dist, expected):
    game = zoma.Apocalypse(3, 3, [], [(1, 1)], [(1, 1)])
    game.move_zombies(dist)
    actual = list(game.zombies())
    assert expected == actual


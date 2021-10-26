###
#-------------------------------------------------------------------------------
# test_word_wrangler.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 05, 2021
# Run:      pytest -q test_word_wrangler.py
#
# Description:
# This program implements the test bench for word_wrangler.py
#
##

import word_wrangler as wra
import pytest

@pytest.mark.parametrize("list1, expected", [
    ([2, 2, 2, 3, 5, 8, 8], [2, 3, 5, 8])
])

def test_remove_duplicates(list1, expected):
    actual = wra.remove_duplicates(list1)
    assert expected == actual

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 5, 7, 9, 11, 15, 19], [2, 3, 4, 6, 7, 9, 10, 15], [2, 7, 9, 15])
])

def test_intersect(list1, list2, expected):
    actual = wra.intersect(list1, list2)
    assert expected == actual

@pytest.mark.parametrize("list1, list2, expected", [
    ([12, 18, 24, 39, 48, 54, 62], [10, 16, 25, 34, 45, 51, 61], [10, 12, 16, 18, 24, 25, 34, 39, 45, 48, 51, 54, 61, 62])
])

def test_merge(list1, list2, expected):
    actual = wra.merge(list1, list2)
    assert expected == actual

@pytest.mark.parametrize("list1, expected", [
    ([90, 38, 17, 54, 3, 85], [3, 17, 38, 54, 85, 90])
])

def test_merge_sort(list1, expected):
    actual = wra.merge_sort(list1)
    assert expected == actual

@pytest.mark.parametrize("word, expected", [
    ("ox", ['', 'x', 'o', 'ox', 'xo'])
])

def test_gen_all_strings(word, expected):
    actual = wra.gen_all_strings(word)
    assert expected == actual


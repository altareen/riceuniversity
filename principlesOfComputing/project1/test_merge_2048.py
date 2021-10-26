###
#-------------------------------------------------------------------------------
# test_merge_2048.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 10, 2021
# Run:      pytest -q test_merge_2048.py
#
# Description:
# This program implements the test bench for merge_2048.py
#
##

from merge_2048 import *

class Test2048:
    def test_one(self):
        expected = [4, 4, 0, 0]
        actual = merge([2, 0, 2, 4])
        assert expected == actual
    
    def test_two(self):
        expected = [4, 0, 0, 0]
        actual = merge([0, 0, 2, 2])
        assert expected == actual

    def test_three(self):
        expected = [4, 0, 0, 0]
        actual = merge([2, 2, 0, 0])
        assert expected == actual

    def test_four(self):
        expected = [4, 4, 2, 0, 0]
        actual = merge([2, 2, 2, 2, 2])
        assert expected == actual

    def test_five(self):
        expected = [8, 32, 8, 0]
        actual = merge([8, 16, 16, 8])
        assert expected == actual


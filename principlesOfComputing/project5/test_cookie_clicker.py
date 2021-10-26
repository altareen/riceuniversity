###
#-------------------------------------------------------------------------------
# test_cookie_clicker.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Sep 28, 2021
# Run:      pytest -q test_cookie_clicker.py
#
# Description:
# This program implements the test bench for cookie_clicker.py
#
##

import cookie_clicker as sim
import pytest

@pytest.mark.parametrize("strategy_name, time, strategy, expected", [
    ("Cursor", 10000000000.0, sim.strategy_cursor_broken, 6965195661.5)
])

def test_get_cookies(strategy_name, time, strategy, expected):
    clicker = sim.run_strategy(strategy_name, time, strategy)
    actual = clicker.get_cookies()
    assert expected == pytest.approx(actual, 0.1)

@pytest.mark.parametrize("strategy_name, time, strategy, expected", [
    ("Cursor", 10000000000.0, sim.strategy_cursor_broken, 16.1)
])

def test_get_cps(strategy_name, time, strategy, expected):
    clicker = sim.run_strategy(strategy_name, time, strategy)
    actual = clicker.get_cps()
    assert expected == pytest.approx(actual, 0.1)

@pytest.mark.parametrize("strategy_name, time, strategy, expected", [
    ("Cursor", 10000000000.0, sim.strategy_cursor_broken, 153308849166.0)
])

def test_get_history(strategy_name, time, strategy, expected):
    clicker = sim.run_strategy(strategy_name, time, strategy)
    actual = clicker.get_history()[-1][3]
    assert expected == pytest.approx(actual, 0.1)




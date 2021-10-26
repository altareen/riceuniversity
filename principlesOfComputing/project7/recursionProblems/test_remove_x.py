###
#-------------------------------------------------------------------------------
# test_remove_x.py
#-------------------------------------------------------------------------------
#
# Author:   Alwin Tareen
# Created:  Oct 04, 2021
# Run:      pytest -q test_remove_x.py
#
# Description:
# This program implements the test bench for remove_x.py
#
##

import remove_x as rex
import pytest

@pytest.mark.parametrize("my_string, expected", [
    ("catxxdogx", "catdog"),
    ("xmoxxuse", "mouse"),
    ("elephant", "elephant"),
    ("axlsekjxxfeoxxxwi", "alsekjfeowi"),
    ("slxkfjxxweoixjsei", "slkfjweoijsei"),
    ("oaxxiwxxefxxslxxekxxjfewo", "oaiwefslekjfewo"),
    ("aoxfixxejxxxoexxijsoxiosiej", "aofiejoeijsoiosiej"),
    ("oixxxfexjxosxxeixxfxjxxseoxxxfisxsxefse", "oifejoseifjseofissefse"),
    ("omxxxaexixjxfxaoxxxesxixfxaxosimxeufoxxeismfo", "omaeijfaoesifaosimeufoeismfo"),
    ("sixxeuxfxhseixxufmxhxseixxfsxxuiexfmseifusif", "sieufhseiufmhseifsuiefmseifusif")
])

def test_is_member(my_string, expected):
    actual = rex.remove_x(my_string)
    assert expected == actual


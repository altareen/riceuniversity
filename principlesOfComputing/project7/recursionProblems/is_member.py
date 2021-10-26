"""
|-------------------------------------------------------------------------------
| is_member.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 is_member.py
|
| Description:
| This program determines if an element is a member of a list.
|
"""

def is_member(my_list, elem):
    if len(my_list) == 0:
        return False
    elif my_list[-1] == elem:
        return True
    else:
        return is_member(my_list[:-1], elem)

result = is_member(['c', 'a', 't'], 'a')
print(result)


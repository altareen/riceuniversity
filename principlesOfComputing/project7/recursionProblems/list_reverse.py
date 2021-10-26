"""
|-------------------------------------------------------------------------------
| list_reverse.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 list_reverse.py
|
| Description:
| This program reverses the elements in a list.
|
"""

def list_reverse(my_list):
    if len(my_list) == 0:
        return []
    else:
        return my_list[-1:] + list_reverse(my_list[:-1])

result = list_reverse([2, 3, 1])
print(result)


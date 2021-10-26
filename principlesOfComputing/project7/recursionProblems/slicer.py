"""
|-------------------------------------------------------------------------------
| slice.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 slicer.py
|
| Description:
| This program performs the slice function of a list.
|
"""

def slicer(my_list, first, last):
    if len(my_list) == 0:
        return []
    elif first < len(my_list) <= last:
        item = my_list.pop()
        return slicer(my_list, first, last) + [item]
    else:
        my_list.pop()
        return slicer(my_list, first, last)

result = slicer(['a', 'b', 'c', 'd', 'e'], 2, 4)
print(result)


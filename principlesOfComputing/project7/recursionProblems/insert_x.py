"""
|-------------------------------------------------------------------------------
| insert_x.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 insert_x.py
|
| Description:
| This program adds the character "x" between each pair of consecutive characters
| in the string.
|
"""

def insert_x(my_string):
    if len(my_string) == 1:
        return my_string
    else:
        return insert_x(my_string[:-1]) + "x" + my_string[-1]

result = insert_x("catdog")
print(result)


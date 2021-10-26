"""
|-------------------------------------------------------------------------------
| remove_x.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 remove_x.py
|
| Description:
| This program deletes all occurrences of the character "x" from the string.
|
"""

def remove_x(my_string):
    if len(my_string) == 0:
        return ""
    else:
        result = ""
        if my_string[-1] != "x":
            result = my_string[-1]
        return remove_x(my_string[:-1]) + result

result = remove_x("catxxdogx")
print(result)


"""
|-------------------------------------------------------------------------------
| triangular_sum.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 triangular_sum.py
|
| Description:
| This program computes the nth triangular number.
|
"""

def triangular_sum(num):
    if num == 0:
        return 0
    else:
        return num + triangular_sum(num-1)

result = triangular_sum(5)
print(result)


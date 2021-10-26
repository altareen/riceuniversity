"""
|-------------------------------------------------------------------------------
| number_of_threes.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 number_of_threes.py
|
| Description:
| This program determines the number of times the digit 3 appears in a number.
|
"""

def number_of_threes(num):
    if num == 0:
        return 0
    else:
        digit = num%10
        count = 0
        if digit == 3:
            count = 1
        num = int(num/10)
        return count + number_of_threes(num)

result = number_of_threes(34534)
print(result)


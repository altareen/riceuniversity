"""
|-------------------------------------------------------------------------------
| gray_to_bin.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 gray_to_bin.py
|
| Description:
| This program computes the decimal value of the binary number.
|
"""

def gray_to_bin(num):
    if len(num) == 1:
        return num
    else:
        most_significant = gray_to_bin(num[:-1])
        least = (int(num[-1]) + int(most_significant[-1])) % 2
        return most_significant + str(least)

result = gray_to_bin("100")
print(result)


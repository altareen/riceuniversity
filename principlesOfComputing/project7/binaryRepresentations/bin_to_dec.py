"""
|-------------------------------------------------------------------------------
| bin_to_dec.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 bin_to_dec.py
|
| Description:
| This program computes the decimal value of the binary number.
|
"""

def bin_to_dec(num):
    if len(num) == 0:
        return 0
    else:
        return 2**(len(num)-1) * int(num[0]) + bin_to_dec(num[1:])

result = bin_to_dec("1111")
print(result)


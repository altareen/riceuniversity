"""
|-------------------------------------------------------------------------------
| gcd.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 gcd.py
|
| Description:
| This program computes the greatest common divisor of num1 and num2.
|
"""

def gcd(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)

result = gcd(270, 192)
print(result)


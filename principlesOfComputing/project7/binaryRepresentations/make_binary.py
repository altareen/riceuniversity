"""
|-------------------------------------------------------------------------------
| make_binary.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 make_binary.py
|
| Description:
| This program returns a list of all binary numbers of length n.
|
"""

def make_binary(n):
    if n == 0:
        return [""]
    else:
        nums = make_binary(n-1)
        clone = nums[:]
        for i in range(len(nums)):
            nums[i] = "0" + nums[i]
        for i in range(len(clone)):
            clone[i] = "1" + clone[i]
        nums.extend(clone)
        return nums

result = make_binary(4)
print(result)


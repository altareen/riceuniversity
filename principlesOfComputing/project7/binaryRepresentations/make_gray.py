"""
|-------------------------------------------------------------------------------
| make_gray.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 make_gray.py
|
| Description:
| This program returns a list of all gray coded numbers of length n.
|
"""

def make_gray(n):
    if n == 0:
        return [""]
    else:
        nums = make_gray(n-1)
        clone = nums[:]
        clone.reverse()
        for i in range(len(nums)):
            nums[i] = "0" + nums[i]
        for i in range(len(clone)):
            clone[i] = "1" + clone[i]
        nums.extend(clone)
        return nums

result = make_gray(4)
print(result)


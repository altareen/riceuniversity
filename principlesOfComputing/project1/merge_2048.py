"""
|-------------------------------------------------------------------------------
| merge_2048.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 10, 2021
| Run:      python3 merge_2048.py
|
| Description:
| This program implements a function that merges a single row or column in 2048.
|
"""

def merge(line):
    """
    Given a `line` (a list of integers), return a list which represents all of
    the integers having undergone a merge operation, according to the rules of
    the 2048 game.
    
    Note that all of the integers should be merged towards the front of the
    list, that is, towards index 0.
    """
    # Slide all of the integers leftward
    partial = list(filter(lambda x: x > 0, line[:]))
    partial.extend([0] * (len(line) - len(partial)))
    
    # Combine the integers into pairs
    idx = 0
    while idx < len(partial)-1:
        if partial[idx] == partial[idx+1]:
            partial[idx] *= 2
            partial[idx+1] = 0
            idx += 2
        else:
            idx += 1
    
    # Slide all of the integers leftward
    result = list(filter(lambda x: x > 0, partial[:]))
    result.extend([0] * (len(line) - len(result)))
    return result


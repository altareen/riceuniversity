"""
|-------------------------------------------------------------------------------
| game_simpledice.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 24, 2021
| Run:      python3 game_simpledice.py
|
| Description:
| This program analyzes the expected value of a simple dice game.
|
"""

import random


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans


def max_repeats(seq):
    """
    Compute the maximum number of times that an outcome is repeated
    in a sequence
    """
    return max([seq.count(x) for x in seq])


def compute_expected_value():
    """
    Function to compute expected value of simple dice game
    """
    doubles = 0
    triples = 0
    outcomes = set([1, 2, 3, 4, 5, 6])
    sequences = gen_all_sequences(outcomes, 3)
    
    for sequence in sequences:
        result = max_repeats(sequence)
        if result == 2:
            doubles += 1
        elif result == 3:
            triples += 1
    
    return round(10.0*doubles/len(sequences) + 200.0*triples/len(sequences), 2)


def run_test():
    """
    Testing code, note that the initial cost of playing the game
    has been subtracted
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    print("All possible sequences of three dice are")
    print(gen_all_sequences(outcomes, 3))
    print()
    print("Test for max repeats")
    print("Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2)))
    print("Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2)))
    print("Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3)))
    print()
    print(f"Ignoring the initial $10, the expected value was ${compute_expected_value()}")
    
run_test()


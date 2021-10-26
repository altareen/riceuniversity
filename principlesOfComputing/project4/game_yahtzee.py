"""
|-------------------------------------------------------------------------------
| game_yahtzee.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 24, 2021
| Run:      python3 game_yahtzee.py
|
| Description:
| This program implements a strategy function in the game of Yahtzee.
|
"""


# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    return max([hand.count(x)*x for x in hand])


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    result = 0.0
    outcomes = set(range(1, num_die_sides+1))
    sequences = gen_all_sequences(outcomes, num_free_dice)
    for sequence in sequences:
        result += 1.0 * score(held_dice + tuple(sequence)) / num_die_sides**num_free_dice
    return result


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    if len(hand) == 0:
        return set([()])
    else:
        result = set()
        first = hand[0]
        others = hand[1:]
        entries = gen_all_holds(others)
        for item in entries:
            result.add(item)
            combine = item + (first,)
            ordered = tuple(sorted(list(combine)))
            result.add(ordered)
        return result
        

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    largest = 0.0
    holds = gen_all_holds(hand)
    for hold in holds:
        exp_value = expected_value(hold, num_die_sides, len(hand)-len(hold))
        if exp_value > largest:
            largest = exp_value
            best_hold = hold
    return (largest, best_hold)


#def run_example():
#    """
#    Compute the dice to hold and expected score for an example hand
#    """
#    num_die_sides = 6
#    hand = (1, 1, 1, 5, 6)
#    hand_score, hold = strategy(hand, num_die_sides)
#    print("Best strategy for hand {hand} is to hold {hold} with expected score {hand_score}")


#run_example()
#print(expected_value((2, 2), 6, 2))
#print(gen_all_holds((1, 2, 3)))
#print(strategy((1,), 6))


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)


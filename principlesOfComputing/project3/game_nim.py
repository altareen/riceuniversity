"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
#import codeskulptor
#codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def play_random_game(start_items):
    current_items = start_items
    while True:
        comp_move = random.randint(1, MAX_REMOVE)
        current_items -= comp_move
        if current_items <= 0:
            return 0
        player_move = random.randint(1, MAX_REMOVE)
        current_items -= player_move
        if current_items <= 0:
            return 1


def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    # Insert your code here
    initial_moves = range(1, MAX_REMOVE+1)
    overall_wins = {x: 0.0 for x in initial_moves}
    for move in initial_moves:
        num_items -= move
        event = 0
        for trial in range(TRIALS):
            event += play_random_game(num_items)
        overall_wins[move] = 1.0*event/TRIALS        
    return max(overall_wins, key=overall_wins.get)


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print(f"Starting game with value {current_items}")
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print(f"Computer choose {comp_move} current value is {current_items}")
        if current_items <= 0:
            print("Computer wins")
            break
        player_move = int(input("Enter your current move: "))
        current_items -= player_move
        print(f"Player choose {player_move} current value is {current_items}")
        if current_items <= 0:
            print("Player wins")
            break

#play_game(21)
play_game(9)
    
                 
    

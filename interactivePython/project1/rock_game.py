"""
|-------------------------------------------------------------------------------
| rock_game.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Jun 10, 2015
| Execute:  python3 rock_game.py
|
| This program implements the rock-paper-scissors-lizard-Spock game.
|
| Codeskulptor link:
| https://py2.codeskulptor.org/#user2-idPIJmB1Tm-11.py
|
"""

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        hand_signal = 'rock'
    elif number == 1:
        hand_signal = 'Spock'
    elif number == 2:
        hand_signal = 'paper'
    elif number == 3:
        hand_signal = 'lizard'
    else:
        hand_signal = 'scissors'

    return hand_signal
    
def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        signal_number = 0
    elif name == 'Spock':
        signal_number = 1
    elif name == 'paper':
        signal_number = 2
    elif name == 'lizard':
        signal_number = 3
    else:
        signal_number = 4
        
    return signal_number

def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # compute difference of player_number and comp_number modulo five
    determinator = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner
    if (determinator == 4) or (determinator == 3):
        victory_defeat = 'Player wins!'
    elif (determinator == 2) or (determinator == 1):
        victory_defeat = 'Computer wins!'
    else:
        victory_defeat = 'Player and computer tie!'
    
    # convert comp_number to name using number_to_name
    comp_name = number_to_name(comp_number)
    
    # print results
    print 'Player chooses', name
    print 'Computer chooses', comp_name
    print victory_defeat
    print ''

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


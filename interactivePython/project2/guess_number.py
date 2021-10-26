"""
|-------------------------------------------------------------------------------
| guess_number.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Jun 12, 2015
| Execute:  python3 guess_number.py
|
| This program implements the guess the number game.
|
| Codeskulptor link:
| https://py2.codeskulptor.org/#user2-9mGfc4QQDe-28.py
|
"""

import simplegui
import random
import math

# initialize global variables used in your code
number_range = 100
remaining_guesses = 7
secret_number = 0

# helper function to initial game
def init():
    global secret_number
    secret_number = random.randrange(0, number_range)
    print "New game. Range is from 0 to", number_range
    print "Number of remaining guesses is", remaining_guesses, "\n"
    
# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global number_range, remaining_guesses
    number_range = 100
    remaining_guesses = 7
    init()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global number_range, remaining_guesses
    number_range = 1000
    remaining_guesses = 10
    init()

    
def get_input(guess):
    # main game logic goes here
    global remaining_guesses
    player_guess = int(guess)

    # decrement and display the quantity of remaining guesses
    remaining_guesses -= 1
    print "Guess was", player_guess
    print "Number of remaining guesses is", remaining_guesses     
    
    # Check if the player discovered the secret number
    if (secret_number == player_guess):
        print "Correct!\n"
        if (number_range == 100):
            range100()
        else:
            range1000()    
    # Check for game termination condition
    elif (remaining_guesses == 0):
        print "You have exhausted all of your guesses."
        print "The secret number was", secret_number
        print "Game over!\n"
        if (number_range == 100):
            range100()
        else:
            range1000()        
    elif (secret_number < player_guess):     
        print "Lower!\n"
    else:
        print "Higher!\n"    
    

# create frame
game_frame = simplegui.create_frame("Guess the number", 200, 200)

# create control elements for frame
game_frame.add_button("Range is [0, 100)", range100, 200)
game_frame.add_button("Range is [0, 1000)", range1000, 200)
game_frame.add_input("Enter a guess", get_input, 200)

init()

# register event handlers for control elements

# start frame
game_frame.start()



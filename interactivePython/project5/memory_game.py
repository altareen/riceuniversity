"""
|-------------------------------------------------------------------------------
| memory_game.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Jun 28, 2015
| Execute:  python3 memory_game.py
|
| This program implements the memory game.
|
| Codeskulptor link:
| https://py2.codeskulptor.org/#user5-gzATlXBWGN-4.py
|
"""

import simplegui
import random

# helper function to initialize globals
def init():
    global state, card_deck, exposed, first_card, second_card, turn_count
    state = 0
    first_card = 0
    second_card = 0
    turn_count = 0

    # create a list consisting of 16 numbers
    # with each number lying in the range [0,8) and appearing twice
    card_deck = [i % 8 for i in range(16)]

    # shuffle the deck
    random.shuffle(card_deck)

    # create a list 'exposed' such that:
    # True == card flipped over, False == card hidden
    exposed = [False for i in range(16)]

# define event handlers
def mouseclick(pos):
    global state, first_card, second_card, turn_count
    clicked_card = pos[0] // 50
    
    if not(exposed[clicked_card]):
        exposed[clicked_card] = True
        
        if state == 0:
            first_card = clicked_card
            turn_count += 1
            state = 1
        elif state == 1:
            second_card = clicked_card
            state = 2
        else:
            if (card_deck[first_card] != card_deck[second_card]):
                exposed[first_card] = False
                exposed[second_card] = False
            first_card = clicked_card
            turn_count += 1
            state = 1 
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_deck, exposed
    placement = [0, 70]
    
    # draw the number associated with each card on the canvas
    for i in range(16):
        if (exposed[i] == True):
            placement[0] += 10
            canvas.draw_text(str(card_deck[i]), placement, 40, "White")
            placement[0] -= 10
        else:
            canvas.draw_line([i*50+25, 0], [i*50+25, 100], 50, "Green")
            canvas.draw_line([i*50, 0], [i*50, 100], 2, "Brown")           
        placement[0] += 50
        
    # update the turn count
    l.set_text("Moves = " + str(turn_count))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


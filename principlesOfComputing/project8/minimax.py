"""
|-------------------------------------------------------------------------------
| minimax.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 09, 2021
|
| Run:      python3 minimax.py
|
| Description:
| This program analyzes a Tic-Tac-Toe game using the minimax algorithm.
|
"""

#import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#import codeskulptor
#codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)
    options = dict()
    largest = -2
    for square in board.get_empty_squares():
        child = board.clone()
        child.move(square[0], square[1], player)
        score = mm_move(child, provided.switch_player(player))[0]
        options[(square[0], square[1])] = score
        if player == provided.PLAYERX:
            largest = max(options, key=options.get)
        elif player == provided.PLAYERO:
            largest = min(options, key=options.get)
    return options[largest], largest

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)


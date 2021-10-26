"""
|-------------------------------------------------------------------------------
| game_tictactoe.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 23, 2021
| Run:      python3 game_tictactoe.py
|
| Description:
| This program implements the Tic-Tac-Toe game with a Monte Carlo simulator.
|
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.

NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trial(board, player):
    """
    Simulate a single game with random moves
    """
    while board.check_win() is None:
        empty = board.get_empty_squares()
        square = random.choice(empty)
        board.move(square[0], square[1], player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    Score the completed board and update the scores grid
    """
    opponent = provided.switch_player(player)
    dim = board.get_dim()

    if board.check_win() == player:    
        for idx in range(dim):
            for jdx in range(dim):
                if board.square(idx, jdx) == player:
                    scores[idx][jdx] += SCORE_CURRENT
                elif board.square(idx, jdx) == opponent:
                    scores[idx][jdx] -= SCORE_OTHER
    elif board.check_win() == opponent:
        for idx in range(dim):
            for jdx in range(dim):
                if board.square(idx, jdx) == opponent:
                    scores[idx][jdx] += SCORE_CURRENT
                elif board.square(idx, jdx) == player:
                    scores[idx][jdx] -= SCORE_OTHER


def get_best_move(board, scores):
    """
    Return an empty square with the maximum score
    """
    empty = board.get_empty_squares()
    largest = float('-inf')
    move = random.choice(empty)
    for square in empty:
        if scores[square[0]][square[1]] > largest:
            largest = scores[square[0]][square[1]]
            move = square
    return move


def mc_move(board, player, trials):
    """
    Use a Monte Carlo simulation to return a move for the machine player
    """
    dim = board.get_dim()
    scores = [[0 for dummy_col in range(dim)] for dummy_row in range(dim)]
    for dummy_trial in range(trials):
        simulate_board = board.clone()
        mc_trial(simulate_board, player)
        mc_update_scores(scores, simulate_board, player)
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


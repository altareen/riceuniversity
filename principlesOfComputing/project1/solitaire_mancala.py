"""
|-------------------------------------------------------------------------------
| merge_2048.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 12, 2021
| Run:      python3 solitaire_mancala.py
|
| Description:
| This program implements the Solitaire Mancala game, in which the goal is to
| move as many seeds from given houses into the store.
|
"""

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = configuration[:]
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self._board)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        return self._board[1:] == [0]*(len(self._board)-1)
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == 0:
            return False
        else:
            return house_num == self.get_num_seeds(house_num)
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if house_num != 0:
            self._board[house_num] = 0
            for house in range(house_num-1, -1, -1):
                self._board[house] += 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for house_num in range(1, len(self._board)):
            if self.is_legal_move(house_num):
                return house_num
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
		After each move, move the seeds in the house closest to the store 
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        clone_board = self._board[:]
        legal_moves = []
        house_num = 1
        while house_num < len(clone_board):
            if house_num == clone_board[house_num]:
                legal_moves.append(house_num)
                clone_board[house_num] = 0
                for house in range(house_num-1, -1, -1):
                    clone_board[house] += 1
                house_num = 1
            else:
                house_num += 1
        return legal_moves

# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())


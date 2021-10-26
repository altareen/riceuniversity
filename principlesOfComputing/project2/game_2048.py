"""
|-------------------------------------------------------------------------------
| game_2048.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 16, 2021
| Run:      python3 game_2048.py
|
| Description:
| This program implements the full version of the 2048 game.
|
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

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


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializes the TwentyFortyEight class.
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._board = []
        self._initial_tiles = {UP: [(0, j) for j in range(grid_width)], DOWN: [(grid_height-1, j) for j in range(grid_width)], LEFT: [(i, 0) for i in range(grid_height)], RIGHT: [(i, grid_width-1) for i in range(grid_height)]}
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = ""
        for row in self._board:
            result += str(row) + "\n"
        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_tiles = self._initial_tiles[direction]
        offset = OFFSETS[direction]
        create_tile = False
        
        limit = self._grid_width
        if direction in [UP, DOWN]:
            limit = self._grid_height
        
        for place in initial_tiles:
            coords = []
            coords.append(place)
            tile = place[:]
            for dummy_num in range(1, limit):
                tile = (tile[0]+offset[0], tile[1]+offset[1])
                coords.append(tile)
            print(coords)
            extracted = [self._board[pos[0]][pos[1]] for pos in coords]
            result = merge(extracted)
            for idx in range(len(coords)):
                self.set_tile(coords[idx][0], coords[idx][1], result[idx])
            
            if extracted != result:
                create_tile = True
        
        if create_tile:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile = 4
        if random.random() < 0.9:
            tile = 2
        zero_locations = [(i, j) for i in range(self._grid_height) for j in range(self._grid_width) if self._board[i][j] == 0]
        pick = random.choice(zero_locations)
        self._board[pick[0]][pick[1]] = tile

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

#game = TwentyFortyEight(4, 4)
#print(game)
#print(game.move(UP))
#print(game)




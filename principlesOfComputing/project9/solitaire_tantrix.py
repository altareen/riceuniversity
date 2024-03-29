"""
|-------------------------------------------------------------------------------
| solitaire_tantrix.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 10, 2021
|
| Run:      python3 solitaire_tantrix.py
|
| Description:
| Game is played on a grid of hexagonal tiles.
| All ten tiles for Tantrix Solitaire and place in a corner of the grid.
| Click on a tile to rotate it. Cick and drag to move a tile.
| The goal is to position the 10 provided tiles to form a yellow, red or blue
| loop of length 10.
|
"""

# Core modeling idea - a triangular grid of hexagonal tiles are 
# model by integer tuples of the form (i, j, k) 
# where i + j + k == size and i, j, k >= 0.

# Each hexagon has a neighbor in one of six directions
# These directions are modeled by the differences between the 
# tuples of these adjacent tiles

# Numbered directions for hexagonal grid, ordered clockwise at 60 degree intervals
DIRECTIONS = {0 : (-1, 0, 1), 1 : (-1, 1, 0), 2 : (0, 1, -1), 
              3 : (1, 0, -1), 4 : (1, -1, 0), 5 : (0,  -1, 1)}

def reverse_direction(direction):
    """
    Helper function that returns opposite direction on hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions / 2) % num_directions

# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]

# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 4


class Tantrix:
    """
    Basic Tantrix game class
    """
    
    def __init__(self, size):
        """
        Create a triangular grid of hexagons with size + 1 tiles on each side.
        """
        assert size >= MINIMAL_GRID_SIZE
        pass

        # Initialize dictionary tile_value to contain codes for ten
        # tiles in Solitaire Tantrix in one 4x4 corner of grid
        self.size = size
        self.tile_value = dict()
        positions = []
        factor = len(SOLITAIRE_CODES) - self.size
        k = self.size
        for num in range(factor):
            ipos = list(range(num+1))
            ipos.reverse()
            for j in range(num+1):
                positions.append((ipos[j], j, k))
            k -= 1
        for i in range(len(positions)):
            self.tile_value[positions[i]] = SOLITAIRE_CODES[i]

    def __str__(self):
        """
        Return string of dictionary of tile positions and values
        """
        return str(self.tile_value)
        
    def get_tiling_size(self):
        """
        Return size of board for GUI
        """
        return self.size
    
    def tile_exists(self, index):
        """
        Return whether a tile with given index exists
        """
        return index in self.tile_value
    
    def place_tile(self, index, code):
        """
        Play a tile with code at cell with given index
        """
        self.tile_value[index] = code

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index
        and return the code value for that tile
        """
        return self.tile_value.pop(index)
               
    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        """
        code = get_code(index)
        rotated = code[-1] + code[:-1]
        self.place_tile(index, rotated)

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        """
        return self.tile_value[index]

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in given direction
        """
        factor = DIRECTIONS[direction]
        return (index[0]+factor[0], index[1]+factor[1], index[2]+factor[2])

    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for adjacent tiles
        """
        for tile in self.tile_value:
            for direction in DIRECTIONS.keys():
                neighbor = self.get_neighbor(tile, direction)
                if self.tile_exists(neighbor):
                    if self.get_code(tile)[direction] != self.get_code(neighbor)[reverse_dirction(direction)]:
                        return False
        return True
        
    def has_loop(self, color):
        """
        Check whether a tile configuration has a loop of size 10 of given color
        """
        # TODO
        return False


# run GUI for Tantrix
#import poc_tantrix_gui
#poc_tantrix_gui.TantrixGUI(Tantrix(6))

game = Tantrix(6)
print(game)

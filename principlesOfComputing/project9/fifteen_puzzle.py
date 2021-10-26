"""
|-------------------------------------------------------------------------------
| fifteen_puzzle.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 10, 2021
|
| Run:      python3 fifteen_puzzle.py
|
| Description:
| This program solves the Fifteen puzzle.
| Note that solved configuration has the blank(zero) tile in upper left.
| Use the arrows key to swap this tile with its neighbors.
|
| Codeskulptor Link:
| https://py2.codeskulptor.org/#user48_juzU6X12Kw_4.py
|
"""

#import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # replace with your code
        if self.get_number(target_row, target_col) != 0:
            return False
        
        for row in range(target_row + 1, self.get_height()):
            for col in range(self.get_width()):
                if (row, col) != self.current_position(row, col):
                    return False

        for col in range(target_col + 1, self.get_width()):
            if (target_row, col) != self.current_position(target_row, col):
                return False

        return True


    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        moves = ""
        tile = self.current_position(target_row, target_col)
        diff = (target_row - tile[0], target_col - tile[1])

        # case 1: target tile is directly above the zero tile
        if (target_row-1, target_col) == tile:
            moves += "uld"
        # case 2: target tile is directly to the left of the zero tile
        elif (target_row, target_col-1) == tile:
            moves += "l"
        # case 3: target tile is diagonally to the left of the zero tile
        elif (target_row-1, target_col-1) == tile:
            moves += "lurdl"
        # case 4: target tile is in the same column as the zero tile, several
        # rows above
        elif diff[1] == 0:
            moves += diff[0] * "u"
            moves += (diff[0] - 1) * "lddru"
            moves += "ld"
        # case 5: target tile is in the same row as the zero tile, several
        # columns to the left
        elif diff[0] == 0:
            moves += diff[1] * "l"
            moves += (diff[1] - 1) * "urrdl"
        # case 6: target tile is several rows above and to the left
        elif diff[1] > 0:
            moves += diff[0] * "u"
            moves += diff[1] * "l"
            moves += (diff[1] - 1) * "drrul"
            moves += "dru"
            moves += (diff[0] - 1) * "lddru"
            moves += "ld"
        # case 7: target tile is at row self.get_height() - 2 and to the right
        elif tile[0] == self.get_height() - 2 and diff[1] < 0:
            col_diff = abs(diff[1])
            moves += diff[0] * "u"
            moves += col_diff * "r"
            moves += (col_diff - 1) * "ulldr"
            moves += "ul"
            moves += "lddru"
            moves += "ld"
        # case 8: target tile is several rows above and to the right
        elif diff[1] < 0:
            col_diff = abs(diff[1])
            moves += diff[0] * "u"
            moves += col_diff * "r"
            moves += (col_diff - 1) * "dllur"
            moves += "dlu"
            moves += (diff[0] - 1) * "lddru"
            moves += "ld"

        self.update_puzzle(moves)
        return moves


    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        moves = ""
        target_col = 0
        tile = self.current_position(target_row, target_col)
        diff = (target_row - tile[0], target_col - tile[1])
        
        # case 1: target tile is directly above the zero tile
        if (target_row-1, target_col) == tile:
            moves += "ur"
            moves += "r" * (self.get_width() - 2)
            self.update_puzzle(moves)
            return moves
        # case 2: target tile is in the same column as the zero tile, several
        # rows above
        elif diff[1] == 0:
            moves += diff[0] * "u"
            moves += (diff[0] - 2) * "rddlu"
            moves += "rdl"
        # case 3: target tile is at row self.get_height() - 2 and to the right
        elif tile[0] == self.get_height() - 2 and diff[1] < 0:
            col_diff = abs(diff[1])
            moves += diff[0] * "u"
            moves += col_diff * "r"
            moves += (col_diff - 1) * "ulldr"
            moves += "l"
        # case 4: target tile is several rows above and to the right
        elif diff[1] < 0:
            col_diff = abs(diff[1])
            moves += diff[0] * "u"
            moves += col_diff * "r"
            moves += (col_diff - 1) * "dllur"
            moves += "dlu"
            moves += (diff[0] - 2) * "rddlu"
            moves += "rdl"

        moves += "ruldrdlurdluurddlur"
        moves += "r" * (self.get_width() - 2)

        self.update_puzzle(moves)
        return moves


    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        if self.get_number(0, target_col) != 0:
            return False
        
        # check row 0
        for col in range(target_col + 1, self.get_width()):
            if (0, col) != self.current_position(0, col):
                return False
        
        # check row 1
        for col in range(target_col, self.get_width()):
            if (1, col) != self.current_position(1, col):
                return False
        
        # check all other rows
        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                if (row, col) != self.current_position(row, col):
                    return False

        return True


    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        for col in range(target_col + 1, self.get_width()):
            if (0, col) != self.current_position(0, col):
                return False

        return self.lower_row_invariant(1, target_col)


    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        moves = ""
        target_row = 0
        tile = self.current_position(target_row, target_col)
        diff = (abs(target_row - tile[0]), abs(target_col - tile[1]))
        
        # case 1: target tile is directly to the left of the zero tile
        if (0, target_col-1) == tile:
            moves += "ld"
        # case 2: target tile is diagonally to the left of the zero tile
        elif (1, target_col-1) == tile:
            moves += "lld"
            moves += "urdlurrdluldrruld"
        # case 3: target tile is at row 0 and to the left of the zero tile
        elif tile[0] == 0:
            moves += diff[1] * "l"
            moves += "druld"
            moves += (diff[1] - 2) * "urrdl"
            moves += "urdlurrdluldrruld"
        # case 4: target tile is at row 1 and to the left of the zero tile
        elif tile[0] == 1:
            moves += "ld"
            moves += (diff[1] - 1) * "l"
            moves += (diff[1] - 2) * "urrdl"
            moves += "urdlurrdluldrruld"

        self.update_puzzle(moves)
        return moves


    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        moves = ""
        target_row = 1
        tile = self.current_position(target_row, target_col)
        diff = (target_row - tile[0], abs(target_col - tile[1]))
        
        # case 1: target tile is directly above the zero tile
        if (0, target_col) == tile:
            moves += "u"
        # case 2: target tile is directly to the left of the zero tile
        elif (1, target_col-1) == tile:
            moves += "lur"
        # case 3: target tile is diagonally to the left of the zero tile
        elif (0, target_col-1) == tile:
            moves += "uldru"
        # case 4: target tile is at row 0 and to the left of the zero tile
        elif tile[0] == 0:
            moves += "u"
            moves += diff[1] * "l"
            moves += (diff[1] - 1) * "drrul"
            moves += "dru"
        # case 5: target tile is at row 1 and to the left of the zero tile
        elif tile[0] == 1:
            moves += diff[1] * "l"
            moves += (diff[1] - 1) * "urrdl"
            moves += "ur"
        
        self.update_puzzle(moves)
        return moves

    ###########################################################
    # Phase 3 methods

    def verify_configuration(self, move):
        """
        Checks if the upper left 2x2 tiles are in
        their correct configuration
        """
        board = self.clone()
        board.update_puzzle(move)
        return board.current_position(0, 1) == (0, 1) and \
        board.current_position(1, 1) == (1, 1) and \
        board.current_position(1, 0) == (1, 0)


    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        moves = ""

        if self.verify_configuration("ul"):
            moves += "ul"
            self.update_puzzle(moves)
            return moves
        elif self.verify_configuration("lu"):
            moves += "lu"
            self.update_puzzle(moves)
            return moves

        moves += "ul"

        board = self.clone()
        for item in ["rdlu", "rdlu"]:
            board.update_puzzle(item)
            if board.current_position(0, 1) == (0, 1) and \
            board.current_position(1, 1) == (1, 1) and \
            board.current_position(1, 0) == (1, 0):
                moves += item
                self.update_puzzle(moves)
                return moves
            else:
                moves += item
                board.update_puzzle(moves)

        board = self.clone()
        for item in ["drul", "drul"]:
            board.update_puzzle(item)
            if board.current_position(0, 1) == (0, 1) and \
            board.current_position(1, 1) == (1, 1) and \
            board.current_position(1, 0) == (1, 0):
                moves += item
                self.update_puzzle(moves)
                return moves
            else:
                moves += item
                board.update_puzzle(moves)

        self.update_puzzle(moves)
        return moves


    def position_zero(self, item_row, item_col, target_row, target_col):
        """
        Place zero tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        moves = ""
        tile = self.current_position(item_row, item_col)
        diff = (target_row - tile[0], target_col - tile[1])
        # case 1: zero tile is to the left of the target_col
        if diff[1] > 0:
            moves += diff[1] * "r"
        # case 2: zero tile is to the right of the target_col
        elif diff[1] < 0:
            col_diff = abs(diff[1])
            moves += col_diff * "l"
        
        # move zero tile downwards
        moves += diff[0] * "d"

        self.update_puzzle(moves)
        return moves


    def initialize_zero(self):
        """
        Place zero tile at target position
        """
        for row in range(self.get_height()-1, 0, -1):
            for col in range(self.get_width()-1, -1, -1):
                if (row, col) != self.current_position(row, col):
                    if self.get_number(row, col) == 0:
                        return "", row, col
                    else:
                        moves = self.position_zero(0, 0, row, col)
                        return moves, row, col


    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        moves = ""
        
        # check if puzzle is already solved
        puzzle_solved = True
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                if (row, col) != self.current_position(row, col):
                    puzzle_solved = False
        if puzzle_solved:
            return ""

        # place the zero in its correct initial position
        initial_moves, start_row, start_col = self.initialize_zero()
        moves += initial_moves

        # ensure that the puzzle size is greater than 2; otherwise, skip these tasks
        if self.get_height() > 2:
            # check for a mostly solved puzzle, except for the 4 upper left tiles
            if self.row1_invariant(start_col):
                moves += self.solve_2x2()
                return moves

            # place tiles in their correct locations for all rows, except rows 0 and 1
            for row in range(start_row, 1, -1):
                for col in range(start_col, -1, -1):
                    if col == 0:
                        moves += self.solve_col0_tile(row)
                    else:
                        moves += self.solve_interior_tile(row, col)
                start_col = self.get_width()-1

        # place tiles in their correct locations for rows 0 and 1
        for col in range(self.get_width()-1, 1, -1):
            moves += self.solve_row1_tile(col)
            moves += self.solve_row0_tile(col)
        
        # solve the final upper left 2x2 portion of the puzzle
        moves += self.solve_2x2()
        return moves


# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4, [[9, 3, 1, 13], [5, 10, 2, 7], [8, 12, 6, 11], [4, 0, 14, 15]]))
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]]))

game = Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
print(game)
game.solve_puzzle()
print(game)


"""
|-------------------------------------------------------------------------------
| zombie_apocalypse.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 29, 2021
|
| Run:      python zombie_apocalypse.py
|
| Description:
| This program implements the zombie apocalypse simulator.
|
"""

import random
import poc_grid
import poc_queue
#import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        entity_list = self._zombie_list[:]
        if entity_type == HUMAN:
            entity_list = self._human_list[:]
            
        visited = poc_grid.Grid(self.get_grid_height(), self.get_grid_width())
        distance_field = [[self.get_grid_height() * self.get_grid_width()
                        for dummy_col in range(self.get_grid_width())] 
                        for dummy_row in range(self.get_grid_height())]
        
        boundary = poc_queue.Queue()
        for cell in entity_list:
            boundary.enqueue(cell)
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0

        while len(boundary) > 0:
            cell = boundary.dequeue()
            neighbors = self.four_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1
        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for idx in range(len(self._human_list)):
            row, col = self._human_list[idx]
            neighbors = self.eight_neighbors(row, col)
            largest = zombie_distance_field[row][col]
            position = (row, col)
            for cell in neighbors:
                if zombie_distance_field[cell[0]][cell[1]] > largest and self.is_empty(cell[0], cell[1]):
                    largest = zombie_distance_field[cell[0]][cell[1]]
                    position = (cell[0], cell[1])
            self._human_list[idx] = position
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for idx in range(len(self._zombie_list)):
            row, col = self._zombie_list[idx]
            neighbors = self.four_neighbors(row, col)
            smallest = human_distance_field[row][col]
            position = (row, col)
            for cell in neighbors:
                if human_distance_field[cell[0]][cell[1]] < smallest and self.is_empty(cell[0], cell[1]):
                    smallest = human_distance_field[cell[0]][cell[1]]
                    position = (cell[0], cell[1])
            self._zombie_list[idx] = position


# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))


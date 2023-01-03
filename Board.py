from Boat import Boat, fleet_list
import pandas as pd
from tabulate import tabulate
import copy

class Board: 
    '''
    Information about a square board that manages the game.
    A square of the board can be either: 
        '_': an empty spot or
        '[Boat's name first letter]': the spot of a boat or
        'X': a spot containing a boat that has been attacked or
        'O': a spot not containing a boat that has been attacked.
        
    Attributes:
    size: the number of squares on one side of the board; can be either 5, 8, or 10 
    depends on the level of difficulty 
        an integer
    num_hit: the number of squares containing a boat that has been attacked
        an intege
    grid: list of lists - the list representation of the board 
        a list 
    '''
    
    def __init__(self, size=0): 
        '''
        Initializes the Board object
        
        Board, (int) -> None
        '''
        self.__size = size
        self.num_hit = 0
        self.grid = [['_'] * self.__size for i in range(self.__size)]
        
        
    def set_size(self): 
        '''
        Sets the size for the boat based on the player's choice
        
        Board -> None
        '''
        user_choice = None
        while True:
            print('''
Select a level that you would like to play!

1. Easy
2. Medium 
3. Hard
                            
Enter a number (1, 2, or 3): 
                            ''')
            user_choice = int(input('>>> '))
            if user_choice not in [1,2,3]:
                print('Your choice is invalid. Please try again!')
                print()
            else: 
                break
            
        if user_choice == 1: 
            self.__size = 5
            self.grid = [['_'] * 5 for i in range(5)]
        elif user_choice == 2: 
            self.__size = 8
            self.grid = [['_'] * 8 for i in range(8)]
        else: 
            self.__size = 10
            self.grid = [['_'] * 10 for i in range(10)]

        
    def get_size(self): 
        '''
        Returns the size of the board
        
        Board -> int
        '''
        return self.__size
    
    
    def __str__(self): 
        '''
        Converts the grid to a table for visualization
        Returns the table
        
        Board -> DataFrame
        '''
        grid_df = pd.DataFrame(self.grid)
        return tabulate(grid_df, tablefmt='fancy_grid', headers=list(range(self.__size)))
        
    
    def get_public_view(self):
        '''
        Converts the grid to a table for visualization with boat locations hidden
        Returns the table
        
        Board -> Data Frame
        '''
        sub_grid = copy.deepcopy(self.grid)
        for i in range(self.__size):
            for j in range(self.__size):
                if self.grid[i][j] in [boat.label[0] for boat in fleet_list]:
                    sub_grid[i][j] = '_'
        grid_df = pd.DataFrame(sub_grid)
        return tabulate(grid_df, tablefmt='grid', headers=list(range(self.__size)))
        
        
    def add_boat(self, boat): 
        '''
        Adds a boat to the board. Returns False if the boat can't be placed at the 
        inputted location; returns True otherwise
        
        Board, Boat -> bool
        '''
        if boat.direction == 'h': 
            width = boat.length
            length = boat.width
        else: 
            width = boat.width
            length = boat.length
            
        ## Check if the boat's position is valid size-wise
        if (boat.x < 0) or (boat.y < 0) \
        or (boat.x + width > self.__size) \
        or (boat.y + length > self.__size): 
            return False 
        
        ## Check if the location has been occupied
        for y in range(length): 
            for x in range(width): 
                if self.grid[boat.y + y][boat.x + x] != '_': 
                    return False
                
        ## Update the new position 
        for y in range(length): 
            for x in range(width): 
                self.grid[boat.y + y][boat.x + x] = boat.label[0]
        return True    
        
        
    def attack(self, x, y): 
        '''
        Attacks at a point with given coordinates
        Returns 1 if attacks successfully; 0 if it hits an empty spot; 2 if the spot has
        been attacked before; 3 if the attack position is invalid
        
        Board, int, int -> int
        '''
        while True: 
            try: 
                current_square = self.grid[y][x]
                if current_square in [boat.label[0] for boat in fleet_list]:
                    self.grid[y][x] = 'X'
                    self.num_hit += 1
                    return 1
                elif current_square == '_':
                    self.grid[y][x] = 'O'
                    return 0
                else: 
                    return 2
            except: 
                return 3
            
    
    def get_stats(self): 
        '''
        Returns the number of hit and miss on a board
        
        Board -> tup-of-int
        '''
        total_hit = sum(row.count('X') for row in self.grid)
        total_miss = sum(row.count('O') for row in self.grid)
        return total_hit, total_miss
        
        
    def is_defeated(self): 
        '''
        Returns True if all ships has been attacked, False otherwise
        
        Board -> bool
        '''
        if (self.num_hit == 33 and self.__size == 10) or (self.num_hit == 23 and self.__size == 8) or (self.num_hit == 11 and self.__size == 5): 
            return True 
        else: 
            return False
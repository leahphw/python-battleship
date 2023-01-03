from Board import Board
from Boat import Boat, fleet_list
from random import randint


class Bot: 
    '''
    Informations about a bot player
    
    Attributes: 
    board
        Board object 
    fleet
        list of Boat objects
    opponent
        Player() object
    '''
    
    def __init__(self, opponent): 
        '''
        Initializes the player 
        
        Bot, Player -> None
        '''
        self.opponent = opponent
        size = opponent.board.get_size()
        self.board = Board(size)
        self.fleet = []


    def __repr__(self):
        '''
        Returns string representation of the object

        Bot -> str
        '''
        return 'Bot("' + self.opponent.name + '")'
    
        
    def set_fleet(self): 
        ''' 
        Sets the fleet of the bot based on the player's choice.
        
        Bot -> None
        '''
        size = self.opponent.board.get_size()
        if size == 5:
            self.fleet = [boat for boat in fleet_list if boat.length <= 3]
        elif size == 8: 
            self.fleet = [boat for boat in fleet_list if boat.length <= 4]
        else: 
            self.fleet = fleet_list
        
        
    def place_fleet(self):
        '''
        Places the whole fleet on the board 
        
        Bot -> None
        '''
        
        for boat in self.fleet: 
            self.place_boat(boat)
        
    
    def place_boat(self, boat): 
        '''
        Places a single boat 
        
        Bot, Boat -> None
        '''
        
        ## Get orientation
        while True:
            direction = randint(1,2)
            if direction == 1: 
                direction = 'v'
            else: 
                direction = 'h'
            ## Ask for position 
            x = randint(0, self.board.get_size()-1)
            y = randint(0, self.board.get_size()-1)

            boat.set_direction(direction)
            boat.set_position(x, y)
                
            ## Adding the boat to the board 
            if self.board.add_boat(boat) == True: 
                self.board.add_boat(boat)
                break
                    
                
    def take_turn(self): 
        '''
        Processes a single turn for the bot
        Returns True if the opponent has been defeated, False otherwise
        
        Bot -> bool
        '''  
        
        while True:  
            ## Get attack position 
            x = randint(0, self.board.get_size()-1)
            y = randint(0, self.board.get_size()-1)
                    
            ## Perform attack 
            hit_point = self.opponent.board.attack(x,y)
            if hit_point == 1 or hit_point == 0: 
                break
        
        ## Return True if the opponent is defeated, False otherwise 
        if self.opponent.board.is_defeated() == True: 
            return True 
        else: 
            return False
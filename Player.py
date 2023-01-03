from Board import Board
from Boat import Boat, fleet_list
   
class Player: 
    '''
    Information about a player 
    
    Attributes: 
    name
        a string 
    board: the board representing the player's plan
        Board object 
    fleet: a list of the player's boats to be placed
        list of Boat objects
    '''
    
    def __init__(self, name=None): 
        '''
        Initializes the player 
        
        Player, (str) -> None
        '''
        self.name = name 
        self.board = Board()
        self.fleet = []


    def __repr__(self):
        '''
        Returns the string representation of the object

        Player -> str
        '''
        return 'Player("' + self.name + '")'
    
        
    def set_fleet(self): 
        ''' 
        Sets the fleet of the player based on the player's choice
        of difficulty
        
        Player -> None
        '''
        size = self.board.get_size()
        if size == 5:
            self.fleet = [boat for boat in fleet_list if boat.length <= 3]
        elif size == 8: 
            self.fleet = [boat for boat in fleet_list if boat.length <= 4]
        else: 
            self.fleet = fleet_list


    def set_opponent(self, opponent): 
        '''
        Sets the bot as the opponent for the player 
        
        Player, Bot -> None
        '''
        self.opponent = opponent
    
    
    def place_fleet(self):
        '''
        Places all of the boats on the board 
        
        Player -> None
        '''
        input(self.name + ', Press Enter to start placing your fleet!')
        print()
        for boat in self.fleet: 
            self.place_boat(boat)
        
    
    def place_boat(self, boat): 
        '''
        Positions a single boat 
        
        Player, Boat -> None
        '''
        print(self.board)
        print()
        print(f'You need to place a {boat.label} of length {boat.length} and width {boat.width} on the board.')
        
        ## Ask for orientation
        direction = ''
        while True: 
            print()
            print('Would you like to place the boat horizontally or vertically (h/v)?')
            direction = input('>>> ')
            if direction not in ['v', 'h']: 
                print('Enter "v" or "h" only. Try again!')
            else: 
                break
            
        ## Ask for position 
        position = ''
        while True: 
            try:
                print('''
Select the position for this boat
                                 
Enter using the form (x,y), with x is the top coordinate and y is the left-side coordinate: 
                                 ''')
                position = input('>>> ')
                
                if position[0] != '(' and position[-1] != ')': 
                    raise Exception
                
                position = position[1:-1].split(',')
                x = int(position[0])
                y = int(position[-1]) 
                
                boat.set_direction(direction)
                boat.set_position(x, y)
                
                ## Adding the boat to the board 
                if self.board.add_boat(boat) == True: 
                    self.board.add_boat(boat)
                
                break

            except: 
                print()
                print('''
Invalid form! You need a set of parentheses and the coordinates must\
not violate the size of the board or the placing of other boats.
                      ''')
                
                
    def take_turn(self): 
        '''
        Processes a single turn for the player
        Returns True if the opponent has been defeated, False otherwise
        
        Player -> bool
        '''   
        ## Display the boards: 
        print('Your board:')
        print()    
        print(self.board)
        print() 
        print(f'Your opponent\'s board:')
        print()
        print(self.opponent.board.get_public_view())   
        
        ## Get attack position 
        position = ''
        while True: 
            try: 
                print('''
Enter the position you would like to attack.

Enter using (x,y) form. x for the horizontal location and y for vertical location: 
                                 ''')
                position = input('>>> ')
                
                if position[0] != '(' and position[-1] != ')': 
                    raise Exception
                
                position = position[1:-1].rstrip().split(',')
                
                x = int(position[0])
                y = int(position[1]) 
                
                hit_point = self.opponent.board.attack(x,y) 
                if hit_point == 1: 
                    print('''
█▄█ █▀█ █░█   █░█ █ ▀█▀   ▄▀█   █▄▄ █▀█ ▄▀█ ▀█▀ █
░█░ █▄█ █▄█   █▀█ █ ░█░   █▀█   █▄█ █▄█ █▀█ ░█░ ▄
''')
                    break
                elif hit_point == 0:
                    print('''
█▄█ █▀█ █░█   █▀▄▀█ █ █▀ █▀ █▀▀ █▀▄ ░
░█░ █▄█ █▄█   █░▀░█ █ ▄█ ▄█ ██▄ █▄▀ ▄
                  ''')
                    break
                else:
                    raise Exception
            except:
                print()
                print('The position you entered is invalid. Try again! Make sure to include parentheses and not violating the board size')

        
        ## Return True if the opponent is defeated, False otherwise 
        if self.opponent.board.is_defeated() == True: 
            return True 
        else: 
            return False  

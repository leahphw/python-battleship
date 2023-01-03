class Boat: 
    '''
    Information about one boat.
    
    Attributes: 
    label: name of the boat 
        a string 
    length
        an integer
    width
        an integer
    x: the x-coordinate on the board of the boat 
        an integer 
    y: the y-coordinate on the board of the boat 
        an integer 
    direction: the direction of the boat, either 'h' for horizontal or 'v' for vertical
        a string
    '''
    
    def __init__(self, label, length, width, x=0, y=0, direction=''): 
        '''
        Initializing the Boat object. 
        
        Boat, str, int, int, (int), (int), (str) -> None 
        '''
        self.label = label
        self.width = width 
        self.length = length
        self.x = x
        self.y = y
        self.direction = direction
        
        
    def __repr__(self): 
        '''
        Returns the string representation of the Boat object 
        
        Boat -> None
        '''
        return (f'Boat(\'{self.label}\', {self.length} {self.width}, {self.x}, {self.y}, \'{self.direction}\')')
        
        
    def set_position(self, x, y):
        '''
        Sets the boat's position. x is the x-coordinate and y is the y-coordinate.
        
        Boat, int, int -> None
        '''
        self.x = x
        self.y = y 
        
        
    def set_direction(self, direction):
        '''
        Sets the boat's direction. The direction must be either 'h' for horizontal or 
        'v' for vertical.
        
        Boat, str -> None
        '''
        self.direction = direction
        
        
## Creates a list of all boats from the txt file
fleet_info = {}
with open('fleet.txt') as fleet_file: 
    try:
        for line in fleet_file: 
            boat = line.split(',')
            boat[1] = boat[1].split('x')
            boat[1][0] = int(boat[1][0])
            boat[1][1] = int(boat[1][1].strip())
            fleet_info[boat[0]] = boat[1]
    
    except OSError: 
        print('There was some error importing fleet data. Can you check if "fleet.txt" is in the same folder?')

fleet_list = []        
for boat in fleet_info: 
    boat_object = Boat(boat, fleet_info[boat][0], fleet_info[boat][1])
    fleet_list.append(boat_object)
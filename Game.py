from Player import Player
from Bot import Bot
from Board import Board 
from Boat import Boat

class Game: 
    '''
    Information about a game with a human and a bot
    
    Attributes: 
    players: a list of players
        a list 
    '''
    
    def __init__(self): 
        ''' 
        Initializes the game 
        
        Game -> None
        '''
        
        self.players = None


    def __repr__(self):
        '''
        Returns the string representation of the object

        Game -> str
        '''

        return 'Game()'
        
        
    def set_players(self, player1, player2): 
        '''
        Sets up the list of players
        
        Game, Player, Bot -> None
        '''
        self.players = [player1, player2]
        self.players[0].set_opponent(self.players[1])
        
        
    def display_rule(self): 
        '''
        Displays the rule of the game for the players
        
        Game -> None
        '''
        
        print('''
The rules of the game are relatively simple! 

You will have the chance to explore different oceans and join in the battles of the ships. You will be playing with our bot.

Basically, you will be given a 5x5, 8x8, or 10x10 board based on your selection of level difficulty and received a set of fleet to play with. You and your opponent will place your boats accordingly on the board so that you fleet stays within the grid and not overlaps each other. After that, you and your opponent will take turn finding attacks points and hit on other’s matrix. Who can hit every of the other’s fleet first will be the winner! 

Have fun playing this game! 

              ''')
        
        
    def play(self): 
        ''' 
        Runs the game by switching turns
        
        Game -> None
        '''
        
        self.players[0].set_fleet()
        self.players[1].set_fleet()
        
        self.players[0].place_fleet()
        self.players[1].place_fleet() 
        
        won = False
        is_player1_turn = True
        while not won: 
            if is_player1_turn == True: 
                won = self.players[0].take_turn()
                if won == True: 
                    print('''

░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░░░░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗░░░
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝░░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝

██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝╚═╝
                          ''')
            else: 
                won = self.players[1].take_turn()
                if won == True: 
                    print('''
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█ ░   █▄█ █▀█ █░█   █░░ █▀█ █▀ ▀█▀ ░
█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄ ▄   ░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ░█░ ▄
                          ''')
            is_player1_turn = not is_player1_turn
            
            
    def send_report(self): 
        '''
        Sending the player the statistics of the game they just played 
        
        Game -> None
        '''
        
        with open('game_stats.txt', 'w') as game_stats: 
            try:
                game_stats.write('Here is your game stats:\n')
                
                self_stats = self.players[1].board.get_stats()
                self_hit = self_stats[0]
                self_miss = self_stats[1]
                
                opponent_stats = self.players[0].board.get_stats()
                opponent_hit = opponent_stats[0]
                
                if self_hit > opponent_hit: 
                    game_stats.write('You won!\n')
                else: 
                    game_stats.write('You lost.\n')
                
               
                
                game_stats.write('You used a total of ' + str(self_hit + self_miss) + ' attacks to destroy ' + str(self_hit) + ' places of your opponent\'s fleet.\n')
                game_stats.write('That\'s a total of ' + str(self_miss) + ' miss attacks. Great eyes!')
        
            except: 
                print('There was some problem working with your game stats report. Sorry for this inconvenience.')
                    
                
                
        
        
        

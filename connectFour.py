# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
ConnectFour.py

Author: Christopher Ayling

A class to represent a game of connect four.

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import renderCF

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ConnectFour():
    '''
    Class to represent a connect four game board, including the position of
    each player's counters and the size of the board.
    '''
    def __init__(self, height = 6, width = 8, player1 = 'red', player2 = 'green', num_to_win = 4, square_size = 100):
        self.height = height
        self.width = width
        self.board = [[] for i in range(width)]
        self.num_to_win = num_to_win

        self.player1 = player1
        self.player2 = player2
        self.players = (player1, player2)
        
        self.square_size = square_size
        
        renderCF.setup_board(self.width, self.height, self.square_size)
        
        self.game_over = False
        self.winning_player = None
        


    def insert_counter(self, player, column):
        '''
        Insert a counter into the specified column.
        '''
        self.board[column].append(player)
        

        
    def actions(self):
         '''
        Return the list of actions that can be executed in the given state if
        these actions do not result in the overflowing of a column.
        '''
         actions = range(0, self.width)
         valid_actions = []
        
         for action in actions:
            if (len(self.board[action]) < self.height):
                valid_actions.append(action)
       
         return valid_actions



    def check_for_win(self):
         '''
        Check if a player has won.
        '''
         directions = [(0, 1), (1, 0), (1, 1)]
         #convert self.board into a matrix

         for direction in directions:
            for player in [self.player1, self.player2]:
                pass
                
                

    def render(self):
        '''
        renders the game board using turtle graphics.
        '''
        renderCF.draw_board(self.board, self.square_size, self.height)

        
        
    def __str__(self):
        '''
       String representation of the class.
       '''
        state = []
        for col in self.board:
            state.append(str(col))            
        return "\n".join(state)
# -*- coding: utf-8 -*-
"""
CONNECT FOUR

Created on Fri Jun  9 08:56:46 2017

@author: USER
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class ConnectFour():
    '''
    Class to represent a connect four game board, including the position of
    each player's counters and the size of the board.
    
    self.counters is a list of (x, y, c)
    self.height and self.width are integers
    '''
    def __init__(self, height = 6, width = 8, player1 = 'X', player2 = 'O', num_to_win = 4):
        self.height = height
        self.width = width
        self.board = [[] for i in range(width)]
        self.num_to_win = num_to_win

        self.player1 = player1
        self.player2 = player2


    def insert_counter(self, player, column):
        '''
        Insert a counter into the specified colum
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
        Check if a player has won
        '''
        directions = [(0, 1), (1, 0), (1, 1)]
        #convert self.board into a matrix
        
        for direction in directions:
            for player in [self.player1, self.player2]:
                pass

    def render(self):
        x = 1
        return
        
        
    def __str__(self):
        state = []
        for col in self.board:
            state.append(str(col))
            
        return "\n".join(state)

            
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    CF = ConnectFour(height = 3)
    
    print("inserting counters")
    CF.insert_counter(CF.player1, 4)
    CF.insert_counter(CF.player1, 4)
    CF.insert_counter(CF.player2, 4)
    CF.insert_counter(CF.player2, 2)
    print(CF)

    CF.render()
    
    print('valid_actions = ', CF.actions())
    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
2playerConnectFour.py

Author: Christopher Ayling

Script for a two player game of connect four

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import connectFour

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    #create board
    CF = connectFour.ConnectFour()
    
    #enter game loop
    while (not CF.game_over):
        for player in CF.players:
            #print valid actions
            valid_actions = CF.actions()
            print('valid actions = ', valid_actions)
            #loop for valid input
            while (True):
                chosen_action = int(input(player + "'s turn: "))
                if chosen_action in valid_actions:
                    break
                else:
                    print("please input a valid action")

            CF.insert_counter(player, chosen_action)
            CF.render()
        
        
    #display the winning player
    print("The winner is... ", CF.winning_player)
    
    #exit cleanly
    #... I wish I knew how ...
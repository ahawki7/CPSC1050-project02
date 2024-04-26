"""
Author:         Alaina Hawkinson
Date:           04/25/2024
Assignment:     Project 02
Course:         CPSC1051
Lab Section:    001

CODE DESCRIPTION: This code is for keeping track of if the game is over.    
"""


class game_status: #keeps track of if the game is still going on 

    def __init__(self): # initializes that the game is still going on
        self.game_over = False

    def status(self, bool): # sets if the status changes 
        if bool:
            self.game_over = True # if it changes then they win
            print("Congratulations! You've escaped from the museum.")
            quit()

    def is_game_over(self): # checks if the game is still going
        return self.game_over
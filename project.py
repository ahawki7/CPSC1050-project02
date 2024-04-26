"""
Author:         Alaina Hawkinson
Date:           04/25/2024
Assignment:     Project 02
Course:         CPSC1051
Lab Section:    001

CODE DESCRIPTION: In this code, the user will be navigating a role playing game where they will be in a musuem and going room to room collecting artifacts. The goal of this is to collect the right items to give to the mummy so that they can escape the museum. 

GITHUB LINK: https://github.com/ahawki7/CPSC1050-project02.git
"""

import sys #ability to access other modules
import os #imports operating systems
from map import museum_map #imports the museum_map class from the map module
from map import Room # imports the Room class from the map module 
from room_quests import combat #imports the combat class from the room quest module
from status_update import game_status #imports the game_status class from the status_update module


class Bag: #This is the toolbox of the player, it will store the items they collect
    def __init__(self): #initializes the contents list 
        self.contents=[]
    
    def add_to_bag(self,addition): #adds item to the contents of the bag
        self.contents.append(addition)
    
    def get_contents(self): #returns a list of contents 
        return self.contents 

    def list_contents(self): #returns a string of contents 
        contents=self.contents
        return "\n".join(contents)
    
    def check(self,content):
        if content in self.contents: #checks to see if a certain item has already been picked up
            return True

    def remove(self,content): #takes an item out of the bag
        self.contents.pop(content) 




def main():
    #introduction dialog
    print("Welcome to a night in the museum! We are so glad you are here, so much so that you can never leave!")
    print("\nBOOM!\n") 
    print("Did you hear that? that was the sound of the door slamming shut behind you and locking.\n")
    map=museum_map()#initializes museum map
    bag=Bag() #initializes the players bag
    
    #adds the exhibits of the museum to the map
    map.add_exhibit(Room("US HISTORY","Welcome to the US History exhibit! Along the left wall is every presidents picture and to the right is a life sized statue of the statue of liberty!",["ANIMAL EXHIBIT","DINOSAUR EXHIBIT"]))
    map.add_exhibit(Room("ANIMAL EXHIBIT", "Welcome to the room of animals! If you look around you can see some extinct animals from the past, some taxidermy animals from the present, and we started the animals of the future exhibit but we are not sure there will be any left.",["US HISTORY","ART","GEOLOGY"]))
    map.add_exhibit(Room("DINOSAUR EXHIBIT","Welcome to the Dino Room! This is a wonderful place where astroids don't exhist! we have bones and fossils from a super long time ago and its really cool",["US HISTORY","WAR EXHIBIT"]))
    map.add_exhibit(Room("ART","Welcome where to the art exhibit! Here we have paintings from all kinds of wonderful artists! Its super cool but unfortunately a dead end sorry!",["ANIMAL EXHIBIT"]))
    map.add_exhibit(Room("GEOLOGY","Welcome to the the geology exhibit, this place rocks!",["ANIMAL EXHIBIT","ANCIENT HISTORY","WAR EXHIBIT"]))
    map.add_exhibit(Room("ANCIENT HISTORY","Welcome to Ancient History exhibit! Watch out for the mummy, he gets cranky when hes woken up without a gift",["WAR EXHIBIT"]))
    map.add_exhibit(Room("WAR EXHIBIT","Welcome to the war exhibit, here we have displays from the world wars",["DINOSAUR EXHIBIT","ANCIENT HISTORY","GEOLOGY"]))
    
    #more dialog
    print("The only way out of this place is with the mummy's help. If you collect gifts for the mummy and find him, he may help you")
    print("or kill you \n")
    print("Good Luck!")
    print("you will start out in the US History room")

    current_room=map.get_room("US HISTORY") #starts the player in the US history exhibit
    going=True #initializes the boolean that keeps the loop going for the play
    print(current_room) #prints out the information for the room the player is starting in
    exits=current_room.list_exits() #creates a variable for the exits that the room has 
    riff=combat(bag) #this initializes the combat clas
    riff.ushistory() # prints out the combat in the first room
    game_check=game_status() #initialize the class that checks to see if the game is done

    while going: #while the game has not ended 
        if game_check.is_game_over(): #check to make sure the game has not ended 
            going=False #ends loop
        else: # if the game is still going
            print("\nWhere do you want to go next?") # ask the player where they want to go next 
            exits = current_room.list_exits() #find their options for exits
            print(f"Your options are:\n{exits}\n") #give them their options for exits
            next_stop = input().strip().lower() #player inputs 
            target_room = map.get_room(next_stop) #find the correct room in the map
            if target_room is None: # if there is an error ask them again
                print("Invalid room name. Please choose a valid room.")
            else: #if the room is valid
                current_room = target_room # replace the current room with the new one 
                print(current_room) #print out the spiel about the room

                #find which conflict to run into based off of what room they are in
                if next_stop=="us history": 
                    riff.ushistory()
                elif next_stop=="animal exhibit":
                    riff.animals()
                elif next_stop=="dinosaur exhibit":
                    riff.dinosaurexhibit()
                elif next_stop=="art":
                    riff.art()
                elif next_stop=="geology":
                    riff.geology()
                elif next_stop=="ancient history":
                    riff.ancienthistory()
                elif next_stop=="war exhibit":
                    riff.war()
       





if __name__ == "__main__":
    main()

"""
Author:         Alaina Hawkinson
Date:           04/25/2024
Assignment:     Project 02
Course:         CPSC1051
Lab Section:    001

CODE DESCRIPTION: THis code holds the classes for the map of the museum and the individual room that the player is in.  
"""

class museum_map: #stores info for the map of the museum
    def __init__(self):
        self.map={} #initializes an empty map

    def add_exhibit(self,exhibit): 
        self.map[exhibit.get_name().lower()] = exhibit #adds exhibits to the map

    def get_room(self, room_name): 
        room = self.map.get(room_name.lower()) #retrieves the room in lowercase 
        return room
    
    
class Room: #stores the information for each exhibit 
    def __init__(self,name,description,exits): #initializes attributes of the rooms 
        self.name=name 
        self.description=description
        self.exits=exits
    
    def get_name(self): #returns the name of the exhibit
        return self.name
    
    def get_description(self): #returns the description of the exhibit
        return self.description

    def get_exits(self): # returns the exits for the exhibit
        return self.exits

    def list_exits(self): #returns a string list of the exhibit
        exits=self.exits #gets the exits
        for i in range(len(exits)): # lowercase exits
            exits[i]=exits[i].lower() 
        return "\n".join(exits) #returns a string 

    def __str__(self):
        return (f"{self.get_name()}: {self.get_description()}\n\nExits:\n{self.list_exits()}\n\n") #string of the name, description, and exits in the room 
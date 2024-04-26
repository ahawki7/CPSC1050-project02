
import sys 
import os
from map import museum_map
from map import Room
from room_quests import combat
from status_update import game_status


class Bag:
    def __init__(self):
        self.contents=[]
    
    def add_to_bag(self,addition):
        self.contents.append(addition)
    
    def get_contents(self):
        return self.contents 

    def list_contents(self):
        contents=self.contents
        return "\n".join(contents)
    
    def check(self,content):
        if content in self.contents:
            return True

    def remove(self,content):
        self.contents.pop(content)




def main():
    print("Welcome to a night in the museum! We are so glad you are here, so much so that you can never leave!")
    print("\nBOOM!\n") 
    print("Did you hear that? that was the sound of the door slamming shut behind you and locking.\n")
    map=museum_map()
    bag=Bag()
    map.add_exhibit(Room("US HISTORY","Welcome to the US History exhibit! Along the left wall is every presidents picture and to the right is a life sized statue of the statue of liberty!",["ANIMAL EXHIBIT","DINOSAUR EXHIBIT"]))
    map.add_exhibit(Room("ANIMAL EXHIBIT", "Welcome to the room of animals! If you look around you can see some extinct animals from the past, some taxidermy animals from the present, and we started the animals of the future exhibit but we are not sure there will be any left.",["US HISTORY","ART","GEOLOGY"]))
    map.add_exhibit(Room("DINOSAUR EXHIBIT","Welcome to the Dino Room! This is a wonderful place where astroids don't exhist! we have bones and fossils from a super long time ago and its really cool",["US HISTORY","WAR EXHIBIT"]))
    map.add_exhibit(Room("ART","Welcome where to the art exhibit! Here we have paintings from all kinds of wonderful artists! Its super cool but unfortunately a dead end sorry!",["ANIMAL EXHIBIT"]))
    map.add_exhibit(Room("GEOLOGY","Welcome to the the geology exhibit, this place rocks!",["ANIMAL EXHIBIT","ANCIENT HISTORY","WAR EXHIBIT"]))
    map.add_exhibit(Room("ANCIENT HISTORY","Welcome to Ancient History exhibit! Watch out for the mummy, he gets cranky when hes woken up without a gift",["WAR EXHIBIT"]))
    map.add_exhibit(Room("WAR EXHIBIT","Welcome to the war exhibit, here we have displays from the world wars",["DINOSAUR EXHIBIT","ANCIENT HISTORY","GEOLOGY"]))
    print("The only way out of this place is with the mummy's help. If you collect gifts for the mummy and find him, he may help you")
    print("or kill you \n")
    print("Good Luck!")
    print("you will start out in the US History room")
    current_room=map.get_room("US HISTORY")
    bag=Bag()
    going=True
    print(current_room)
    exits=current_room.list_exits()
    riff=combat(bag)
    riff.ushistory()
    game_check=game_status()
    while going:
        if game_check.is_game_over():
            break
        else:
            print("\nWhere do you want to go next?")
            exits = current_room.list_exits()
            print(f"Your options are:\n{exits}\n")
            next_stop = input().strip().lower()
            target_room = map.get_room(next_stop)
            if target_room is None:
                print("Invalid room name. Please choose a valid room.")
            else:
                current_room = target_room
                print(current_room)
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

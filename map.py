class museum_map:
    def __init__(self):
        self.map={}

    def add_exhibit(self,exhibit): 
        self.map[exhibit.get_name().lower()] = exhibit

    def get_room(self, room_name): 
        room = self.map.get(room_name.lower())
        return room
    
    
class Room:
    def __init__(self,name,description,exits):
        self.name=name
        self.description=description
        self.exits=exits
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits

    def list_exits(self):
        exits=self.exits
        for i in range(len(exits)): # lowercase exits
            exits[i]=exits[i].lower()
        return "\n".join(exits) #returns a string 

    def __str__(self):
        return (f"{self.get_name()}: {self.get_description()}\n\nExits:\n{self.list_exits()}\n\n")
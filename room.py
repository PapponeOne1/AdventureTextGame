class Room:
    def __init__(self, room_name):
        self_name = room_name
        self.description = None
#why isn t self.descrtitption in brackets?

    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

#getter and setter

    def set_name(self,room_name):
        self.name = room_name

    def get_name(self,room_name):
        self.name = room_name

# metod to link rooms together
    def link_room(self, room_to_link, direction):
        self.linked_room[direction] = room_to_link

#displaying linked rooms
    def get_details(self):
        print(self.name)   
        print("--------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)





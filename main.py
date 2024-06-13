from room import Room

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("ballroom")
ballroom.set_description("A vast hall , grand and pompous")

dining_hall = Room("dining_hall")
dining_hall.set_description("a small place, a tiny plastic table. Above it, a towering poster of Mr.Bean")

kitchen.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

dining_hall.get_details()


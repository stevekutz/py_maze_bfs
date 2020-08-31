from world import World
from ast import literal_eval
import random

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

print(world.print_maze())


"""
grid = ['************************',
        '*************** e ******', 
        '***************007******', 
        '*********0060050s0001***', 
        '***************003******', 
        '***************004******', 
        '************************'
        ]

"""
import random
import math
from room import Room

class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.room_grid = []
        self.grid_size = 0
    def load_graph(self, room_graph):
        num_rooms = len(room_graph)
        rooms = [None] * num_rooms
        grid_size = 1
        for i in range(0, num_rooms):
            x = room_graph[i][0][0]
            grid_size = max(grid_size, room_graph[i][0][0], room_graph[i][0][1])
            self.rooms[i] = Room(f"Room {i}", f"({room_graph[i][0][0]},{room_graph[i][0][1]})",i, room_graph[i][0][0], room_graph[i][0][1])
        self.room_grid = []
        grid_size += 1
        self.grid_size = grid_size
        for i in range(0, grid_size):
            self.room_grid.append([None] * grid_size)
        for room_id in room_graph:
            room = self.rooms[room_id]
            self.room_grid[room.x][room.y] = room
            if 'n' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('n', self.rooms[room_graph[room_id][1]['n']])
            if 's' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('s', self.rooms[room_graph[room_id][1]['s']])
            if 'e' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('e', self.rooms[room_graph[room_id][1]['e']])
            if 'w' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('w', self.rooms[room_graph[room_id][1]['w']])
        self.starting_room = self.rooms[0]

    def print_rooms(self):
        rotated_room_grid = []


        for i in range(0, len(self.room_grid)):
            rotated_room_grid.append([None] * len(self.room_grid))
        for i in range(len(self.room_grid)):
            for j in range(len(self.room_grid[0])):
                rotated_room_grid[len(self.room_grid[0]) - j - 1][i] = self.room_grid[i][j]
        print(f'#####   {len(self.room_grid)}')
        str = ""
        for row in rotated_room_grid:
            all_null = True
            for room in row:
                if room is not None:
                    all_null = False
                    break
            if all_null:
                continue
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        print(str)
        print("#####")


    def print_maze(self):
        maze = []
        for row in range(len(self.room_grid) -1 ):
            str = ''
            for col in range(len(self.room_grid) - 1):
                # print(f' row[{row}]col[{col}] = {self.room_grid[row][col]}')
                
                if self.room_grid[row][col] == None:
                    str += '***'

                else:
                    # str += f"{self.room.id}".zfill(3)
                    room = self.room_grid[row][col].name.split()
                    room = room[-1].zfill(3)
                    # room = room.str(room[-1].zfill(3))
                    print(f' room {room}')
                    str += room
            maze.append(str)
        return maze


        # rotated_room_grid = []
        # for i in range(0, len(self.room_grid)):
        #     rotated_room_grid.append([None] * len(self.room_grid))
        # for i in range(len(self.room_grid)):
        #     for j in range(len(self.room_grid[0])):
        #         rotated_room_grid[len(self.room_grid[0]) - j - 1][i] = self.room_grid[i][j]
        
        # for row in range(0, 1):
        #     for col in range(0, len(self.room_grid)):
        #             for i in range(0, len(self.room_grid)):
        #                 top_edge = '+'.join('+')
        #             maze.append(top_edge)

        print(f' grid:  {self.room_grid}')

        print(f' \n\n')


        print(f' grid:  {self.room_grid}')

        # for row in range(0, ( (len(self.room_grid) + 1 ))):
        #     for col in range(len(self.room_grid + 1)):
        #         maze.append(('"' + '+' * 3(len(self.room_grid) + 1) + '"'))            
        # print(maze)


        # for item in self.room_grid:
        #     maze.append(item)


        # print(f'\n\n MAZE \n\n')
        
        # print(maze)    




        # str = ""
        # for row in rotated_room_grid:
        #     all_null = True
        #     for room in row:
        #         if room is not None:
        #             all_null = False
        #             break
        #     if all_null:
        #         continue
        #     # PRINT NORTH CONNECTION ROW
        #     str += "#"
        #     for room in row:
        #         if room is not None and room.n_to is not None:
        #             str += "  |  "
        #         else:
        #             str += "     "
        #     str += "#\n"
        #     # PRINT ROOM ROW
        #     str += "#"
        #     for room in row:
        #         if room is not None and room.w_to is not None:
        #             str += "-"
        #         else:
        #             str += " "
        #         if room is not None:
        #             str += f"{room.id}".zfill(3)
        #         else:
        #             str += "   "
        #         if room is not None and room.e_to is not None:
        #             str += "-"
        #         else:
        #             str += " "
        #     str += "#\n"
        #     # PRINT SOUTH CONNECTION ROW
        #     str += "#"
        #     for room in row:
        #         if room is not None and room.s_to is not None:
        #             str += "  |  "
        #         else:
        #             str += "     "
        #     str += "#\n"
        # print(str)
        # print("#####")        
def print_rooms(self):
    rotated_room_grid = []
    for i in range(0, len(self.room_grid)):
        rotated_room_grid.append([None] * len(self.room_grid))
    for i in range(len(self.room_grid)):
        for j in range(len(self.room_grid[0])):
            rotated_room_grid[len(self.room_grid[0]) - j - 1][i] = self.room_grid[i][j]
    print("#####")
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
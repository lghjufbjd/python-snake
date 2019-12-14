import random

from bcolors import bcolors

score = 0
snake_color = bcolors.OKGREEN
tile_color = bcolors.OKBLUE
apple_color = bcolors.WARNING
end_color = bcolors.ENDC

last_move_col=0
last_move_row=0

score=3



room_statement = {
    "tile": "▓▓",
    "snake": bcolors.OKGREEN + "██" + bcolors.ENDC,
    "apple": bcolors.WARNING + " ■" + bcolors.ENDC,
    "stairs": bcolors.OKBLUE + "└┐" + bcolors.ENDC,

}
room_grid = [
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]],
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]],
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]],
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]],
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]],
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]],
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]],
    [room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"],
     room_statement["tile"], room_statement["tile"], room_statement["tile"], room_statement["tile"]]
]


def map_draw():
    for room_grid_row in room_grid:
        for elem in room_grid_row:
            print(elem, end=" ")
        print()


def map_spawn():
    global last_move_col
    global last_move_row
    last_move_col= 6
    last_move_row = 5
    room_grid[last_move_row][last_move_col] = room_statement["snake"]
    print("")

def map_move(direction):
    global last_move_col
    global last_move_row
    if direction == "up":
        room_grid[last_move_row - 1][last_move_col ] = room_statement["snake"]
        room_grid[last_move_row][last_move_col] = room_statement["tile"]
        last_move_col -= 1
    elif direction == "right":
        room_grid[last_move_row ][last_move_col+ 1] = room_statement["snake"]
        room_grid[last_move_row][last_move_col] = room_statement["tile"]
        last_move_row += 1
    elif direction == "down":
        room_grid[last_move_row+ 1][last_move_col ] = room_statement["snake"]
        room_grid[last_move_row][last_move_col] = room_statement["tile"]
        last_move_col += 1
    elif direction == "left":
        room_grid[last_move_row][last_move_col-1] = room_statement["snake"]
        room_grid[last_move_row][last_move_col] = room_statement["tile"]
        last_move_row -= 1
    else:
        print("Error: bad direction")




def map_apple():
    print("")


def cls():
    print("\033[H\033[2J");

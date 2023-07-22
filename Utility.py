# Constants
DEFAULT_TILE_VALUE = 2
DEFAULT_DIMS = (4, 4)
BOARD_SIZE = 4
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

# Direction enums
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
LEGAL_DIR_FLAGS = [LEFT, RIGHT, UP, DOWN]

dir_map = {
    "L" : LEFT,
    "R" : RIGHT,
    "U" : UP,
    "D" : DOWN
}

class Direction:
    row_offset = 0
    col_offset = 0
    def __init__(self, dir_flag):
        if dir_flag not in LEGAL_DIR_FLAGS:
            print("Error, invalid direction")
            exit()
        elif dir_flag == LEFT:
            self.row_offset = 0
            self.col_offset = -1
        elif dir_flag == RIGHT:
            self.row_offset = 0
            self.col_offset = 1
        elif dir_flag == UP:
            self.row_offset = -1
            self.col_offset = 0
        elif dir_flag == DOWN:
            self.row_offset = 1
            self.col_offset = 0

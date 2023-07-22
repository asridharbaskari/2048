from Utility import Direction
import Utility
from Board import Tile, Board
from random import randint

class Game:
    board = None
    dims = (4, 4)
    def __init__(self):
        pass

    # Creates a Tile object with value val and places it at position (i, j)
    def place_tile(self, pos, val):
        row, col = pos
        cell = (self.board).cells[row][col]
        cell.contains_tile = True
        cell.tile = Tile(val)
        self.board.num_tiles += 1
    
    # Places a Tile on a random empty cell
    def place_random_tile(self, val):
        rand_row, rand_col = -1, -1
        rows = self.board.rows
        cols = self.board.cols
        while self.board.contains_tile(rand_row, rand_col) or (rand_row < 0 and rand_col < 0):
            rand_row = randint(0, rows - 1)
            rand_col = randint(0, cols - 1)
        self.place_tile((rand_row, rand_col), val)
        


    def delete_tile(self, pos):
        row, col = pos
        cell = (self.board.cells)[row][col]
        cell.tile = None
        cell.contains_tile = False

    
    def move_tile(self, source, dest):
        value = self.board.get(source).tile.value

        # Move the tile
        self.place_tile(dest, value)
        self.delete_tile(source)

    def merge_tiles(self, source, dest):
        source_value = self.board.get(source).tile.value
        dest_value = self.board.get(dest).tile.value

        self.delete_tile(source)
        self.delete_tile(dest)
        
        self.place_tile(dest, source_value + dest_value)

    def shift(self, dir_flag):
        if dir_flag not in Utility.LEGAL_DIR_FLAGS:
            print("Illegal move.")
            return
        direction = Direction(dir_flag)
        row_offset = direction.row_offset
        col_offset = direction.col_offset
        move_on = True
        while move_on:
            move_on = False
            for row in range(Utility.BOARD_SIZE):
                for col in range(Utility.BOARD_SIZE):
                    source = (row, col)
                    dest = (row+row_offset, col+col_offset)
                    cell = (self.board.cells)[row][col]
                    stuck = self.board.out_of_bounds(row+row_offset, col+col_offset)
                    if stuck or not cell.contains_tile:
                        continue
                    else:
                        move_on = True
                        adjacent_cell = (self.board.cells)[row+row_offset][col+col_offset]
                        if not adjacent_cell.contains_tile:
                            # Move the tile into the empty space
                            self.move_tile(source, dest)
                        else:
                            # Check if we can merge
                            can_merge = cell.tile.value == adjacent_cell.tile.value
                            if can_merge:
                                self.merge_tiles(source, dest)
                            else:
                                move_on = False
                                continue




    # Prints out the board
    def print_board(self):
        for row in self.board.cells:
            for cell in row:
                if (cell).contains_tile:
                    print(cell.tile.value, end=" ")
                else:
                    print(f".", end=" ")
            print()

    

    # Sets up all of the game state
    def setup_game(self):
        # Create board
        self.board = Board(Utility.DEFAULT_DIMS)
        self.dims = Utility.DEFAULT_DIMS

        # Fill board with two random tiles
        board = self.board
        rows = self.dims[0]
        cols = self.dims[1]
        for _ in range(2):
            self.place_random_tile(Utility.DEFAULT_TILE_VALUE)

    
    # Executes game loop
    def play_game(self):
        while True:
            self.print_board()
            print()
            print("Enter L, R, U, or D: ")
            dir_flag = input()

            # Compress the board after the move
            self.shift(Utility.dir_map[dir_flag.upper()])

            # Place a random '2' tile after compression
            self.place_random_tile(Utility.DEFAULT_TILE_VALUE)
            print()


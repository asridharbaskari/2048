class Board:
    cells = None
    num_tiles = 0
    def __init__(self, dims):
        self.rows = dims[0]
        self.cols = dims[1]
        self.cells = [[Cell(row, col) for col in range(self.rows)] for row in range(self.cols)]
    
    def get(self, pos):
        row, col = pos
        return (self.cells)[row][col]

    def out_of_bounds(self, i, j):
        return not ((i >= 0 and i < self.rows) and (j >= 0 and j < self.cols))
    
    def contains_tile(self, i, j):
        return (not self.out_of_bounds(i, j) and (self.cells[i][j]).contains_tile)

class Cell:
    contains_tile = False
    tile = None
    def __init__(self, row, col):
        self.row = row
        self.col = col



class Tile:
    value = -1
    # value: number that the tile displays
    def __init__(self, value):
        self.value = value
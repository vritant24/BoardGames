

class Grid:
    EMPTY = -1
    DIM = 10

    def __init__(self):
        self.grid = [
            [self.EMPTY for i in range(self.DIM)] for j in range(self.DIM)
        ]
    
    def updateGrid(self, row, col, new_val):
        if row < 0 or row >= self.DIM or col < 0 or col >= self.DIM:
            return False
        
        self.grid[row][col] = new_val
        return True
    
    def getCell(self, row, col):
        return self.grid[row][col]

    def getGrid(self):
        return self.grid
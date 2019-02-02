class Grid:
    def __init__(self):
        self.gameGrid = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]

    def move(self, row, col, player):
        if row > 2 or row < 0 or col > 2 or col < 0:
            return False
            
        if self.gameGrid[row][col] == -1:
            self.gameGrid[row][col] = player
            return True
        else:
            return False

    def checkWin(self):
        # check columns
        for col in range(3):
            if (self.gameGrid[0][col] == self.gameGrid[1][col]) and (self.gameGrid[1][col] == self.gameGrid[2][col]):
                if not (self.gameGrid[0][col] == -1):
                    return True
        
        # check rows
        for row in range(3):
            if (self.gameGrid[row][0] == self.gameGrid[row][1]) and (self.gameGrid[row][1] == self.gameGrid[row][2]):
                if not (self.gameGrid[0][col] == -1):
                    return True

        # check diagonals 
        if (self.gameGrid[0][0] == self.gameGrid[1][1]) and (self.gameGrid[1][1] == self.gameGrid[2][2]):
            if not (self.gameGrid[0][col] == -1):
                    return True
        if (self.gameGrid[0][2] == self.gameGrid[1][1]) and (self.gameGrid[1][1] == self.gameGrid[2][0]):
            if not (self.gameGrid[0][col] == -1):
                    return True
        
        # No winner found
        return False

    def getGrid(self):
        return self.gameGrid
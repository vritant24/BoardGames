from grid import Grid

class Game:
    PLAYER1 = "O"
    PLAYER2 = "X"
    MAX_MOVES = 9

    def __init__(self):
        # player can be 1 or 2
        self.player = 1 
        self.grid = Grid()
        self.moves = 0
    
    def displayGrid(self):
        currentGrid = self.grid.getGrid()

        for i in range(len(currentGrid)):
            for j in range(len(currentGrid[0])):
                if currentGrid[i][j] == 1:
                    print(f" {self.PLAYER1} ", end='')
                elif currentGrid[i][j] == 2:
                    print(f" {self.PLAYER2} ", end='')
                else:
                    print(" - ", end='')
            print("\n")

    def changePlayer(self):
        # change player
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def movePlayer(self, row, col):
        self.moves += 1
        canMove = self.grid.move(row, col, self.player)
        
        if(canMove):
            self.changePlayer()
        else:
            print("You cannot move there :(")

    def checkGameOver(self):
        # check if someone won
        if self.grid.checkWin():
            print(f"Winner is player{self.player}")
            return True
        
        # check if it's a draw
        if self.moves == self.MAX_MOVES:
            print("It's a draw!!")
            return True
        
        return False

    def play(self):
        while (not self.checkGameOver()):
            print("=====================")
            self.displayGrid()
            print(f"Player{self.player} Turn")

            row = input("input row to move to: ")
            col = input("input column to move to: ")
            
            self.movePlayer(int(row), int(col))
            print("=====================")

game = Game()

game.play()
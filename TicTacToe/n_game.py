player_1 = 'X'
player_2 = 'Y'
current_player = " ";
empty_cell = " "

grid = [
    [empty_cell, empty_cell, empty_cell],
    [empty_cell, empty_cell, empty_cell],
    [empty_cell, empty_cell, empty_cell]
]

def showGrid():
    # print column indices
    print("|" + grid[0][0] + "|" + grid[0][1] + "|" + grid[0][2] + "|")
    print("|" + grid[1][0] + "|" + grid[1][1] + "|" + grid[1][2] + "|")
    print("|" + grid[2][0] + "|" + grid[2][1] + "|" + grid[2][2] + "|")

def makeMove(player, row, column):
    grid[row][column] = player

def setCurrentPlayer(player):
    global current_player
    current_player = player

def changePlayer():
    if(current_player == player_1):
        setCurrentPlayer(player_2)
    else:
        setCurrentPlayer(player_1)

def isGameOver():
    return False

def playGame():
    # start game with player 1
    setCurrentPlayer(player_1)
    while(not isGameOver()):
        showGrid()
        row = input("input row to move to: ")
        col = input("input column to move to: ")
        makeMove(current_player, int(row), int(col))
        changePlayer()

playGame()



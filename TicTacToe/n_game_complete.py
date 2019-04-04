player_1 = 'X'
player_2 = 'Y'
current_player = " ";
moves = 0
empty_cell = " "

grid = [
    [empty_cell, empty_cell, empty_cell],
    [empty_cell, empty_cell, empty_cell],
    [empty_cell, empty_cell, empty_cell]
]

def showGrid():
    # print column indices
    print("  1 2 3")
    print("1|" + grid[0][0] + "|" + grid[0][1] + "|" + grid[0][2] + "|")
    print("2|" + grid[1][0] + "|" + grid[1][1] + "|" + grid[1][2] + "|")
    print("3|" + grid[2][0] + "|" + grid[2][1] + "|" + grid[2][2] + "|")

def canMove(row, col):
    if grid[row][col] == empty_cell:
        return True
    else:
        return False

def makeMove(player, row, col):
    global moves
    grid[row][col] = player
    moves += 1

def setCurrentPlayer(player):
    global current_player
    current_player = player

def changePlayer():
    if current_player == player_1:
        setCurrentPlayer(player_2)
    else:
        setCurrentPlayer(player_1)

def isGameOver():
    # check rows
    for row in range(3):
        if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2] and grid[row][0] != empty_cell:
            print("winner player: " + grid[row][0])
            return True
    
    # check columns
    for col in range(3):
        if grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col] and grid[0][col] != empty_cell:
            print("winner player: " + grid[0][col])
            return True
    
    # check diagonals
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] != empty_cell:
        print("winner player: " + grid[0][0])
        return True
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] != empty_cell:
        print("winner player: " + grid[0][2])
        return True

    # check if maximum number of moves have been made
    if moves >= 9:
        print("Draw")
        return True

    return False

def playGame():
    # start game with player 1
    setCurrentPlayer(player_1)
    showGrid()
    while not isGameOver():
        print(current_player + " turn")
        row = int(input("input row to move to: "))
        col = int(input("input column to move to: "))

        row = row - 1
        col = col - 1

        if canMove(row, col):
            makeMove(current_player, row, col)
            changePlayer()
        else:
            print("you cannot move there :(")
        showGrid()

playGame()



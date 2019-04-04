import random

MINE = -1
BLANK = 0
NOT_OPEN = -3
NUM_MINES = 10
GRID_SIZE = 8

def playGame():
    game_grid = initGrid(NOT_OPEN)
    grid = createGrid(NUM_MINES)
    printGrid(game_grid)
    print("")
    
    while True:
        r = int(input("row: "))
        c = int(input("col: "))

        if game_grid[r][c] == NOT_OPEN:
            if grid[r][c] is not MINE:
                openGrid(game_grid, grid, r, c, True)
            else: 
                print("GAME OVER")
                printGrid(grid)
                exit()
        printGrid(game_grid)
    

def openGrid(game_grid, grid, i, j, first):
    # if grid isn't blank, stop
    if game_grid[i][j] is not NOT_OPEN:
        return

    if not first:
        if grid[i][j] is not BLANK:
            return;

    game_grid[i][j] = grid[i][j]

    # NW
    if isValidIdx(i-1, j-1):
        openGrid(game_grid, grid, i-1, j-1, False)
    # N
    if isValidIdx(i-1, j):
        openGrid(game_grid, grid, i-1, j, False)
    # NE
    if isValidIdx(i-1, j+1):
        openGrid(game_grid, grid, i-1, j+1, False)
    # E
    if isValidIdx(i, j+1):
        openGrid(game_grid, grid, i, j+1, False)
    # SE
    if isValidIdx(i+1, j+1):
        openGrid(game_grid, grid, i+1, j+1, False)
    # S
    if isValidIdx(i+1, j):
        openGrid(game_grid, grid, i+1, j, False)
    # SW
    if isValidIdx(i+1, j-1):
        openGrid(game_grid, grid, i+1, j-1, False)
    # W
    if isValidIdx(i, j-1):
        openGrid(game_grid, grid, i, j-1, False)
    

###################################################
# create grid

def createGrid(num_mines):
    # create grid with all values as 0 
    grid = initGrid(BLANK)
    
    # add mines to the grid
    grid = addMines(grid, num_mines)

    # add numbers to the grid
    grid = fillNumbers(grid)

    return grid

def initGrid(default_val):
    grid = []
    for i in range(GRID_SIZE):
        tmp = []
        for j in range(GRID_SIZE):
            tmp.append(default_val)
        grid.append(tmp)
    return grid

def addMines(grid, num_mines):
    i = 0
    while i < num_mines:
        r = random.randint(0, GRID_SIZE - 1)
        c = random.randint(0, GRID_SIZE - 1)

        if grid[r][c] == BLANK:
            grid[r][c] = MINE
            i = i + 1;

    return grid

def fillNumbers(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == MINE:
                continue
            else:
                grid[i][j] = getMineCount(grid, i, j)
    return grid

def getMineCount(grid, i, j):
    count = 0
    # NW
    if isValidIdx(i-1, j-1):
        if grid[i-1][j-1] == MINE:
            count += 1
    # N
    if isValidIdx(i-1, j):
        if grid[i-1][j] == MINE:
            count += 1
    # NE
    if isValidIdx(i-1, j+1):
        if grid[i-1][j+1] == MINE:
            count += 1
    # E
    if isValidIdx(i, j+1):
        if grid[i][j+1] == MINE:
            count += 1
    # SE
    if isValidIdx(i+1, j+1):
        if grid[i+1][j+1] == MINE:
            count += 1
    # S
    if isValidIdx(i+1, j):
        if grid[i+1][j] == MINE:
            count += 1
    # SW
    if isValidIdx(i+1, j-1):
        if grid[i+1][j-1] == MINE:
            count += 1
    # W
    if isValidIdx(i, j-1):
        if grid[i][j-1] == MINE:
            count += 1
    
    return count

def isValidIdx(i, j):
    if i < 0 or i >= GRID_SIZE or j < 0 or j >= GRID_SIZE:
        return False
    else:
        return True

def printGrid(grid):
    for i in range(GRID_SIZE):
        print("|", end="")
        for j in range(GRID_SIZE):
            if grid[i][j]  ==  MINE:
                print("B | ", end="")
            elif grid[i][j] == NOT_OPEN:
                print("  | ", end="")
            else: 
                print( str(grid[i][j]) + " | ",  end="")
        print("")

# printGrid(createGrid(NUM_MINES))
playGame()
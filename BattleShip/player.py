from grid import Grid

boats = [
    dict(
        name = "carrier",
        length = 5
    ),
    dict(
        name = "Battleship",
        length = 4
    ),
    dict(
        name = "Cruiser",
        length = 3
    ),
    dict(
        name = "Submarine",
        length = 3
    ),
    dict(
        name = "Destroyer",
        length = 2
    )
]

class Player:
    HIT = 0
    MISS = 1
    BOAT = 2

    def __init__(self):
        self.boat_grid = Grid()
        self.move_grid = Grid()

    def setUpBoats(self):
        for boat in boats:
            self.displayBoatGrid()
            print(f"Enter the positioning for the {boat.name} of length {boat.length}")
            start_row = input("enter starting row")
            start_col = input("enter starting col")
            end_row = input("enter ending row")
            end_col = input("enter endling col")

            #TODO need to add error checking

            

    def displayBoatGrid(self) :
        currentGrid = self.boat_grid.getGrid()

        for i in range(len(currentGrid)):
            for j in range(len(currentGrid[0])):
                if currentGrid[i][j] == self.BOAT:
                    print(f" x ", end='')
                else:
                    print(" - ", end='')
            print("\n")


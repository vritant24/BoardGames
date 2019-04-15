from guess_number import LOWER, HIGHER, EQUAL, playGame

low = 0
high = 100

def getAvg(num1, num2):
    return int((num1 + num2) / 2)

def setLow(num):
    global low
    low = num

def setHigh(num):
    global high
    high = num

def gameRunnerBinarySearch(prompt):
    # first guess
    if prompt == None:
        return 50

    # change high and low accordingly
    if prompt == LOWER:
        setHigh(getAvg(high, low))
    elif prompt == HIGHER:
       setLow(getAvg(high, low))
    elif prompt == EQUAL:
        return
    
    # guess between high and low
    guess = getAvg(high, low)
    return guess

def simul():
    guesses = playGame(gameRunnerBinarySearch)
    print(f"guess taken = {guesses}")

simul()
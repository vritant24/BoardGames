from guess_number import EQUAL, playGame

last_guess = -1

def setLastGuess(num):
    global last_guess
    last_guess = num

def gameRunnerBruteForce(prompt):
    if prompt == EQUAL:
        return
    
    setLastGuess(last_guess + 1)
    return last_guess

def simul():
    guesses = playGame(gameRunnerBruteForce)
    print(guesses)

simul()
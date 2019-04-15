import random

LOWER = "lower"
HIGHER = "higher"
EQUAL = "equal"

chosen_one = -1

def setNewRandomNum():
    global chosen_one
    chosen_one = random.randint(1,101)

def getInput(prompt):
    if prompt != None:
        if prompt == EQUAL:
            # game ended
            print("You Got it!")
            return
        else:
            print(prompt)

    inp = input("Enter your guess")
    return int(inp)

# takes input gameRunner, that provides input by user or computer
# also known as dependency injection
def playGame(gameRunner):
    setNewRandomNum()
    print(chosen_one)
    print("Guess the number. It is between 1 and 100")
    
    guesses_made = 0 # track number of guesses made

    prompt = None
    while(True):
        #increment number of guesses made
        guesses_made += 1

        # get user / computer guess
        guess = gameRunner(prompt)

        # check user inout with chosen number
        prompt = guessNumber(guess)

        # end condition
        if prompt == EQUAL:
            gameRunner(prompt)
            break
    return guesses_made


# compare guess with chosen number
def guessNumber(num):
    if num == chosen_one:
        return EQUAL
    elif num > chosen_one:
        #guess needs to be lower
        return LOWER
    else:
        #guess needs to be higher
        return HIGHER

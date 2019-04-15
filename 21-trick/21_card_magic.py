import random

HEART = "\u2660"
SPADES = "\u2665"
DIAMOND = "\u2666"

def printArr(arr):
    i = 0
    while i < len(arr):
        print(str(arr[i]) + "  |  " + str(arr[i + 1]) + "  |  " + str(arr[i + 2]))
        i = i + 3

def printAndSelect(arr):
    col1 = []
    col2 = []
    col3 = []

    i = 0
    while i < len(arr):
        col1.append(arr[i])
        col2.append(arr[i+1])
        col3.append(arr[i+2])
        i = i + 3

    printArr(arr)
    choice = input("Enter column your card is in (1 or 2 or 3)")

    n_arr = []
    if choice == '1':
        # add col1 in the middle
        for el in col2:
            n_arr.append(el)
        for el in col1:
            n_arr.append(el)
        for el in col3:
            n_arr.append(el)
        
    elif choice == '2':
         # add col2 in the middle
        for el in col1:
            n_arr.append(el)
        for el in col2:
            n_arr.append(el)
        for el in col3:
            n_arr.append(el)
    else:
         # add col3 in the middle
        for el in col2:
            n_arr.append(el)
        for el in col3:
            n_arr.append(el)
        for el in col2:
            n_arr.append(el)

    return n_arr


def magic():
    arr = []

    print("Let's start the magic")

    for i in range(7):
        arr.append(str(i) + HEART)
        arr.append(str(i) + SPADES)
        arr.append(str(i) + DIAMOND)
    
    random.shuffle(arr)
    
    for i in range(3):
        arr = printAndSelect(arr)
    
    print("Your card is " + arr[10])

magic()
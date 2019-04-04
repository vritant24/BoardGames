import random

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
        return col2 + col1 + col3
    elif choice == '2':
        return col1 + col2 + col3
    else:
        return col1 + col3 + col2


def magic():
    arr = []

    print("Let's start the magic")

    for i in range(7):
        arr.append(str(i) + "\u2660")
        arr.append(str(i) + "\u2665")
        arr.append(str(i) + "\u2666")
    
    random.shuffle(arr)
    
    for i in range(3):
        arr = printAndSelect(arr)
    
    print("Your card is " + arr[10])

magic()
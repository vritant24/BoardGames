import random

deck = []

for n in ['2','3','4','5','6','7','8','9','X','*','*','*']:
    for c in ['R','G','B','Y']:
        deck.append(c+n)

def shuffle():
    for s in range(0,7):
        for i in range(0,len(deck)):
            r = random.randint(0,len(deck)-1)
            tmp = deck[i]
            deck[i] = deck[r]
            deck[r] = tmp
    return

def deal(hand1,hand2):
    for c in range(0,7):
        hand1.append(deck.pop())
        hand2.append(deck.pop())
    return

def printCard(stack,c,r):
    if len(stack[c]) > r:
        return stack[c][r] + " "
    return "   "

def drawBoard(s1,ss,s2,dk):
    print("\n\n|---------------------------|")
    print("| Game board (" + str(len(dk)) + " cards rem) |\n|   (X->10; *->2x,3x,4x)    |")
    print("|                           |")
    rowMax = max(len(s1[0]),len(s1[1]),len(s1[2]),len(s1[3]))-1
    for r in range(rowMax,-1,-1):
        rowStr = '|        '
        for c in range(0,4):
            rowStr = rowStr + printCard(s1,c,r)
        print(rowStr + '       |')
    print("|       -------------       |\n|discard " + ss[0][len(ss[0])-1] + " " +
          ss[1][len(ss[1])-1] + " " +
          ss[2][len(ss[2])-1] + " " +
          ss[3][len(ss[3])-1] + " discard|\n|       -------------       |")
    for r in range(0,max(len(s2[0]),len(s2[1]),len(s2[2]),len(s2[3]))):
        rowStr = '|        '
        for c in range(0,4):
            rowStr = rowStr + printCard(s2,c,r)
        print(rowStr + '       |')
    print("|                           |")
    print("|---------------------------|\n")
    return

def takeTurn(ph,ps,ss,dk):
    for i in range(0,7):
        print(str(i) + " - " + ph[i])
    print('')
    m = ''
    while (m is not 'p' and m is not 'd'):
        m = input("(p)lay or (d)iscard? ")
    done = False
    while not done:
        c = -1
        while (c < 0 or c > 6):
            c = int(input("Choose a card to play, 0-6: "))
        if ph[c][0] is 'R':
            s = 0
        elif ph[c][0] is 'G':
            s = 1
        elif ph[c][0] is 'B':
            s = 2
        elif ph[c][0] is 'Y':
            s = 3
        if m is 'd':
            ss[s].append(ph[c])
            ph.remove(ph[c])                       
            done = True
        else:
            if len(ps[s]) == 0 or ph[c] >= ps[s][len(ps[s])-1]:
                ps[s].append(ph[c])
                ph.remove(ph[c])
                done = True
            else:
                print("That card cannot be played.")
    m = ''
    if len(ss[0]) > 1 or len(ss[1]) > 1 or len(ss[2]) > 1 or len(ss[3]) > 1:
        while (m is not 'd' and m is not 's'):
            m = input("draw from (d)eck or (s)hared? ")
    else:
        m = 'd'
    if m is 'd':
        ph.append(dk[len(dk)-1])
        dk.remove(dk[len(dk)-1])
    else:
        shDraw = []
        if len(ss[0]) > 1:
            shDraw.append('r')
        if len(ss[1]) > 1:
            shDraw.append('g')
        if len(ss[2]) > 1:
            shDraw.append('b')
        if len(ss[3]) > 1:
            shDraw.append('y')
        drawStr = ''
        for ds in shDraw:
            drawStr = drawStr + '(' + ds + '), '
        drawStr = drawStr[0:len(drawStr)-2]
        s = ''
        while (s not in shDraw):
            s = input("Choose " + drawStr + ": ")
        if s is 'r':
            c = 0
        elif s is 'g':
            c = 1
        elif s is 'b':
            c = 2
        elif s is 'y':
            c = 3
        ph.append(ss[c][len(ss[c])-1])
        ss[c].remove(ss[c][len(ss[c])-1])
    return

def playerPoints(ps):
    pts = 0
    for s in ps:
        if len(s) > 0:
            bonus = 1
            spts = 0
            for c in s:
                if '*' in c:
                    bonus += 1
                elif 'X' in c:
                    spts += 10
                else:
                    spts += int(c[1:])
            pts = pts + ((spts - 20) * bonus)        
    return pts

def determineWinner(s1,s2):
    p1pts = playerPoints(s1)
    p2pts = playerPoints(s2)
    print("Player 1 scored " + str(p1pts) + " points")
    print("Player 2 scored " + str(p2pts) + " points")
    if p1pts > p2pts:
        print("Player 1 wins!")
    elif p2pts > p1pts:
        print("Player 2 wins!")
    else:
        print("Draw")
    return

def lostCities():
    shuffle()
    p1hand = []
    p2hand = []

    p1stacks = [[],[],[],[]]
    p2stacks = [[],[],[],[]]
    shstacks = [['RR'],['GG'],['BB'],['YY']]

    deal(p1hand,p2hand)
    turn = random.randint(1,2)

    while(len(deck) > 0):
        drawBoard(p1stacks,shstacks,p2stacks,deck)
        if turn == 1:
            print("Player 1: " + str(playerPoints(p1stacks)) + " points\n-------------------")
            takeTurn(p1hand,p1stacks,shstacks,deck)
            turn = 2
        else:
            print("Player 2: " + str(playerPoints(p2stacks)) + " points\n-------------------")
            takeTurn(p2hand,p2stacks,shstacks,deck)
            turn = 1

    determineWinner(p1stacks,p2stacks)
    return

lostCities()
import random

# characters
ALL         = -1 
DUKE        = 0
CAPTAIN     = 1
ASSASSIN    = 2
CONTESSA    = 3
AMBASSADOR  = 5

# actions
INCOME          = 6
FOREIGN_AID     = 7
COUP            = 8
TAX             = 9
ASSASSINATE     = 10
EXCHANGE_CARD   = 11
STEAL           = 12

# counteractions
BLOCK_FOREIGN_AID = 13
BLOCK_STEAL = 14
BLOCK_ASSASSINATION = 15

#dictionary to represent possible character actions
characters = {}

characters[ALL] = {}
characters[ALL][INCOME] = True
characters[ALL][FOREIGN_AID] = True
characters[ALL][ASSASSIN] = True

characters[CAPTAIN] = {}
characters[CAPTAIN][STEAL] = True
characters[CAPTAIN][BLOCK_STEAL] = True

characters[DUKE] = {}
characters[DUKE][TAX] = True
characters[DUKE][BLOCK_FOREIGN_AID] = True

characters[AMBASSADOR] = {}
characters[AMBASSADOR][EXCHANGE_CARD] = True
characters[AMBASSADOR][BLOCK_STEAL] = True

characters[CONTESSA] = {}
characters[BLOCK_ASSASSINATION] = True

characters[ASSASSIN] = {}
characters[ASSASSIN][ASSASSINATE] = True



class Actions:
    def income():
        #take 1 coin
        pass
    def foreignAid():
        #take 2 coins
        pass
    def coup():
        #pay 7 coins
        pass
    def tax():
        #take 3 coins
        pass
    def assassinate():
        #pay 3 coins
        pass
    def exchangeCard():
        #echange cards with deck
        pass
    def steal():
        #take 2 coins from other player
        pass

class CounterAction:
    def blockForeignAid(self, player_hand):
        #Duke
        pass
    def blockSteal(self, player_hand):
        #Ambassador and captain
        pass
    def blockAssassination(self, player_hand):
        #Contessa
        pass

class Deck:
    def __init__(self):
        # initialze list that represents deck
        # 0 - 4 represent the characters
        self.deck = []
        for i in range(5):
            self.deck.append(i)
            self.deck.append(i)
            self.deck.append(i)
        # shuffle deck
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.deck)
        self.top = 0
    
    def replaceNextCard(self, new_card):
        # exchange cards
        card = self.deck[self.top]
        self.deck[self.top] = new_card

        # shuffle if deck emptied
        self.top += 1
        if(self.top == 15):
            self.shuffle()

        return card

    def peekCard(self):
        return self.deck[self.top]
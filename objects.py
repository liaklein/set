from __future__ import print_function
import random

class Card():
    def __init__(self,color,number,shape,shading):
        self.attributes = {'color':color,'number':number,'shape':shape,'shading':shading}
    def __str__(self):
        return ' '.join([self.attributes['color'],self.attributes['number'],self.attributes['shape'],self.attributes['shading']])

class Deck():
    def __init__(self):
        self.cardList = self.initialize_cards()
        self.cardCount = 81
    def isEmpty(self):
        if self.cardCount == 0:
            return True
        else:
            return False
    def initialize_cards(self):
        cards = []
        colors = ['R','G','P']
        numbers = ['1','2','3']
        shapes = ['O','S','D']
        shadings = ['E','F','|']
        for color in colors:
            for number in numbers:
                for shape in shapes:
                    for shading in shadings:
                        cards.append(Card(color,number,shape,shading))
        return cards
    def dealCard(self):
        #if the deck is empty, return error
        if self.cardCount == 0:
            return 'NoCards'
        #remove and return a random card from the deck
        cardIndex = random.randint(0,self.cardCount-1)
        card = self.cardList[cardIndex]
        del self.cardList[cardIndex]
        #decrement the card cardCount
        self.cardCount -= 1
        return card

class Board():
    def __init__(self):
        self.deck = Deck()
        self.cards = self.initialize_cards()
        self.cardCount = 12
    def initialize_cards(self):
        cards = []
        for i in range(12):
            cards.append(self.deck.dealCard())
        return cards
    def isEmpty(self):
        if self.cardCount == 0:
            return True
        else:
            return False
    def display(self):
        for i in range(12):
            if i%3 == 0:
                print('\n\n')
            print('\t\t' + str(self.cards[i]),end = '')
    def replaceIndex(self,i):
        nextCard = self.deck.dealCard()
        if nextCard == 'NoCards':
            self.cards[i] = ''
            self.cardCount -= 1
        else:
            self.cards[i] = nextCard

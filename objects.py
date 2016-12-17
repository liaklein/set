from __future__ import print_function
import random

class bcolors:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ITALICS = '\033[3m'
   END = '\033[0m'

colors = {'R':bcolors.RED,'G':bcolors.GREEN,'P':bcolors.PURPLE}
shadings = {'E':bcolors.ITALICS,'F':bcolors.BOLD,'|':bcolors.UNDERLINE}
shapes = {'O':'O ','S':'S ','<>':'<>'}
class Card():
    def __init__(self,color,number,shape,shading):
        self.attributes = {'color':color,'number':number,'shape':shape,'shading':shading}
    #def __str__(self):
    #    return ' '.join([self.attributes['color'],self.attributes['number'],self.attributes['shape'],self.attributes['shading']])
    def __str__(self):
        st = colors[self.attributes['color']]
        st += shadings[self.attributes['shading']]
        for i in range(int(self.attributes['number'])):
            st += shapes[self.attributes['shape']]
        st += bcolors.END
        return st
    def __eq__(self, otherCard):
        return isinstance(otherCard, Card) and self.attributes == otherCard.attributes

class Deck():
    def __init__(self):
        self.cardList = self.initialize_cards()
    def isEmpty(self):
        return len(self.cardList) == 0
    def initialize_cards(self):
        cards = []
        colors = ['R','G','P']
        numbers = ['1','2','3'] #consider changing from strings to ints
        shapes = ['O','S','<>']
        shadings = ['E','F','|']
        for color in colors:
            for number in numbers:
                for shape in shapes:
                    for shading in shadings:
                        cards.append(Card(color,number,shape,shading))
        return cards

    def dealCard(self):
        #if the deck is empty, return error
        if self.isEmpty():
            return 'NoCards'
        #remove and return a random card from the deck
        cardIndex = random.randint(0,len(self.cardList)-1)
        card = self.cardList[cardIndex]
        del self.cardList[cardIndex]
        return card

class Board():
    def __init__(self):
        self.deck = Deck()
        self.cards = self.initialize_cards()
    def initialize_cards(self):
        cards = []
        for i in range(12):
            cards.append(self.deck.dealCard())
        return cards
    def isEmpty(self):
        return len(self.cards) == 0
    def display(self):
        for i in range(len(self.cards)):
            if i%3 == 0:
                print('\n\n')
            print('\t\t' + str(self.cards[i]),end = '')
    def replaceIndex(self,i):
        nextCard = self.deck.dealCard()
        if nextCard == 'NoCards':
            del self.cards[i]
        else:
            self.cards[i] = nextCard
    def addCard(self):
        nextCard = self.deck.dealCard()
        if nextCard != 'NoCards':
            self.cards.append(nextCard)
    def shiftCards(self,cs):
        numLeftoverCards = len(self.cards) - len(cs)
        replacers = [x for x in cs if x < numLeftoverCards]
        overs = [i for i in range(numLeftoverCards, len(self.cards)) if i not in
                cs]
        for r in replacers:
            index = overs.pop()
            self.cards[r] = self.cards[index]
        self.cards = self.cards[:numLeftoverCards]


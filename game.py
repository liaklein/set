from __future__ import print_function
from objects import *

def validSet(card1,card2,card3):
    for att in card1.attributes:
        att1 = card1.attributes[att]
        att2 = card2.attributes[att]
        att3 = card3.attributes[att]
        if not(allSame(att1,att2,att3) or allDifferent(att1,att2,att3)):
            return False
    return True
def allSame(att1,att2,att3):
    if att1 == att2 and att2 == att3:
        return True
    else:
        return False
def allDifferent(att1,att2,att3):
    if not att1 == att2 and not att2 == att3 and not att1 == att3:
        return True
    else:
        return False

def numSets(board):
    setCount = 0
    for i in range(len(board.cards)):
        for j in range(i):
            for k in range(j):
                c1 = board.cards[i]
                c2 = board.cards[j]
                c3 = board.cards[k]
                if validSet(c1, c2, c3):
                    setCount += 1
    return setCount

def printSetCount(board):
    setCount = numSets(board)
    print(str(setCount) + ' set', end='')
    if setCount != 1:
        print('s')
    else:
        print()

def validateInput(userInput, numCards=12):
    if not userInput:
        return
    cards = userInput.strip()
    if cards == 'add' or cards == '?':
        return cards
    cards = cards.split(' ')
    if len(cards) != 3:
        print('Invalid input')
        return
    # try to convert input to integers
    intCards = []
    for card in cards:
        try:
            intCard = int(card)
            intCards.append(intCard)
        except ValueError:
            print('Invalid input')
            return
    # numbers should be between 0 (inclusive) and numCards (exclusive) no duplicates
    intCards.sort()
    if intCards[0] < 0 or intCards[2] >= numCards or intCards[0] == intCards[1] or intCards[1] == intCards[2]:
        print('Invalid input')
        return
    return intCards

def main():
    score = 0
    board = Board()
    while not board.isEmpty():
        board.display()
        userInput = raw_input("\n\nPlease Enter Set in space separated list (e.g. 0 10 4): ")
        cards = validateInput(userInput, numCards=len(board.cards))
        if not cards:
            continue
        if cards == 'add':
            board.addCard()
            board.addCard()
            board.addCard()
            continue
        if cards == '?':
            printSetCount(board)
            continue
        c1,c2,c3 = cards
        print('\n\t\t' + str(board.cards[c1]) +  '\t\t' + str(board.cards[c2]) +
                '\t\t' + str(board.cards[c3]) + '\n')
        if validSet(board.cards[c1],board.cards[c2],board.cards[c3]):
            print('nice set')
            if len(board.cards) > 12:
                board.shiftCards([c1,c2,c3])
            else:
                board.replaceIndex(c1)
                board.replaceIndex(c2)
                board.replaceIndex(c3)
            score += 1
        else:
            print('Invalid Set')
            score -= 1
    print('Score: ' + str(score))

if __name__ == '__main__':
    main()

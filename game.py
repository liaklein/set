from objects import *
extra = False

def validSet(card1,card2,card3):
    print('\n\t\t' + str(card1) +  '\t\t' + str(card2) + '\t\t' + str(card3) + '\n')
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

def validateInput(userInput):
    cards = userInput.split(' ')
    if not cards or len(cards) != 3:
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
    # numbers should be between 0 and 11 inclusive, no duplicates
    intCards.sort()
    if intCards[0] < 0 or intCards[2] > 11 or intCards[0] == intCards[1] or intCards[1] == intCards[2]:
        print('Invalid input')
        return
    return intCards

def main():
    global extra
    score = 0
    board = Board()
    while not board.isEmpty():
        board.display()
        userInput = raw_input("\n\nPlease Enter Set in space separated list (e.g. 0 10 4): ")
        cards = validateInput(userInput)
        if not cards:
            continue
        c1,c2,c3 = cards
        if validSet(board.cards[c1],board.cards[c2],board.cards[c3]):
            print 'nice set'
            if extra:
                board.shiftCards([c1,c2,c3])
                extra = False
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

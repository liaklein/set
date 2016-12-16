from objects import *

def validSet(card1,card2,card3):
    for att in card1.attributes:
        att1 = card1.attributes[att]
        att2 = card2.attributes[att]
        att3 = card3.attributes[att]
        if not(allSame(att1,att2,att2) or allDifferent(att1,att2,att3)):
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

extra = False
def main():
    global extra
    score = 0
    board = Board()
    while not board.isEmpty():
        board.display()
        userInput = raw_input("\n\nPlease Enter Set in space separated list: ")
        userInput = userInput.strip()
        if userInput == 'add':
            board.addCard()
            board.addCard()
            board.addCard()
            extra = True
            continue
        c1,c2,c3 = userInput.split(' ')
        c1 = int(c1)
        c2 = int(c2)
        c3 = int(c3)
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

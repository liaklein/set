import unittest
import copy
from objects import *

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.b = Board()

    def testInit(self):
        self.assertIsNotNone(self.b.deck)
        self.assertIsNotNone(self.b.cards)
        self.assertEqual(len(self.b.cards), 12)

    def testIsEmpty(self):
        self.assertFalse(self.b.isEmpty())
        self.b.cards = []
        self.assertTrue(self.b.isEmpty())

    def testReplaceIndex(self):
        self.b.replaceIndex(0)
        self.assertIsInstance(self.b.cards[0], Card)
        self.assertEqual(len(self.b.cards), 12)

        self.b.deck.cardList = []
        self.b.replaceIndex(0)
        self.assertIsInstance(self.b.cards[0], Card)
        self.assertEqual(len(self.b.cards), 11)

    def testAddCard(self):
        self.b.addCard()
        self.assertEqual(len(self.b.cards), 13)
        self.b.deck.cardList = []
        self.b.addCard()
        self.assertEqual(len(self.b.cards), 13)

    def testShiftCards_empty(self):
        oldCardArrangement = copy.deepcopy(self.b.cards)
        self.b.shiftCards([])
        self.assertEqual(self.b.cards, oldCardArrangement)

    def testShiftCards_inBeginning(self):
        oldCardArrangement = copy.deepcopy(self.b.cards)
        self.b.shiftCards([1, 5, 7])
        self.assertEqual(len(self.b.cards), 9)
        # cards 1, 5, 7 should be replaced by cards 11, 10, 9
        self.assertEqual(self.b.cards[1], oldCardArrangement[11])
        self.assertEqual(self.b.cards[5], oldCardArrangement[10])
        self.assertEqual(self.b.cards[7], oldCardArrangement[9])
        # other cards should have stayed the same
        for i in range(9):
            if i != 1 and i != 5 and i != 7:
                self.assertEqual(self.b.cards[i], oldCardArrangement[i])

    def testShiftCards_mixed(self):
        oldCardArrangement = copy.deepcopy(self.b.cards)
        self.b.shiftCards([1, 5, 10])
        self.assertEqual(len(self.b.cards), 9)
        # cards 1 and 5 should have been replaced by cards 11 and 9
        self.assertEqual(self.b.cards[1], oldCardArrangement[11])
        self.assertEqual(self.b.cards[5], oldCardArrangement[9])
        # other cards should have stayed the same
        for i in range(9):
            if i != 1 and i != 5:
                self.assertEqual(self.b.cards[i], oldCardArrangement[i])

    def testShiftCards_atEnd(self):
        oldCardArrangement = copy.deepcopy(self.b.cards)
        self.b.shiftCards([9, 10, 11])
        self.assertEqual(len(self.b.cards), 9)
        # no cards should be replaced
        self.assertEqual(self.b.cards, oldCardArrangement[:9])

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.d = Deck()

    def testInit(self):
        self.assertIsNotNone(self.d.cardList)
        self.assertEqual(len(self.d.cardList), 81)
        # TODO: add more assertions for this?

    def testDealCard(self):
        card = self.d.dealCard()
        self.assertEqual(len(self.d.cardList), 80)
        self.assertIsInstance(card, Card)
        self.assertNotIn(card, self.d.cardList)

    def testIsEmpty(self):
        self.assertFalse(self.d.isEmpty())
        self.d.cardList = []
        self.assertTrue(self.d.isEmpty())

class TestCard(unittest.TestCase):

    def setUp(self):
        self.c = Card('R','3','O','E')

    def testInit(self):
        self.assertEqual(self.c.attributes['color'], 'R')
        self.assertEqual(self.c.attributes['number'], '3')
        self.assertEqual(self.c.attributes['shape'], 'O')
        self.assertEqual(self.c.attributes['shading'], 'E')

    # TODO
    def testStr(self):
        pass

    def testEq(self):
        otherCard = Card('R','3','O','E')
        self.assertEqual(self.c, otherCard)
        otherCard2 = Card('G','3','O','E')
        self.assertNotEqual(self.c, otherCard)

if __name__ == '__main__':
    boardSuite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    unittest.TextTestRunner(verbosity=2,buffer=True).run(boardSuite)

    deckSuite = unittest.TestLoader().loadTestsFromTestCase(TestDeck)
    unittest.TextTestRunner(verbosity=2,buffer=True).run(deckSuite)

    cardSuite = unittest.TestLoader().loadTestsFromTestCase(TestCard)
    unittest.TextTestRunner(verbosity=2,buffer=True).run(cardSuite)





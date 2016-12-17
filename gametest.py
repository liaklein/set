import unittest
from game import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.b = Board()

    def testValidSet(self):
        # c1, c2, c3 is a set
        # c1, c4, c5 is a set
        c1 = Card('R','1','O','E')
        c2 = Card('R','2','O','E')
        c3 = Card('R','3','O','E')
        c4 = Card('G','2','<>','|')
        c5 = Card('P','3','S','F')
        self.assertTrue(validSet(c1, c2, c3))
        self.assertFalse(validSet(c1, c2, c4))
        self.assertTrue(validSet(c1, c4, c5))

    def testAllSame(self):
        self.assertTrue(allSame('E','E','E'))
        self.assertFalse(allSame('E','E','|'))
        self.assertFalse(allSame('E','F','|'))

    def testAllDifferent(self):
        self.assertFalse(allDifferent('E','E','E'))
        self.assertFalse(allDifferent('E','E','|'))
        self.assertTrue(allDifferent('E','F','|'))

    def testNumSets(self):
        # c1, c2, c3 is a set
        # c1, c4, c5 is a set
        c1 = Card('R','1','O','E')
        c2 = Card('R','2','O','E')
        c3 = Card('R','3','O','E')
        c4 = Card('G','2','<>','|')
        c5 = Card('P','3','S','F')
        self.b.cards = []
        self.assertEqual(numSets(self.b), 0)
        self.b.cards.append(c1)
        self.assertEqual(numSets(self.b), 0)
        self.b.cards.append(c2)
        self.assertEqual(numSets(self.b), 0)
        self.b.cards.append(c3)
        self.assertEqual(numSets(self.b), 1)
        self.b.cards.append(c4)
        self.assertEqual(numSets(self.b), 1)
        self.b.cards.append(c5)
        self.assertEqual(numSets(self.b), 2)

    def testValidateInput_specialInput(self):
        self.assertEqual(validateInput('add'), 'add')
        self.assertEqual(validateInput('?'), '?')

    def testValidateInput_invalidInput(self):
        self.assertIsNone(validateInput(None))
        self.assertIsNone(validateInput(''))
        self.assertIsNone(validateInput('0 1'))
        self.assertIsNone(validateInput('0 1 2 3'))
        self.assertIsNone(validateInput('a b c'))
        self.assertIsNone(validateInput('2 -1 3'))
        self.assertIsNone(validateInput('3 14 2'))
        self.assertIsNone(validateInput('2 3 3'))
        self.assertIsNone(validateInput('2 2 3'))
        # limit is currently 11
        self.assertIsNone(validateInput('2 3 12'))

    def testValidateInput_validInput(self):
        self.assertEqual(validateInput('0 3 11'), [0, 3, 11])
        self.assertEqual(validateInput('11 0 3'), [0, 3, 11])
        self.assertEqual(validateInput('2 3 12', numCards=15), [2, 3, 12])



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGame)
    unittest.TextTestRunner(verbosity=2,buffer=True).run(suite)





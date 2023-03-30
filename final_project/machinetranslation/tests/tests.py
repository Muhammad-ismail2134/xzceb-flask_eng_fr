import sys
import unittest
sys.path.insert(0,'..')

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Function to test Null input
    """
    def testNull(self):
        self.assertEqual(english_to_french(None),"Error: Null input")
    """
    Function to test on valid input
    """
    def testValid(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """
    Function to test Null input
    """
    def testNull(self):
        self.assertEqual(french_to_english(None),"Error: Null input")
    """
    Function to test on valid input
    """
    def testValid(self):
        self.assertEqual(french_to_english('Bonjour'),"Hello")

unittest.main()
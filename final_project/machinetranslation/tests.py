'''Going to test if the translation works'''
import unittest

from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    '''
    Test the French to English Translation
    '''
    def test1(self):
        '''Test with Bonjour and Oui'''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Oui'), 'Yes')

class TestEnglishToFrench(unittest.TestCase):
    '''
    Test the English to French Translation
    '''
    def test1(self):
        '''Test with Hello and Yes'''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Yes'), 'Oui')

unittest.main()

import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_eng_to_fren(self):
        value = 'Hello'
        self.assertIsNotNone(value,"It is not none")
        self.assertEqual(english_to_french(value),'Bonjour')

    def test_fren_to_eng(self):
        value = 'Bonjour'
        self.assertIsNotNone(value,"it is not none")
        self.assertEqual(french_to_english(value),'Hello')

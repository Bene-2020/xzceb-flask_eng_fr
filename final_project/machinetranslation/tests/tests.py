import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_hello(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test_englishToFrench_hello1(self):
        self.assertEqual(englishToFrench('None'), 'Néant')
    def test_englishToFrench_hello2(self):
        self.assertEqual(englishToFrench('0'), '0')

    def test_frenchToEnglish_bonjour(self):
        self.assertEqual(frenchToEnglish('bonjour'), 'Hello')
    def test_frenchToEnglish_bonjour1(self):
        self.assertEqual(frenchToEnglish('None'), 'None')
    def test_frenchToEnglish_bonjour2(self):
        self.assertEqual(frenchToEnglish('0'), '0')

if __name__ == '__main__':
    unittest.main()
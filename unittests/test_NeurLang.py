import unittest
from ..NeurLang import NeurLang



class test_NeurLang(unittest.TestCase):

    test_path = "test.nl"
    testNeurLang = NeurLang(test_path)

    def test_fileLoader(self):

        self.assertEqual(len(testNeurLang.load_file(test_path)), 10)

    #test_fileLoader(self):
    #    self.assertEqual(testscanner.end,)

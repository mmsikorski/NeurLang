import unittest
from ..NeurLang import scanner.*



class test_scanner(unittest.TestCase):

    test_path = "test.nl"
    testscanner = Scanner(test_path)

    #test_fileLoader(self):
    #    self.assertEqual(testscanner.end,)

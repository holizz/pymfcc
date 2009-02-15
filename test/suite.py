
import unittest
from pymfcc import *

class TestPyMFCC(unittest.TestCase):
    def test_mel_imel(self):
        self.assertAlmostEqual(imel(mel(6)), 6)
        self.assertAlmostEqual(mel(imel(6)), 6)

if __name__ == '__main__':
    unittest.main()

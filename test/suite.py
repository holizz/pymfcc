
import unittest
import numpy
from pymfcc import *

class TestPyMFCC(unittest.TestCase):
    def test_mel_imel(self):
        self.assertAlmostEqual(imel(mel(6)), 6)
        self.assertAlmostEqual(mel(imel(6)), 6)

    def test_window_1d(self):
        signal = numpy.arange(1000)
        self.assertRaises(TypeError,lambda:window(signal, 10, 20))

    def test_window_2d(self):
        signal = numpy.array([numpy.arange(1000)])
        self.assertRaises(TypeError,lambda:window(signal, 10, 20))

    def test_window_2d_transposed(self):
        signal = numpy.array([numpy.arange(1000)]).transpose()
        frames = window(signal, 10, 20)
        self.assertFalse(frames==None)
        self.assert_((frames[:,2]==list(range(20,40))).all())
        self.assert_((frames[:,-1]==list(range(980,1000))).all())
        self.assertEqual(frames.shape[1], 99)

if __name__ == '__main__':
    unittest.main()

import unittest
import test

class TestMethods(unittest.TestCase):

    def test_twelve(self):
        assert test.between(12, 00) == 0

    def test_three(self):
        assert test.between(3, 00) == 90

suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner().run(suite)

import unittest
from test import Test

class TestMethods(unittest.TestCase):
    
    def test_twelve(self):
        test = Test()
        assert test.between(12, 00) == 0

suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner().run(suite)

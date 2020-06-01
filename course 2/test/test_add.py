from function import add

import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.m = "Hello"

    def test_add(self):
        self.assertEqual(add(5,6),11)

    def test_negative(self):
        self.assertRaises(ValueError,add,2,3)

    def tearDown(self):
        self.m = "Bye"

unittest.main()

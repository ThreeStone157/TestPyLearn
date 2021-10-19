#encoding: utf-8
import unittest

def add(x, y):
    return x+y

class TAdd(unittest.TestCase):

    def setUp(self):
        print("setUp")

    def test_add1(self):
        print("1111")
        self.assertEqual(add(1, 2), 3)

    def test_add2(self):
        print("2222")
        self.assertEqual(add(1, 5), 6)
    def tearDown(self):
        print("tearDown")


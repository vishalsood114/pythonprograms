import unittest
import mywraps

class SimpleTest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(1+1, 2)
    

class WrapTest(unittest.TestCase):
    def test_splitline(self):
        self.assertEqual(mywraps.splitline("",3),[""])
        self.assertEqual(mywraps.splitline("a",3),["a"])
        self.assertEqual(mywraps.splitline("abc",3),["abc"])
        self.assertEqual(mywraps.splitline("abcd",3),["abc","d"])

if __name__ == "__main__":
    unittest.main()

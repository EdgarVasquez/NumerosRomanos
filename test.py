import unittest
import UnitTest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("only positive numbers or decimal with . are allowed", UnitTest.Validation("1,2"))  # add assertion here


if __name__ == '__main__':
    unittest.main()

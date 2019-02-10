import unittest
import example


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        c = example.addition(1, 2)
        self.assertEqual(c, 1 + 2)


if __name__ == '__main__':
    unittest.main()

import unittest
from array_list import ArrayList

class TestArrayList(unittest.TestCase):
    def test_length_and_append(self):
        lst = ArrayList()
        self.assertEqual(lst.length(), 0)
        lst.append('a')
        lst.append('b')
        self.assertEqual(lst.length(), 2)
        self.assertEqual(lst.get(0), 'a')
        self.assertEqual(lst.get(1), 'b')

if __name__ == '__main__':
    unittest.main()
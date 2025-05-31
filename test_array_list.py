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

    def test_insert_valid_and_invalid(self):
        lst = ArrayList()
        lst.append('a')
        lst.insert('b', 1)  # insert at end
        lst.insert('c', 0)  # insert at beginning
        self.assertEqual(lst.get(0), 'c')
        self.assertEqual(lst.get(1), 'a')
        self.assertEqual(lst.get(2), 'b')
        with self.assertRaises(IndexError):
            lst.insert('d', -1)
        with self.assertRaises(IndexError):
            lst.insert('e', 10)

    def test_delete_valid_and_invalid(self):
        lst = ArrayList()
        lst.append('x')
        lst.append('y')
        deleted = lst.delete(0)
        self.assertEqual(deleted, 'x')
        self.assertEqual(lst.length(), 1)
        with self.assertRaises(IndexError):
            lst.delete(5)
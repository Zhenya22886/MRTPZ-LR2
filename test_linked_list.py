import unittest
from linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_append_and_length_and_get(self):
        lst = DoublyLinkedList()
        self.assertEqual(lst.length(), 0)

        lst.append('a')
        lst.append('b')
        lst.append('c')

        self.assertEqual(lst.length(), 3)
        self.assertEqual(lst.get(0), 'a')
        self.assertEqual(lst.get(1), 'b')
        self.assertEqual(lst.get(2), 'c')

        with self.assertRaises(IndexError):
            lst.get(3)

if __name__ == '__main__':
    unittest.main()

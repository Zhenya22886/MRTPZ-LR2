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

    def test_insert_at_positions_and_invalid(self):
        lst = DoublyLinkedList()
        lst.append('b')
        lst.append('d')

        lst.insert('a', 0)  # вставка на початок
        lst.insert('c', 2)  # вставка в середину
        lst.insert('e', 4)  # вставка в кінець

        self.assertEqual(lst.length(), 5)
        self.assertEqual(lst.get(0), 'a')
        self.assertEqual(lst.get(1), 'b')
        self.assertEqual(lst.get(2), 'c')
        self.assertEqual(lst.get(3), 'd')
        self.assertEqual(lst.get(4), 'e')

        with self.assertRaises(IndexError):
            lst.insert('x', -1)
        with self.assertRaises(IndexError):
            lst.insert('x', 10)
			
    def test_delete_head_tail_middle_and_invalid(self):
        lst = DoublyLinkedList()
        lst.append('a')
        lst.append('b')
        lst.append('c')
        lst.append('d')

        deleted = lst.delete(0)  # видаляємо з голови
        self.assertEqual(deleted, 'a')
        self.assertEqual(lst.length(), 3)
        self.assertEqual(lst.get(0), 'b')

        deleted = lst.delete(2)  # видаляємо з хвоста
        self.assertEqual(deleted, 'd')
        self.assertEqual(lst.length(), 2)

        deleted = lst.delete(1)  # видаляємо з середини
        self.assertEqual(deleted, 'c')
        self.assertEqual(lst.length(), 1)
        self.assertEqual(lst.get(0), 'b')

        with self.assertRaises(IndexError):
            lst.delete(-1)

        with self.assertRaises(IndexError):
            lst.delete(10)

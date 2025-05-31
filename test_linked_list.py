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

        lst.insert('a', 0)  
        lst.insert('c', 2)  
        lst.insert('e', 4)  

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

        deleted = lst.delete(0)  
        self.assertEqual(deleted, 'a')
        self.assertEqual(lst.length(), 3)
        self.assertEqual(lst.get(0), 'b')

        deleted = lst.delete(2)  
        self.assertEqual(deleted, 'd')
        self.assertEqual(lst.length(), 2)

        deleted = lst.delete(1)  
        self.assertEqual(deleted, 'c')
        self.assertEqual(lst.length(), 1)
        self.assertEqual(lst.get(0), 'b')

        with self.assertRaises(IndexError):
            lst.delete(-1)

        with self.assertRaises(IndexError):
            lst.delete(10)

    def test_deleteAll_and_clear(self):
        lst = DoublyLinkedList()
        lst.append('x')
        lst.append('y')
        lst.append('x')
        lst.append('z')
        lst.append('x')

        lst.deleteAll('x')
        self.assertEqual(lst.length(), 2)
        self.assertEqual(lst.get(0), 'y')
        self.assertEqual(lst.get(1), 'z')
        self.assertEqual(lst.findFirst('x'), -1)

        
        lst.clear()
        self.assertEqual(lst.length(), 0)

        with self.assertRaises(IndexError):
            lst.get(0)


    def test_clone_and_reverse(self):
        lst = DoublyLinkedList()
        for ch in ['a', 'b', 'c']:
            lst.append(ch)

        clone = lst.clone()
        self.assertEqual(clone.length(), 3)
        self.assertEqual(clone.get(0), 'a')
        self.assertEqual(clone.get(2), 'c')

        
        clone.append('d')
        self.assertEqual(clone.length(), 4)
        self.assertEqual(lst.length(), 3)

        
        lst.reverse()
        self.assertEqual(lst.get(0), 'c')
        self.assertEqual(lst.get(1), 'b')
        self.assertEqual(lst.get(2), 'a')

    def test_findFirst_and_findLast(self):
        lst = DoublyLinkedList()
        lst.append('x')
        lst.append('y')
        lst.append('x')
        lst.append('z')
        lst.append('x')

        self.assertEqual(lst.findFirst('x'), 0)
        self.assertEqual(lst.findLast('x'), 4)
        self.assertEqual(lst.findFirst('q'), -1)

    def test_extend(self):
        lst1 = DoublyLinkedList()
        lst2 = DoublyLinkedList()
        lst1.append('a')
        lst2.append('b')
        lst2.append('c')

        lst1.extend(lst2)

        self.assertEqual(lst1.length(), 3)
        self.assertEqual(lst1.get(1), 'b')
        self.assertEqual(lst1.get(2), 'c')
        self.assertEqual(lst2.length(), 2)
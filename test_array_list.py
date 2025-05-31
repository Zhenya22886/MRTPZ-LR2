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

    def test_delete_all_and_clear(self):
        lst = ArrayList()
        lst.append('a')
        lst.append('b')
        lst.append('a')
        lst.deleteAll('a')
        self.assertEqual(lst.length(), 1)
        self.assertEqual(lst.get(0), 'b')
        lst.clear()
        self.assertEqual(lst.length(), 0)

    def test_clone_and_reverse(self):
        lst = ArrayList()
        lst.append('x')
        lst.append('y')
        clone = lst.clone()
        self.assertEqual(clone.get(0), 'x')
        self.assertEqual(clone.get(1), 'y')
        lst.reverse()
        self.assertEqual(lst.get(0), 'y')
        self.assertEqual(lst.get(1), 'x')

    def test_findFirst_and_findLast(self):
        lst = ArrayList()
        lst.append('a')
        lst.append('b')
        lst.append('a')
        self.assertEqual(lst.findFirst('a'), 0)
        self.assertEqual(lst.findLast('a'), 2)
        self.assertEqual(lst.findFirst('z'), -1)

    def test_extend(self):
        lst1 = ArrayList()
        lst2 = ArrayList()
        lst1.append('1')
        lst2.append('2')
        lst2.append('3')
        lst1.extend(lst2)
        self.assertEqual(lst1.length(), 3)
        self.assertEqual(lst1.get(1), '2')
        self.assertEqual(lst1.get(2), '3')
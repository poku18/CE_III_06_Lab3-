import unittest
from BST import BinarySearchTree
class BSTTestCase(unittest.TestCase):

    def test_bstTest(self):
        bst=BinarySearchTree()

        bst.add(10, "A value")
        self.assertEqual(bst._size(), 1)
        
        bst.add(5, "B value")
        self.assertEqual(bst._size(), 2)

        bst.add(30, "C value")
        self.assertEqual(bst._size(), 3)

        self.assertListEqual(bst.inOrderWalk(), [5, 10, 30])
        self.assertListEqual(bst.preOrderWalk(), [10, 5, 30])
        self.assertListEqual(bst.postOrderWalk(), [5, 30, 10])

        self.assertEqual(bst.find_smallest(), 5)
        self.assertEqual(bst.find_largest(), 30)

        

if __name__  == '__main__':
    unittest.main()

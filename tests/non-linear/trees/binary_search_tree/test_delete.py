import pytest
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

def test_delete_empty_tree():
    """
    Tests the delete operation on an empty tree.
    """
    bst = BinarySearchTree()
    bst.delete(10)  # Should not raise any errors
    assert bst.root is None, "Deleting from an empty tree should do nothing."

def test_delete_leaf_node():
    """
    Tests the deletion of a leaf node.
    A leaf node is a node with no children.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.delete(5)
    assert not bst.search(5), "Leaf node 5 should be deleted."

def test_delete_traverse_right_subtree():
    """
    Tests the deletion of a node located in the right subtree.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)
    bst.delete(15)
    assert not bst.search(15), "Node 15 should be deleted."
    assert bst.root.right.key == 20, "Node 20 should replace node 15 in the right subtree."

def test_delete_node_with_one_child():
    """
    Tests the deletion of a node that has only one child.
    Making sure the child node replaces the deleted node.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(3)
    bst.delete(5)
    assert not bst.search(5), "Node 5 should be deleted."
    assert bst.root.left.key == 3, "Node 3 should replace node 5."

def test_delete_node_with_two_children():
    """
    Tests the deletion of a node that has two children.
    Making sure the node is replaced by its successor.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(7)
    bst.delete(5)
    bst.delete(10)
    assert bst.root.key == 7, "Node 7 should replace node 5."

def test_delete_root_node():
    """
    Tests the deletion of the root node.
    Making sure the tree handles the root deletion.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.delete(10)
    assert not bst.search(10), "Root node 10 should be deleted."

def test_delete_complex_tree():
    """
    Tests the deletion of a node in a more complex tree structure.
    """
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    bst.insert(5)
    bst.insert(15)
    bst.insert(25)
    bst.insert(35)
    bst.delete(20)  # Delete root with two children
    assert not bst.search(20), "Root 20 should be deleted."
    assert bst.root.key == 25, "Root should now be replaced by in-order successor 25."
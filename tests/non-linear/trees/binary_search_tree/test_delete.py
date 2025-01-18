import pytest
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

@pytest.fixture
def bst():
    r"""
    Fixture to create a Binary Search Tree (BST) with predefined values.
    The tree structure before deletion:
             20
            /  \
          10   30
         /  \   /  \
        5   15 25  35
    """
    elements = [20, 10, 30, 5, 15, 25, 35]
    return BinarySearchTree.list_to_tree(elements)

def test_delete_empty_tree():
    """
    Tests the delete operation on an empty tree.
    Deleting a key from an empty BST should not cause any errors.
    """
    bst = BinarySearchTree()
    bst.delete(10)
    assert bst.root is None, "Deleting from an empty tree should do nothing."

def test_delete_leaf_node(bst):
    """
    Tests the deletion of a leaf node (node with no children).
    """
    bst.delete(5)
    assert bst.search(5) is None, "Leaf node 5 should be deleted."

def test_delete_traverse_right_subtree(bst):
    """
    Tests the deletion of a node located in the right subtree.
    """
    bst.delete(30)
    assert bst.search(30) is None, "Node 30 should be deleted."
    assert bst.root.right.key == 35, "Node 35 should replace node 30 in the right subtree."

def test_delete_node_with_one_child(bst):
    """
    Tests the deletion of a node with only one child.
    The child node should replace the deleted node.
    """
    bst.delete(10)
    assert bst.search(10) is None, "Node 10 should be deleted."
    assert bst.root.left.key == 15, "Node 15 should replace node 10."

def test_delete_node_with_two_children(bst):
    """
    Tests the deletion of a node that has two children.
    The node should be replaced by its in-order successor.
    """
    bst.delete(20)
    assert bst.search(20) is None, "Node 20 should be deleted."
    assert bst.root.key == 25, "Root should now be replaced by in-order successor 25."

def test_delete_root_node():
    """
    Tests the deletion of the root node.
    The tree should correctly handle deleting the root.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.delete(10)
    assert bst.search(10) is None, "Root node 10 should be deleted."

def test_delete_complex_tree(bst):
    """
    Tests the deletion of a node in a complex tree structure.
    Ensures the BST maintains correct structure after deletion.
    """
    bst.delete(20)  # Deleting root with two children
    assert bst.search(20) is None, "Root 20 should be deleted."
    assert bst.root.key == 25, "Root should now be replaced by in-order successor 25."
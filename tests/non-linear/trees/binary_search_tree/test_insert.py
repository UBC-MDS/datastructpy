import pytest
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

@pytest.fixture
def bst():
    """
    Fixture to create an empty Binary Search Tree (BST) for insertion tests.
    """
    return BinarySearchTree()

def test_insert_root(bst):
    """
    Tests inserting the first value into an empty BST.
    """
    bst.insert(10)
    assert bst.root.key == 10, "The root key should be 10."

def test_insert_left_child(bst):
    """
    Tests inserting a value smaller than the root, forming a left child.
    """
    bst.insert(10)
    bst.insert(5)
    assert bst.root.left.key == 5, "The left child key should be 5."

def test_insert_right_child(bst):
    """
    Tests inserting a value larger than the root, forming a right child.
    """
    bst.insert(10)
    bst.insert(15)
    assert bst.root.right.key == 15, "The right child key should be 15."

def test_insert_duplicate_break(bst):
    """
    Tests that inserting a duplicate key does not alter the tree structure.
    """
    bst.insert(10)
    bst.insert(5)
    bst.insert(10)  # Duplicate value
    bst.insert(5)   # Duplicate left child value
    assert bst.root.key == 10, "The root key should remain 10."
    assert bst.root.left.key == 5, "The left child should remain 5."
    assert bst.root.right is None, "There should be no right child."

def test_insert_multiple_levels(bst):
    """
    Tests inserting values to form a deeper tree structure.
    """
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    bst.insert(18)
    assert bst.root.left.key == 5, "The left child of the root should be 5."
    assert bst.root.right.key == 15, "The right child of the root should be 15."
    assert bst.root.right.left.key == 12, "The left child of 15 should be 12."
    assert bst.root.right.right.key == 18, "The right child of 15 should be 18."

def test_insert_error_non_integer(bst):
    """
    Tests inserting a non-integer value to check error handling.
    """
    with pytest.raises(TypeError, match="Only integers are allowed in the BST."):
        bst.insert("string")

def test_insert_error_none(bst):
    """
    Tests inserting None to check error handling.
    """
    with pytest.raises(TypeError, match="None values are not allowed in the BST."):
        bst.insert(None)
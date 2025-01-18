import pytest
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree


def test_insert_root():
    """Test inserting the first value into an empty BST."""
    bst = BinarySearchTree()
    bst.insert(10)
    assert bst.root.key == 10, "The root key should be 10."

def test_insert_left_child():
    """Test inserting a value smaller than the root, forming a left child."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    assert bst.root.left.key == 5, "The left child key should be 5."

def test_insert_right_child():
    """Test inserting a value larger than the root, forming a right child."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    assert bst.root.right.key == 15, "The right child key should be 15."

def test_insert_duplicate_break():
    """Test that inserting a duplicate key hits the break logic."""
    bst = BinarySearchTree()
    bst.insert(10)  # Insert the root
    bst.insert(5)   # Insert a left child
    bst.insert(10)  # Insert duplicate value (should trigger the break statement)
    bst.insert(5)   # Insert duplicate left child value (should trigger the break statement)
    # Assert tree structure remains correct
    assert bst.root.key == 10, "The root key should remain 10."
    assert bst.root.left.key == 5, "The left child should remain 5."
    assert bst.root.right is None, "There should be no right child."

def test_insert_multiple_levels():
    """Test inserting values to form a deeper tree structure."""
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    bst.insert(18)
    assert bst.root.left.key == 5, "The left child of the root should be 5."
    assert bst.root.right.key == 15, "The right child of the root should be 15."
    assert bst.root.right.left.key == 12, "The left child of 15 should be 12."
    assert bst.root.right.right.key == 18, "The right child of 15 should be 18."

def test_insert_error_non_integer():
    """Test inserting a non-integer value to check error handling."""
    bst = BinarySearchTree()
    with pytest.raises(TypeError, match="Only integers are allowed in the BST."):
        bst.insert("string")  # Attempt to insert a string

def test_insert_error_none():
    """Test inserting None to check error handling."""
    bst = BinarySearchTree()
    with pytest.raises(TypeError, match="None values are not allowed in the BST."):
        bst.insert(None)  # Attempt to insert None

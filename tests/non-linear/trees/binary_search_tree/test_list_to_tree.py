import pytest
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

@pytest.mark.parametrize("elements, expected_root, expected_left, expected_right", [
    ([10, 5, 15, 12, 20], 10, 5, 15),  
    ([30, 20, 40, 35, 50], 30, 20, 40),  
])
def test_list_to_tree_valid_input(elements, expected_root, expected_left, expected_right):
    """
    Tests creating a Binary Search Tree (BST) from a list of elements.
    Ensures the root and its immediate children are correctly assigned.
    """
    bst = BinarySearchTree.list_to_tree(elements)
    
    assert bst.root.key == expected_root, f"Expected root key {expected_root}, got {bst.root.key}"
    assert bst.root.left.key == expected_left, f"Expected left child {expected_left}, got {bst.root.left.key}"
    assert bst.root.right.key == expected_right, f"Expected right child {expected_right}, got {bst.root.right.key}"

def test_list_to_tree_not_a_list():
    """
    Tests that passing a non-list input raises a ValueError.
    """
    with pytest.raises(ValueError, match="Input must be a list of integers."):
        BinarySearchTree.list_to_tree(10)

def test_list_to_tree_non_integer_elements():
    """
    Tests that passing a list containing non-integer elements raises a ValueError.
    """
    with pytest.raises(ValueError, match="All elements in the list must be integers."):
        BinarySearchTree.list_to_tree([10, "5", 15])

def test_list_to_tree_empty_list():
    """
    Tests creating a BST from an empty list.
    Ensures the root remains None.
    """
    bst = BinarySearchTree.list_to_tree([])
    assert bst.root is None, "Expected root to be None."

def test_list_to_tree_single_element():
    """
    Tests creating a BST from a list containing a single element.
    """
    bst = BinarySearchTree.list_to_tree([10])
    assert bst.root.key == 10, "Expected root key to be 10."

def test_list_to_tree_negative_numbers():
    """
    Tests creating a BST from a list of negative numbers.
    Ensures proper BST structure.
    """
    elements = [-10, -5, -15, -12, -20]
    bst = BinarySearchTree.list_to_tree(elements)
    assert bst.root.key == -10, "Expected root key to be -10."
    assert bst.root.left.key == -15, "Expected left child to be -15."
    assert bst.root.right.key == -5, "Expected right child to be -5."
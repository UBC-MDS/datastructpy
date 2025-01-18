import pytest
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

# Fixture to create a Binary Search Tree (BST) with predefined values
@pytest.mark.parametrize("elements, expected_root, expected_left, expected_right", [
    ([10, 5, 15, 12, 20], 10, 5, 15),  
    ([30, 20, 40, 35, 50], 30, 20, 40),  
])

# Test Case 1: Valid Input (Standard Case)
def test_list_to_tree_valid_input(elements, expected_root, expected_left, expected_right):
    """
    Test case to check if a Binary Search Tree (BST) is correctly created 
    from a list of elements.
    """
    bst = BinarySearchTree.list_to_tree(elements)

    # Test the root node and its immediate children
    assert bst.root.key == expected_root, f"Expected root key to be {expected_root}, but got {bst.root.key}"
    assert bst.root.left.key == expected_left, f"Expected left child to be {expected_left}, but got {bst.root.left.key}"
    assert bst.root.right.key == expected_right, f"Expected right child to be {expected_right}, but got {bst.root.right.key}"

    print("Test passed: Valid input")

#Test Case 2: Input is Not a List
def test_list_to_tree_not_a_list():
    try:
        bst = BinarySearchTree.list_to_tree(10)  
    except ValueError as e:
        assert str(e) == "Input must be a list of integers.", f"Expected error message, but got {e}"

    print("Test passed: Input is not a list")

#Test Case 3: List Contains Non-Integer Elements
def test_list_to_tree_non_integer_elements():
    try:
        bst = BinarySearchTree.list_to_tree([10, "5", 15]) 
    except ValueError as e:
        assert str(e) == "All elements in the list must be integers.", f"Expected error message, but got {e}"

    print("Test passed: List contains non-integer elements")


#Test Case 4: Empty List
def test_list_to_tree_empty_list():
    elements = []
    bst = BinarySearchTree.list_to_tree(elements)
    assert bst.root is None, f"Expected root to be None, but got {bst.root}"

    print("Test passed: Empty list")



#Test Case 5: List with One Element
def test_list_to_tree_single_element():
    elements = [10]
    bst = BinarySearchTree.list_to_tree(elements)
    assert bst.root.key == 10, f"Expected root key to be 10, but got {bst.root.key}"

    print("Test passed: Single element list")

#Test Case 6: List with Negative Numbers
def test_list_to_tree_negative_numbers():
    elements = [-10, -5, -15, -12, -20]
    bst = BinarySearchTree.list_to_tree(elements)
    assert bst.root.key == -10, f"Expected root key to be -10, but got {bst.root.key}"
    assert bst.root.left.key == -15, f"Expected left child to be -15, but got {bst.root.left.key}"
    assert bst.root.right.key == -5, f"Expected right child to be -5, but got {bst.root.right.key}"

    print("Test passed: List with negative numbers")


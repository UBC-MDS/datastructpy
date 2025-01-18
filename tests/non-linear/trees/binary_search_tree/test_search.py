import pytest
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

@pytest.fixture
def bst():
    r"""
    Fixture to create a Binary Search Tree (BST) with predefined values.

    The tree structure:
             10
            /  \
           5   15
          / \   / \
         3   7 13 18
    """
    elements = [10, 5, 15, 3, 7, 13, 18]
    return BinarySearchTree.list_to_tree(elements)

@pytest.mark.parametrize("key, expected", [
    (10, True),  # Root node
    (5, True),   # Left child of root
    (15, True),  # Right child of root
    (3, True),   # Left child of 5
    (7, True),   # Right child of 5
    (13, True),  # Left child of 15
    (18, True),  # Right child of 15
    (20, False), # Not in tree
    (-1, False), # Not in tree
])
def test_search_dfs(bst, key, expected):
    """
    Tests depth-first search (DFS) in BST.
    Ensures DFS correctly identifies if a key exists in the tree.
    """
    result = bst.search(key, algorithm='dfs')
    assert (result is not None) == expected

@pytest.mark.parametrize("key, expected", [
    (10, True),  # Root node
    (5, True),   # Left child of root
    (15, True),  # Right child of root
    (3, True),   # Left child of 5
    (7, True),   # Right child of 5
    (13, True),  # Left child of 15
    (18, True),  # Right child of 15
    (20, False), # Not in tree
    (-1, False), # Not in tree
])
def test_search_bfs(bst, key, expected):
    """
    Tests breadth-first search (BFS) in BST.
    Ensures BFS correctly identifies if a key exists in the tree.
    """
    result = bst.search(key, algorithm='bfs')
    assert (result is not None) == expected

def test_search_default_algorithm(bst):
    """
    Ensures that search() defaults to DFS when no algorithm is specified.
    """
    assert bst.search(7) is not None  # Should be found using DFS
    assert bst.search(20) is None     # Should not be found

def test_search_empty_tree():
    """
    Tests searching in an empty BST.
    The search should return None for any key.
    """
    empty_bst = BinarySearchTree()
    assert empty_bst.search(10) is None  # Should return None

def test_search_invalid_algorithm(bst):
    """
    Tests if search() handles invalid algorithm names properly.
    """
    with pytest.raises(ValueError):
        bst.search(10, algorithm='invalid_algorithm')
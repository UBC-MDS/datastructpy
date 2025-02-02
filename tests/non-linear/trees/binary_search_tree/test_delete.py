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
    Deleting a key from an empty BST should return False.
    """
    bst = BinarySearchTree()
    assert not bst.delete(10), "Deleting from an empty tree should return False."

def test_delete_leaf_node(bst):
    """
    Tests the deletion of a leaf node (node with no children).
    """
    assert bst.delete(5), "Leaf node 5 should be successfully deleted."
    assert bst.search(5) is None, "Leaf node 5 should no longer be in the tree."

def test_delete_non_existent_key(bst):
    """
    Tests deleting a key that does not exist in the BST.
    Should return False without modifying the tree.
    """
    assert not bst.delete(100), "Deleting a non-existent key should return False."

def test_delete_non_integer(bst):
    """
    Tests deleting a key that isn't an integer (string).
    Should raise a TypeError.
    """
    with pytest.raises(TypeError):
        bst.delete("100")

def test_delete_none_key(bst):
    """
    Tests deleting a None key.
    Should raise a TypeError.
    """
    with pytest.raises(TypeError):
        bst.delete(None)

def test_delete_none_node(bst):
    """
    Tests deleting a key that does not exist in the BST.
    Should return False without modifying the tree.
    """
    bst = BinarySearchTree()
    assert not bst.delete(100), "Deleting a non-existent key should return False."        

def test_delete_node_with_only_left_child():
    """
    Tests deleting a node that has only a left child.
    Ensures it reaches the `elif node.right is None: return node.left` condition.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)  # Left child only
    assert bst.delete(10), "Node 10 should be successfully deleted."
    assert bst.root.key == 5, "Node 5 should replace node 10."

def test_delete_traverse_right_subtree(bst):
    """
    Tests the deletion of a node located in the right subtree.
    """
    assert bst.delete(30), "Node 30 should be successfully deleted."
    assert bst.search(30) is None, "Node 30 should no longer be in the tree."
    assert bst.root.right.key == 35, "Node 35 should replace node 30 in the right subtree."

def test_delete_node_with_one_child(bst):
    """
    Tests the deletion of a node with only one child.
    The child node should replace the deleted node.
    """
    assert bst.delete(10), "Node 10 should be successfully deleted."
    assert bst.search(10) is None, "Node 10 should no longer be in the tree."
    assert bst.root.left.key == 15, "Node 15 should replace node 10."

def test_delete_node_with_two_children(bst):
    """
    Tests the deletion of a node that has two children.
    The node should be replaced by its in-order successor.
    """
    assert bst.delete(20), "Node 20 should be successfully deleted."
    assert bst.search(20) is None, "Node 20 should no longer be in the tree."
    assert bst.root.key == 25, "Root should now be replaced by in-order successor 25."

def test_delete_root_node():
    """
    Tests the deletion of the root node.
    The tree should correctly handle deleting the root.
    """
    bst = BinarySearchTree()
    bst.insert(10)
    assert bst.delete(10), "Root node 10 should be successfully deleted."
    assert bst.search(10) is None, "Root node 10 should no longer be in the tree."

def test_delete_complex_tree(bst):
    """
    Tests the deletion of a node in a complex tree structure.
    Ensures the BST maintains correct structure after deletion.
    """
    assert bst.delete(20), "Root 20 should be successfully deleted."
    assert bst.search(20) is None, "Root 20 should no longer be in the tree."
    assert bst.root.key == 25, "Root should now be replaced by in-order successor 25."
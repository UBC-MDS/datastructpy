from datastructpy.node import Node

def depth_first_search(root, key):
    """
    Performs a depth-first search (DFS) on a binary search tree.

    Parameters:
    ----------
    root (Node): The root of the BST.
    key (int): The value to search for.

    Returns:
    ----------
    Node or None: The node containing the key, or None if not found.
    """
    if not root:
        return None
    
    if root.key == key:
        return root  # Found the key

    # Search left subtree
    left_result = depth_first_search(root.left, key)
    if left_result:
        return left_result

    # Search right subtree
    return depth_first_search(root.right, key)
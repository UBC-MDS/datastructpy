from collections import deque
from datastructpy.node import Node

def breadth_first_search(root, key):
    """
    Performs a breadth-first search (BFS) on a binary search tree.
    
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

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.key == key:
            return node  # Found the key

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return None  # Key not found
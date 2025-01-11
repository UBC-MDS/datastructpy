class Node:
    """
    A class representing a node in a binary search tree (BST).

    Attributes
    ----------
    key : int
        The value stored in the node.
    left : Node, optional
        The left child node (default is None).
    right : Node, optional
        The right child node (default is None).
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    A class representing a binary search tree (BST).

    Methods
    -------
    insert(key)
        Inserts a key into the BST.
    delete(key)
        Deletes a key from the BST.
    search(key)
        Searches for a key in the BST.
    """

    def __init__(self):
        """
        Initializes an empty binary search tree.

        Attributes
        ----------
        root : Node, optional
            The root node of the binary search tree (default is None).
        """
        self.root = None

    def insert(self, key):
        """
        Inserts a new key into the binary search tree.

        Parameters
        ----------
        key : int
            The value to be inserted.
        """
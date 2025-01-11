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
        Inserts a key into the binary search tree.

        This function inserts a new value into the tree, maintaining the
        properties of a BST:
        - Values smaller than the current node's key go to the left subtree.
        - Values larger than the current node's key go to the right subtree.

        Parameters
        ----------
        key : int
            The value to insert into the BST.

        Examples
        --------
        # Creating a Binary Search Tree and inserting values
        bst = BinarySearchTree()
        bst.insert(10)  # Insert root
        bst.insert(5)   # Insert left child
        bst.insert(15)  # Insert right child
        bst.insert(12)  # Insert a node in the right subtree
        print(bst.root.left.key)  # Output: 5
        print(bst.root.right.key) # Output: 15
        """

    def delete(self, key):
        """Delete a value from the BST.

        This method removes a node with the specified value from the tree while maintaining the properties of a BST. 
        If the node to be deleted has two children, it replaces the node's value with its in-order successor 
        (the smallest value in the right subtree) and deletes the successor.

        Parameters
        ----------
        value : int or float
            The value to delete from the binary search tree.

        Examples
        --------
        # Creating a BST and deleting a node
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(12)

        bst.delete(10)  # Delete the root
        print(bst.root.value)  # Output: 12 (in-order successor)

        bst.delete(5)  # Delete a leaf node
        print(bst.root.left)  # Output: None
        """


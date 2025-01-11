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
    
    @staticmethod
    def list_to_tree(elements):
        """
        Constructs a Binary Search Tree (BST) from a list of elements.

        This function takes a list of numerical values and inserts them into a BST
        in the order they appear in the list. Duplicate values are ignored 
        to maintain the properties of a BST.

        Parameters
        ----------
        elements : list of int
            A list of integers to be inserted into the BST.

        Returns
        -------
        BinarySearchTree
            A BinarySearchTree object containing all the elements from the input list.

        Raises
        ------
        ValueError
            If the input is not a list or contains non-integer elements.

        Examples
        --------
        # Creating a BST from a list of values
        elements = [10, 5, 15, 12, 20]
        bst = BinarySearchTree.list_to_tree(elements)
        print(bst.root.key)       # Output: 10 (root node)
        print(bst.root.left.key)  # Output: 5 (left child of root)
        print(bst.root.right.key) # Output: 15 (right child of root)
        """
    @staticmethod
    def searchBST(root, value):
        """
    Search for a value in the Binary Search Tree (BST).

    This function recursively searches the tree to find the node containing the specified value.
    It compares the value to the root node's value and traverses left or right based on the comparison.
    If the value is found, the function returns True; otherwise, it returns False.

    Parameters
    ----------
    root : BinarySearchTree
        The root of the tree or subtree to search. Can be None if the tree is empty.
    value : int
        The value to search for in the tree.

    Returns
    -------
    bool
        - True if the value is found in the tree.
        - False if the value is not found or the tree is empty.

    Examples
    --------
    # Creating a Binary Search Tree
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(15)

    # Searching for values in the tree
    print(searchBST(bst, 5))  # Output: True
    print(searchBST(bst, 20)) # Output: False
    """

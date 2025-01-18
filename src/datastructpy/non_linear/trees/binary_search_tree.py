from datastructpy.node import Node


class BinarySearchTree:
    """
    A class representing a binary search tree (BST).

    Methods
    -------
    insert(key)
        Inserts a key into the BST.
    search(key)
        Searches for a key in the BST.
    delete(key)
        Deletes a key from the BST.
    list_to_tree(elements)
        Constructs a BST from a list of elements.
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
        if key is None:
            raise TypeError("None values are not allowed in the BST.")
        if not isinstance(key, int):
            raise TypeError("Only integers are allowed in the BST.")
        
        if self.root is None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if key < current.key:
                    # Go to the left subtree
                    if current.left is None:
                        current.left = Node(key)
                        break
                    else:
                        current = current.left
                elif key > current.key:
                    # Go to the right subtree
                    if current.right is None:
                        current.right = Node(key)
                        break
                    else:
                        current = current.right
                else:
                    # The key is already in the BST (no duplicates allowed)
                    break
 
    def search(self, key):
        """
        Checks if a value exists in the Binary Search Tree (BST).

        This method traverses the BST to determine if a node with the specified key exists.
        It starts from the root and:
        - Returns True if a node with the given key is found.
        - Returns False if the key is not present in the tree.

        Parameters
        ----------
        key : int
            The value to search for in the tree.

        Returns
        -------
        bool
            - True if a node with the specified key exists in the tree.
            - False if the key does not exist or the tree is empty.

        Examples
        --------
        # Creating a Binary Search Tree
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        # Searching for values in the tree
        print(bst.search(5))  # Output: True (5 exists in the tree)
        print(bst.search(20)) # Output: False (20 does not exist in the tree)
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

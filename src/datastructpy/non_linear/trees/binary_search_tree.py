from datastructpy.node import Node

class BinarySearchTree:
    """
    A class representing a Binary Search Tree (BST).

    Methods
    -------
    insert(key)
        Inserts a key into the BST while maintaining the BST properties.
    search(key, algorithm='dfs')
        Searches for a key in the BST using the specified search algorithm ('dfs' or 'bfs').
    delete(key)
        Deletes a key from the BST while preserving the BST structure.
    list_to_tree(elements)
        Constructs a BST from a list of integers.
    """

    def __init__(self):
        """
        Initializes an empty Binary Search Tree (BST).

        Attributes
        ----------
        root : Node, optional
            The root node of the BST (default is None).
        """
        self.root = None

    def insert(self, key):
        """
        Inserts a key into the Binary Search Tree (BST) while maintaining its properties.

        - Values smaller than the current node's key go to the left subtree.
        - Values larger than the current node's key go to the right subtree.
        - Duplicate values are not allowed.

        Parameters
        ----------
        key : int
            The value to insert into the BST.

        Raises
        ------
        TypeError
            If the key is not an integer or is None.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.root.left.key
        5
        >>> bst.root.right.key
        15
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
                    if current.left is None:
                        current.left = Node(key)
                        break
                    current = current.left
                elif key > current.key:
                    if current.right is None:
                        current.right = Node(key)
                        break
                    current = current.right
                else:
                    break  # Duplicate keys are ignored

    def search(self, key):
        """
        Searches for a key in the Binary Search Tree (BST).

        Parameters
        ----------
        key : int
            The value to search for in the BST.

        Returns
        -------
        Node or None
            - The Node object containing the specified key if found.
            - None if the key does not exist or the tree is empty.

        Raises
        ------
        TypeError
            If the key is not an integer or is None.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.search(5).key
        5
        >>> bst.search(20) is None
        True
        """
        if key is None:
            raise TypeError("None values are not allowed in the BST.")
        if not isinstance(key, int):
            raise TypeError("Only integers are allowed in the BST.")

        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, key):
        """
        Deletes a key from the Binary Search Tree (BST) while preserving its structure.

        - If the node has no children, it is simply removed.
        - If the node has one child, it is replaced by its child.
        - If the node has two children, it is replaced by the in-order successor (smallest node in the right subtree).

        Parameters
        ----------
        key : int
            The value to delete from the BST.

        Returns
        -------
        bool
            - True if the key was found and deleted.
            - False if the key was not found.

        Raises
        ------
        TypeError
            If the key is not an integer or is None.

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.delete(10)
        True
        >>> bst.delete(20)
        False
        """
        if key is None:
            raise TypeError("None values are not allowed in the BST.")
        if not isinstance(key, int):
            raise TypeError("Only integers are allowed in the BST.")

        def _delete(node, key):
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                min_larger_node = node.right
                while min_larger_node.left is not None:
                    min_larger_node = min_larger_node.left
                node.key = min_larger_node.key
                node.right = _delete(node.right, min_larger_node.key)
            return node

        if self.search(key) is None:
            return False
        self.root = _delete(self.root, key)
        return True

    @staticmethod
    def list_to_tree(elements):
        """
        Constructs a Binary Search Tree (BST) from a list of integers.

        Parameters
        ----------
        elements : list of int
            A list of integers to be inserted into the BST.

        Returns
        -------
        BinarySearchTree
            A BinarySearchTree object containing all elements from the input list.

        Raises
        ------
        ValueError
            If the input is not a list or contains non-integer elements.

        Examples
        --------
        >>> elements = [10, 5, 15, 12, 20]
        >>> bst = BinarySearchTree.list_to_tree(elements)
        >>> bst.root.key
        10
        >>> bst.root.left.key
        5
        >>> bst.root.right.key
        15
        """
        if not isinstance(elements, list):
            raise ValueError("Input must be a list of integers.")
        bst = BinarySearchTree()
        for element in elements:
            if not isinstance(element, int):
                raise ValueError("All elements in the list must be integers.")
            bst.insert(element)
        return bst

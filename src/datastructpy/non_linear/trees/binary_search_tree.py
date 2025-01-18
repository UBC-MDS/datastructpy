from datastructpy.node import Node
from datastructpy.non_linear.trees.breadth_first_search import breadth_first_search
from datastructpy.non_linear.trees.depth_first_search import depth_first_search

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

    def search(self, key, algorithm='dfs'):
        """
        Searches for a key in the Binary Search Tree (BST) using the specified algorithm.

        - DFS (default): Explores the deepest nodes before backtracking.
        - BFS: Searches level by level, ensuring the shortest path is checked first.

        Parameters
        ----------
        key : int
            The value to search for in the BST.
        algorithm : str, optional
            The search algorithm to use ('dfs' for Depth-First Search or 'bfs' for Breadth-First Search).
            Defaults to 'dfs'.

        Returns
        -------
        Node or None
            - The Node object containing the specified key if found.
            - None if the key does not exist or the tree is empty.

        Raises
        ------
        ValueError
            If an invalid algorithm is provided.

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
        if algorithm == 'bfs':
            return breadth_first_search(self.root, key)
        elif algorithm == 'dfs':
            return depth_first_search(self.root, key)
        else:
            raise ValueError(f"Invalid search algorithm: {algorithm}. Use 'dfs' or 'bfs'.")

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

        Examples
        --------
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.delete(10)
        >>> bst.root.key
        15
        """
        def _delete(node, key):
            if node is None:
                return None
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

        self.root = _delete(self.root, key)

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

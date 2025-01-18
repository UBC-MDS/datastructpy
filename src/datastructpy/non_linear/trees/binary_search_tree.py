from datastructpy.node import Node
from datastructpy.non_linear.trees.breadth_first_search import breadth_first_search
from datastructpy.non_linear.trees.depth_first_search import depth_first_search

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
                    
    def search(self, key, algorithm='dfs'):
        """
        Searches for a key in the Binary Search Tree (BST) using the specified algorithm.

        This method allows searching for a key in the BST using either 
        depth-first search (DFS) or breadth-first search (BFS).

        - DFS (default)**: Searches by exploring as deep as possible before backtracking.
        - BFS: Searches level by level, ensuring the shortest path to a node is checked first.

        Parameters
        ----------
        key : int
            The value to search for in the tree.
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
        # Creating a Binary Search Tree
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        # Searching for values in the tree
        result = bst.search(5)
        if result:
            print(result.key)  # Output: 5

        print(bst.search(20)) # Output: None (20 does not exist in the tree)
        """
        if algorithm == 'bfs':
            return breadth_first_search(self.root, key)
        elif algorithm == 'dfs':
            return depth_first_search(self.root, key)
        else:
            raise ValueError(f"Invalid search algorithm: {algorithm}. Use 'dfs' or 'bfs'.")

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
        def _delete(node, key):
            # Base case
            if node is None:
                return None
            
            # Check if key that wants to be deleted is smaller than current's,
            # Go to the left subtree
            if key < node.key:
                node.left = _delete(node.left, key)
            # Check if key that wants to be deleted is larger than current's,
            # Go to the right subtree
            elif key > node.key:
                node.right = _delete(node.right, key)
            # Key is found
            else:

                # Check if we have one or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                # If we have 2 children
                # Find the smallest one in the right subtree to replace the current node
                min_larger_node = node.right
                while min_larger_node.left is not None:
                    min_larger_node = min_larger_node.left
    
                # Replace current node with the smallest node's key
                node.key = min_larger_node.key

                # Delete the right node that contained the smallest key from the right subtree
                node.right = _delete(node.right, min_larger_node.key)

            # Return the updated node
            return node
            
        # To make sure the deletion process starts from the root
        self.root = _delete(self.root, key)
    
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

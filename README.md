# datastructpy

`datastructpy` is a Python package designed to provide customizable and practical implementations of essential data structures, such as Binary Search Trees (BST). It is tailored to help users prepare for technical interviews, coding challenges, and educational projects by offering intuitive and efficient solutions. The package stands out by emphasizing simplicity and clarity while maintaining detailed documentation and modular implementations suited for both learning and practical use. Unlike visualization-heavy libraries, the package focuses on providing a hands-on, customizable experience for working with binary trees and other data structures. If you require a structured, minimalistic approach without additional dependencies or overhead, `datastructpy` serves as a valuable alternative!

## Data Structures Included:

- ### `Binary Search Tree`
    A Binary Search Tree (BST) is a data structure that organizes data hierarchically, allowing for efficient insertion, deletion, and lookup operations. Each node in the tree contains a key, and the tree is structured such that:
    - Keys in the left subtree of a node are smaller than the node’s key.
    - Keys in the right subtree of a node are larger than the node’s key.
    - Duplicate keys are not allowed.

    **Methods**
    - **`insert(key)`**:
        - Inserts a specified key into the Binary Search Tree (BST) while maintaining BST properties.
        - If the tree is empty, it creates a new root node.
        - If the key is smaller than the current node’s key, it is inserted into the left subtree; if larger, into the right subtree.
        - Duplicate keys are ignored.

    - **`search(key, algorithm='dfs')`**:
        - Searches for a specified key in the BST.
        - Supports two search algorithms:
          - **Depth-First Search (DFS) (default):** Explores as deep as possible before backtracking.
          - **Breadth-First Search (BFS):** Searches level by level, ensuring the shortest path to a node is checked first.
        - Returns the node containing the key if found, otherwise `None`.

    - **`delete(key)`**:
        - Deletes a specified key from the BST while maintaining BST properties.
        - If the node has:
          - **No children** → It is removed.
          - **One child** → The child replaces the deleted node.
          - **Two children** → The node is replaced by its in-order successor (the smallest value in the right subtree), and the successor is then deleted.

    - **`list_to_tree(elements)`**:
        - Constructs a Binary Search Tree (BST) from a given list of elements.
        - Sequentially inserts each element into the BST, ensuring the tree maintains BST properties.
        - **Duplicate values are ignored** to preserve the BST structure.
        - Returns a `BinarySearchTree` object with the provided elements organized as a valid BST.

## datastructpy in Python Ecosystem
`datastructpy` complements Python’s standard library by providing customizable implementations of essential data structures for learning and interview preparation. While modules like collections (e.g., deque) and heapq focus on optimized, ready-to-use structures, datastructpy emphasizes clarity and adaptability, making it ideal for understanding core concepts. Unlike specialized libraries like [pyrsistent](https://pypi.org/project/pyrsistent/) or [sortedcontainers](https://pypi.org/project/sortedcontainers/), `datastructpy` bridges the gap between practical functionality and educational needs, carving out a unique space in the Python ecosystem.

## Installation

```bash
$ pip install datastructpy
```

## Usage

### Example usage:

```python
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

# Create a Binary Search Tree from a list of elements
elements = [10, 5, 15, 8]
bst = BinarySearchTree.list_to_tree(elements)

# Check the structure of the tree
print("Tree Structure After Creation:")
print(bst.root.key)             # Output: 10
print(bst.root.left.key)        # Output: 5
print(bst.root.right.key)       # Output: 15
print(bst.root.left.right.key)  # Output: 8

# Insert new nodes into the BST
print("Inserting New Elements:")
bst.insert(12)  # Insert into right subtree of 10
bst.insert(2)   # Insert into left subtree of 5
print(bst.root.right.left.key)  # Output: 12 (left child of 15)
print(bst.root.left.left.key)   # Output: 2 (left child of 5)

# Search for values in the BST
print("Searching for Keys:")
print(bst.search(8) is not None)   # Output: True (8 exists in the tree)
print(bst.search(20) is None)      # Output: True (20 does not exist in the tree)

# Delete a node
print("Deleting Nodes:")
bst.delete(5)  # Delete the left child of the root
if bst.root.left:
    print(bst.root.left.key)    # Output: 8 (5 replaced by its in-order successor)
else:
    print(bst.root.left)        # Output: None (if no successor is present)

bst.delete(10)  # Delete the root
print(bst.root.key)             # Output: 15 (new root after deletion)

# Final structure of the tree
print("Final Tree Structure:")
print(bst.root.key)             # Output: 15
print(bst.root.left.key)        # Output: 8
print(bst.root.right.left.key)  # Output: 12
```

## Contributing

Interested in contributing? Check out the [contributing](https://github.com/UBC-MDS/datastructpy/blob/main/CONTRIBUTING.md) guidelines. Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/datastructpy/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`datastructpy` was created by Albert Halim, Azin Piran, Javier Martinez, Jessica Kuo. It is licensed under the terms of the MIT license.

## Credits

`datastructpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors

Albert Halim, Azin Piran, Javier Martinez, Jessica Kuo

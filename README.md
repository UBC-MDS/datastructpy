# datastructpy

datastructpy is a Python package designed to provide customizable and practical implementations of essential data structures. It is tailored to help users prepare for technical interviews and coding challenges by offering intuitive, modular, and efficient solutions. The library emphasizes clarity and functionality, making it a valuable resource for learning, practicing, and mastering data structure concepts. Whether you’re solving algorithmic problems or building foundational coding skills, datastructpy is crafted to support your success.

## Data Structures Included:

- ### `Binary Search Tree`
    A Binary Search Tree (BST) is a data structure that organizes data hierarchically, allowing for efficient insertion, deletion, and lookup operations. Each node in the tree contains a key, and the tree is structured such that:
    - Keys in the left subtree of a node are smaller than the node’s key.
    - Keys in the right subtree of a node are larger than the node’s key.
    - Duplicate keys are not allowed.

    **Methods**
    - **`insert(root, key)`**:
        - This method inserts a specified key into a Binary Search Tree (BST) by recursively finding the correct position while maintaining BST properties, creating a new root node if the tree is empty, inserting into the left subtree if the key is smaller, or the right subtree if larger.
    - **`delete(root, key)`**:
        - This method deletes a specified key from a Binary Search Tree (BST). If the key is found, it removes the node while maintaining BST properties. For nodes with two children, it replaces the node with its in-order successor (smallest value in the right subtree) and then deletes the successor node. If the node has one child or no children, it is removed, and its child (if any) takes its place.
    - **`list_to_tree(elements)`**:
        - This static method constructs a Binary Search Tree (BST) from a given list of elements. It sequentially inserts each element into the BST, ensuring the tree maintains its BST properties. The method is accessed directly via the BinarySearchTree class and returns a BinarySearchTree object with the provided elements organized in a valid BST structure.

## datastructpy in Python Ecosystem
datastructpy complements Python’s standard library by providing customizable implementations of essential data structures for learning and interview preparation. While modules like collections (e.g., deque) and heapq focus on optimized, ready-to-use structures, datastructpy emphasizes clarity and adaptability, making it ideal for understanding core concepts. Unlike specialized libraries like [pyrsistent](https://pypi.org/project/pyrsistent/) or [sortedcontainers](https://pypi.org/project/sortedcontainers/), datastructpy bridges the gap between practical functionality and educational needs, carving out a unique space in the Python ecosystem.

## Installation

```bash
$ pip install datastructpy
```

## Usage

### Example usage:

```python
from datastructpy.binary_search_tree import BinarySearchTree

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
print(bst.root.right.left.key)  # Output: 12 (right subtree of 10, left child of 15)
print(bst.root.left.left.key)   # Output: 2 (left child of 5)

# Delete a node
print("Deleting Nodes:")
bst.delete(5)  # Delete the left child of the root
if bst.root.left:
    print(bst.root.left.key)    # Output: 8 (5 replaced by its in-order successor)
else:
    print(bst.root.left)        # Output: None (if successor is not present)

bst.delete(10)  # Delete the root
print(bst.root.key)             # Output: 15 (new root after deletion)

# Final structure of the tree
print("Final Tree Structure:")
print(bst.root.key)             # Output: 15
print(bst.root.left.key)        # Output: 8
print(bst.root.right.left.key)  # Output: 12
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`datastructpy` was created by group9_ubc_mds_2025. It is licensed under the terms of the MIT license.

## Credits

`datastructpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors

- Javier Martinez
- Azin Piran
- Jessica Kuo
- Albert Halim
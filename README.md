# datastructpy

Data Structures for Python

## Functions Included:

- **`insertBST(root, key)`**:
    - This function inserts a specified key into a Binary Search Tree (BST) by recursively finding the correct position while maintaining BST properties, creating a new root node if the tree is empty, inserting into the left subtree if the key is smaller, or the right subtree if larger.
    

## Installation

```bash
$ pip install datastructpy
```

## Usage

### insertBST(root, key):
This function inserts a specified key into a Binary Search Tree (BST). It traverses the tree recursively to find the correct position where the key should be placed, ensuring that the BST properties are maintained. If the root is None, a new node is created as the root. If the key is smaller than the current node's key, it is inserted in the left subtree. If the key is larger than the current node's key, it is inserted in the right subtree.

### Example usage:

```python
from datastructpy.binary_search_tree import Node, BinarySearchTree

# Create a Binary Search Tree
bst = BinarySearchTree()
bst.insert(10)  # Insert root
bst.insert(5)   # Insert left child
bst.insert(15)  # Insert right child
bst.insert(8)   # Insert into left subtree

# Check the structure of the tree
print(bst.root.key)             # Output: 10
print(bst.root.left.key)        # Output: 5
print(bst.root.right.key)       # Output: 15
print(bst.root.left.right.key)  # Output: 8
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`datastructpy` was created by group9_ubc_mds_2025. It is licensed under the terms of the MIT license.

## Credits

`datastructpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

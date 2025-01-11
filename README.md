# datastructpy

Data Structures for Python

## Functions Included:

- **`insert(root, key)`**:
    - This function inserts a specified key into a Binary Search Tree (BST) by recursively finding the correct position while maintaining BST properties, creating a new root node if the tree is empty, inserting into the left subtree if the key is smaller, or the right subtree if larger.
- **`delete(root, key)`**:
    - This function deletes a specified key from a Binary Search Tree (BST). If the key is found, it removes the node while maintaining BST properties. For nodes with two children, it replaces the node with its in-order successor (smallest value in the right subtree) and then deletes the successor node. If the node has one child or no children, it is removed, and its child (if any) takes its place.
    

## Installation

```bash
$ pip install datastructpy
```

## Usage

### insert(root, key):

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

### delete(root, key):
This function deletes a specified key from a Binary Search Tree (BST). If the key matches a node in the tree, the function removes the node while ensuring that BST properties are maintained. For nodes with two children, it finds the in-order successor, replaces the node's key with the successor's key, and deletes the successor node. If the node has only one child or no children, the node is removed, and its child (if present) takes its place.

### Example usage:

```python
from datastructpy.binary_search_tree import Node, BinarySearchTree

# Using the tree created above

# Delete a node
bst.delete(5)  # Delete left child
print(bst.root.left) # Output: None (since 5 is deleted)

bst.delete(10)  # Delete root
print(bst.root.key) # Output: 15 (new root after deletion)
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
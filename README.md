# datastructpy

[![Documentation Status](https://readthedocs.org/projects/datastructpy/badge/?version=latest)](https://datastructpy.readthedocs.io/en/latest/?badge=latest)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![codecov](https://codecov.io/gh/UBC-MDS/datastructpy/graph/badge.svg?token=BzhF7l45if)](https://codecov.io/gh/UBC-MDS/datastructpy)



`datastructpy` is a Python package designed to provide customizable and practical implementations of essential data structures, such as Binary Search Trees (BST). It is tailored to help users prepare for technical interviews, coding challenges, and educational projects by offering intuitive and efficient solutions. The package stands out by emphasizing simplicity and clarity while maintaining detailed documentation and modular implementations suited for both learning and practical use. Unlike visualization-heavy libraries, the package focuses on providing a hands-on, customizable experience for working with binary trees and other data structures. If you require a structured, minimalistic approach without additional dependencies or overhead, `datastructpy` serves as a valuable alternative!

## Data Structures Included:

- ### `Binary Search Tree`
    A Binary Search Tree (BST) is a data structure that organizes data hierarchically, allowing for efficient insertion, deletion, and lookup operations. Each node in the tree contains a key, and the tree is structured such that:
    - Keys in the left subtree of a node are smaller than the node’s key.
    - Keys in the right subtree of a node are larger than the node’s key.
    - Duplicate keys are not allowed.

    Time Complexity:
    Search, Insert, Delete:
    - Average Case: O(log n) => This occurs when the BST is balanced.
    - Worst Case: O(n) => This occurs when the BST is skewed.

    Space Complexity:
    - Space for the BST: O(n).
    - Recursive Operations: O(h), where h is the height of the tree.

    **Methods**
    - **`insert(key)`**:
        - Inserts a specified key into the Binary Search Tree (BST) while maintaining BST properties.
        - If the tree is empty, it creates a new root node.
        - If the key is smaller than the current node’s key, it is inserted into the left subtree; if larger, into the right subtree.
        - Duplicate keys are ignored.

    - **`search(key)`**:
        - Searches for a specified key in the BST.
        - The search follows the **Binary Search Tree (BST) property**:
        - If the key is smaller than the current node, search the left subtree.
        - If the key is larger, search the right subtree.
        - If the key matches, return the node.
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

## 🚀 Installation

You can install **datastructpy** using `pip`.

### Install via pip:

```bash
$ pip install datastructpy
```

## Usage

### Example Usage

```python
from datastructpy import BinarySearchTree

# Build a BST from a list of values.
bst = BinarySearchTree.list_to_tree([10, 5, 15, 8])

# After creation, the tree looks like:
#
#         10
#        /  \
#       5    15
#        \
#         8
#
print("Initial Tree:")
print("  Root:", bst.root.key)
print("  Left Child:", bst.root.left.key)
print("  Right Child:", bst.root.right.key)
print("  Right of Left Child:", bst.root.left.right.key)
```
```text
Initial Tree:
  Root: 10
  Left Child: 5
  Right Child: 15
  Right of Left Child: 8
```
```python
# Insert new elements.
bst.insert(12)  # Inserts into left subtree of 15.
bst.insert(2)   # Inserts into left subtree of 5.

# Now the tree is updated to:
#
#         10
#        /  \
#       5    15
#      / \   /
#     2   8 12
#
print("\nAfter Insertion:")
print("  New left of 5:", bst.root.left.left.key)
print("  New left of 15:", bst.root.right.left.key)
```
```text
After Insertion:
  New left of 5: 2
  New left of 15: 12
```
```python
# Search for keys.
print("\nSearch Results:")
print("  8 found:", bst.search(8) is not None)
print("  20 found:", bst.search(20) is not None)
```
```text
Search Results:
  8 found: True
  20 found: False
```
```python
# Delete node with key 5.
# The in-order successor of 5 (which is 8) replaces it.
bst.delete(5)
print("\nAfter Deleting 5:")
if bst.root.left:
    print("  New left child of 10:", bst.root.left.key)
else:
    print("  Left child is None")
# The tree now becomes:
#         10
#        /  \
#       8    15
#      /    /
#     2    12
```
```text
After Deleting 5:
  New left child of 10: 8
```
```python
# Delete the root (10). The in-order successor of 10 (which is 12) replaces it.
bst.delete(10)
print("\nAfter Deleting 10:")
print("  New Root:", bst.root.key)
```
```text
After Deleting 10:
  New Root: 12
```
```python
# Final structure.
print("\nFinal Tree Structure:")
print("  Root:", bst.root.key)
print("  Left Child:", bst.root.left.key)
if bst.root.right:
    print("  Right Child:", bst.root.right.key)
else:
    print("  Right Child: None")
# The final tree is:
#
#         12
#        /  \
#       8    15
#      /     
#     2   
```
```text
Final Tree Structure:
  Root: 12
  Left Child: 8
  Right Child: 15
```

## Running Tests

To run tests for the `datastructpy` package, follow these steps:


1. **Ensure dependencies are installed**:
    If you haven't set up the environment yet, install dependencies using Poetry:

    ```bash
    $ poetry install
    ```

2. **Run tests using pytest**:
    Execute the following command from the root of the project directory:

    ```bash
    $ poetry run pytest
    ```

    This will automatically discover and execute all test files in the `tests/` directory.

3. **Run a specific test file**:
    To test a specific module, specify the file path:

    ```bash
    $ poetry run pytest tests/non-linear/trees/binary_search_tree/test_list_to_tree.py
    ```

4. **Run tests with coverage** (optional):
    To measure test coverage, use:

    ```bash
    $ poetry run pytest --cov=src/datastructpy
    ```

For more advanced testing options and configurations, refer to the [pytest documentation](https://docs.pytest.org/en/stable/).

## Contributors

Albert Halim [@Albert0011](https://github.com/Albert0011), Azin Piran [@AzinPiran](https://github.com/AzinPiran), Javier Martinez [@javiermtzo99](https://github.com/javiermtzo99), Jessica Kuo [@kuo4230](https://github.com/kuo4230)

## Contributing

Interested in contributing? Check out the [contributing](https://github.com/UBC-MDS/datastructpy/blob/main/CONTRIBUTING.md) guidelines. Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/datastructpy/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`datastructpy` was created by Albert Halim, Azin Piran, Javier Martinez, Jessica Kuo. It is licensed under the terms of the [MIT license](https://github.com/UBC-MDS/datastructpy?tab=MIT-1-ov-file).

## Credits

`datastructpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

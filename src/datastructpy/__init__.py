# Read version from installed package
from importlib.metadata import version
__version__ = version("datastructpy")

# Use absolute imports
from datastructpy.node import Node
from datastructpy.non_linear.trees.binary_search_tree import BinarySearchTree

# Define the public API of the package
__all__ = [
    "__version__",
    "Node",
    "BinarySearchTree",
]
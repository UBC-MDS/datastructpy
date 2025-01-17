# read version from installed package
from importlib.metadata import version
__version__ = version("datastructpy")

# Import key submodules or classes for easy access
from .node import Node
from non_linear.trees.binary_search_trees import BinarySearchTree

# Define the public API of the package
__all__ = [
    "__version__",
    "Node",
    "BinarySearchTree",
]
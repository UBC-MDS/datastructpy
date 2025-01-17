import sys
import os

# Get the absolute path to the src directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))

# Add it to sys.path if not already included
if src_path not in sys.path:
    sys.path.insert(0, src_path)
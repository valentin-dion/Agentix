import glob
import os
import sys
from rich import print

def dynamic_import(directory_name):
    """
    Dynamically imports all Python files from the specified directory under the current working directory.
    """

    parent = os.path.dirname
    target_dir = parent(parent(os.path.abspath(__file__)))

    if target_dir not in sys.path:
        sys.path.append(target_dir)
    
    target_files = glob.glob(target_dir + f'/**/{directory_name}/**/*.py', recursive=True)
    

    
    for file_path in target_files:
        print(f"dynamic import of[orange i] `{file_path}`")
        # Extract module name from file path, excluding the directory part
        relative_path = os.path.relpath(file_path, target_dir)
        module_name = os.path.splitext(relative_path)[0].replace(os.sep, '.')
        
        # Import module
        if module_name not in sys.modules:
            __import__(module_name)


import importlib.util

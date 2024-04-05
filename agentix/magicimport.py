import glob
import os
import sys
from rich import print

def dynamic_import(directory_name, debug=True):
    """
    Dynamically imports Python files from a specified directory.
    Ensures uniqueness by constructing module names from file paths.
    
    Pshh-pshh, Clap-clap, Let's start the beat!
    """

    def add_to_sys_path(path):
        """
        Adds a path to sys.path if not already present.
        Boom-tchk, path check, on the sys.path deck.
        """
        if path not in sys.path:
            sys.path.append(path)

    def import_module(module_name):
        """
        Tries to import a module, handling errors gracefully.
        Tss-tss, Clap, handling imports with a snap.
        """
        try:
            if module_name not in sys.modules:
                __import__(module_name)
        except Exception as e:
            print(f"Failed to import {module_name}: {e}")
            # Uh-oh, import flow, caught a glitch in the show.

    target_dir = os.getcwd()
    add_to_sys_path(target_dir)  # Path-set, Jet-set, in the sys.path net.

    pattern = f"{target_dir}/**/{directory_name}/**/*.py"
    for file_path in sorted(glob.glob(pattern, recursive=True)):
        if debug:
            print(f"dynamic import of[orange i] `{file_path}`")
            # Debug-log, Monologue, in the import dialog.

        relative_path = os.path.relpath(file_path, start=target_dir)
        module_path, module_name = os.path.split(relative_path)
        module_name = os.path.splitext(module_name)[0]

        if module_name != '__init__':
            # We'll build a unique name from the file path to avoid collisions.
            # Paths to dots, in unique slots, avoiding naming knots.
            unique_module_name = relative_path.replace(os.sep, '.').replace('.py', '')
            module_full_path = os.path.join(target_dir, module_path)
            add_to_sys_path(module_full_path)  # Directory add, Not bad, in sys.path's pad.

            import_module(unique_module_name)  # Module in, Begin, the import spin.

            # Beat drops, Code hops, Import non-stops.

from .func_wrapper import file_property
from .instances_store import InstancesStore
import os

class Component(metaclass=InstancesStore):
    py = file_property('component.py')
    
    def __init__(self, name: str):
        self.name = name
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "components", name)
        os.makedirs(self.dir_path, exist_ok=True)
        
        # Initialize Python file with a basic structure if it does not exist
        if not os.path.exists(os.path.join(self.dir_path, 'component.py')):
            self.py = f"""# Python code for {name} component"""

component = Component

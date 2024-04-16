from .func_wrapper import file_property
from .instances_store import InstancesStore
import os

class Component(metaclass=InstancesStore):
    html = file_property('component.html')
    css = file_property('style.css')
    js = file_property('script.js')
    
    def __init__(self, name: str):
        self.name = name
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "components", name)
        os.makedirs(self.dir_path, exist_ok=True)

        # Initialize file properties with default content if needed
        self.html = f"""<div>Hello from {name} component</div>"""
        self.css = f"""/* Style for {name} component */"""
        self.js = f"""// JavaScript for {name} component"""

    def export(self):
        # Placeholder for export logic
        pass

component = Component

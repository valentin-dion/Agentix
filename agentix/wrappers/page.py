from .func_wrapper import file_property
from .instances_store import InstancesStore
import os

class Page(metaclass=InstancesStore):
    html = file_property('index.html')
    css = file_property('style.css')
    js = file_property('script.js')
    
    def __init__(self, name: str):
        self.name = name
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "pages", name)
        os.makedirs(self.dir_path, exist_ok=True)
        self._ensure_files_exist()
        
    def _ensure_files_exist(self):
        # Ensure that the HTML, CSS, and JS files exist.
        for prop in ['index.html', 'style.css', 'script.js']:
            file_path = os.path.join(self.dir_path, prop)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write('')  # Create an empty file

    @classmethod
    def factory(cls, name):
        if name not in cls:
            cls[name] = cls(name)
        return cls[name]
        
    @classmethod
    def register(cls, name):
        return cls.factory(name)

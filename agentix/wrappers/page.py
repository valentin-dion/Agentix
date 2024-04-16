from .func_wrapper import file_property
from .instances_store import InstancesStore
import os

class Page(metaclass=InstancesStore):
    py = file_property('_ploup.py')
    template = file_property('tpl.vue')
    css = file_property('css.vue')
    js = file_property('js.vue')
    
    def __init__(self, name: str):
        self.name = name
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "./pages", name)
        self.out_path = os.path.join(cwd, f"/front/pages/{name}.vue")
        
        os.makedirs(self.dir_path, exist_ok=True)        

        self.py = f"""from agentix import page
page('{name}')"""

        
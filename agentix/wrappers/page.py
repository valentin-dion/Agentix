from .func_wrapper import file_property
from .instances_store import InstancesStore
import os

class Page(metaclass=InstancesStore):
    py = file_property('_ploup.py')
    template = file_property('tpl.vue')
    css = file_property('css.vue')
    js = file_property('js.vue')
    prompt = file_property('prompt.conv')  # New property for .conv files
    user_stories = file_property('user_stories.md')  # New property for .md files
    test_cases = file_property('test_cases.md')  # New property for .md files
    tests = file_property('tests.py')  # New property for .py files
    mock = file_property('mock.py')  # New property for .py files
    vars = file_property('vars.py')  # New property for .py files
    
    def __getitem__(self, k):
        return getattr(self, k)
    
    def __init__(self, name: str):
        self.name = name
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "./pages", name)
        self.out_path = os.path.join(cwd, f"/front/pages/{name}.vue")
        
        os.makedirs(self.dir_path, exist_ok=True)        

        self.py = f"""from agentix import page
page('{name}')"""

    def export(self):
        ...
        
page = Page

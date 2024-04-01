import os
from enum import Enum

from .func_wrapper import FuncWrapper, file_property
from .instances_store import InstancesStore

# Assuming FuncWrapper and InstancesStore are defined elsewhere

class ImplState(Enum):
    NIL = 0
    PROPS = 1
    MOCKS = 2
    TEST_WRITTEN = 3
    SOLVED_MOCK = 4
    SOLVED_TREE = 5


class Func(FuncWrapper, metaclass=InstancesStore):
    
    code = file_property('code.py')
    
    def __init__(self, name: str, func: callable):
        super().__init__(name, func)
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "funcs", name)
        os.makedirs(self.dir_path, exist_ok=True)

 

func = Func.register
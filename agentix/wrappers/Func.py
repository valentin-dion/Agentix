import os
from enum import Enum

from .func_wrapper import FuncWrapper
from .instances_store import InstancesStore

# Assuming FuncWrapper and InstancesStore are defined elsewhere

class ImplState(Enum):
    NIL = 0
    PROPS = 1
    MOCKS = 2
    TEST_WRITTEN = 3
    SOLVED_MOCK = 4
    SOLVED_TREE = 5

def file_property(filename, read_transform=None, write_transform=None):
    def decorator(cls):
        def getter(self):
            file_path = os.path.join(self.dir_path, filename)
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    return read_transform(content) if read_transform else content
            except FileNotFoundError:
                return None

        def setter(self, value):
            file_path = os.path.join(self.dir_path, filename)
            value_to_write = write_transform(value) if write_transform else value
            with open(file_path, 'w') as file:
                file.write(value_to_write)

        setattr(cls, filename.split('.')[0], property(getter, setter))
        return cls
    return decorator

@file_property('impl_state.txt', lambda x: ImplState(int(x)), lambda x: str(x.value))
@file_property('short_desc.md')
@file_property('user_stories.md')
@file_property('test_cases.md')
@file_property('tests.py')
@file_property('doc.md')
@file_property('code.py')
@file_property('docstring.txt')
@file_property('prompt.txt')
class Func(FuncWrapper, metaclass=InstancesStore):
    def __init__(self, name: str, func: callable):
        super().__init__(name, func)
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "funcs", name)
        os.makedirs(self.dir_path, exist_ok=True)

    def change_impl_state(self, direction: str):
        # Assume this method is correctly implemented to handle state changes
        pass

    @property
    def parent(self):
        parent_func = self.parent_func or 'human'
        return 'human' if parent_func == 'human' else Func[parent_func]
    
 

func = Func.register
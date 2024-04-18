import os
from enum import Enum

from .func_wrapper import FuncWrapper, file_property
from .instances_store import InstancesStore


class Endpoint( metaclass=InstancesStore):
    
    code = file_property('code.py')
    docstring = file_property('docstring.md')
    user_stories = file_property('user_stories.md')
    test_cases = file_property('test_cases.md')
    tests = file_property('tests.py')
    
    def __init__(self, name: str):
        self.name = name
        cwd = os.getcwd()
        self.dir_path = os.path.join(cwd, "bricks/endpoints", name)
        os.makedirs(self.dir_path, exist_ok=True)
    
        
    @classmethod
    def factory(cls, name:str) -> 'Endpoint':
        if name not in cls:
            cls[name] = cls(name)
        return cls[name]
        
    @classmethod
    def register(cls, func):
        name = func.__name__
        cls.factory(name)._func = func
        
    @classmethod
    def bootstrap(cls, appRouter):
        for name, EP in cls.items():
            appRouter(f"/{name}", methods=['GET','POST'])(EP._func)
            
    route = bootstrap
            
            
    def _full_repr_md(self):
        return f"""# Endpoint {self.name}

## Docstring

{self.docstring}
 
## Code

```python
{self.code}
```

"""

    @classmethod
    def repr_all(cls):
        return '\n____\n'.join(EP._full_repr_md() for EP in cls.values())
    
endpoint=Endpoint.register
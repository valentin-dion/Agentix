from collections import defaultdict
from .func_wrapper import FuncWrapper
from .instances_store import DefaultInstanceStore

class Event( metaclass=DefaultInstanceStore):
    """
    ```python
    Event['stuffHappen'](stuff)
    
    @Event.on('stuffHappen')
    def handler(stuff:str)->None:
       ...
    ```
    
    """
    _handlers = defaultdict(list)
    
    @classmethod
    def on(cls, eventName):
        def _wrapper(func):
            cls._handlers[eventName].append(func)
            return func
        return _wrapper
    
    def _set_item(self,item:str):
        self.item = item
        
    def __call__(self, *whut):
        for handler in self._handlers[self.item]:
            handler(*whut)
        for handler in self._handlers[self.item]:
            ...        
    
    
    

Event['_default'] = Event()
    

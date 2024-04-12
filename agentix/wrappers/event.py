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
        """
        Decorator to register a function as an event handler for a specific event name.

        :param eventName: The name of the event to listen for.
        """
        def _wrapper(func):
            cls._handlers[eventName].append(func)
            return func
        return _wrapper
    
    def _set_item(self,item:str):
        """
        Internal method to set the current event name.

        :param item: The name of the event.
        """
        self.item = item
        
    def __call__(self, *whut):
        for handler in self._handlers[self.item]:
            handler(*whut)
        """
        Trigger all handlers for the current event name with provided arguments.

        :param whut: Arguments to pass to the event handlers.
        """
        if self.item in self._handlers:
            for handler in self._handlers[self.item]:
                handler(*whut)
        else:
            raise KeyError(f"No handlers found for event '{self.item}'.")
    
    
    

Event['_default'] = Event()
    

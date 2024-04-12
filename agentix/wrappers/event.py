from collections import defaultdict
import threading
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
        
    def __call__(self, *args):
        def run_handler(handler, args):
            handler(*args)

        for handler in self._handlers[self.item]:
            thread = threading.Thread(target=run_handler, args=(handler, args))
            thread.start()
            thread.join()
    
    

Event['_default'] = Event()
    

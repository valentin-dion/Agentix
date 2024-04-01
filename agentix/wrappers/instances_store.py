class InstancesStore(type):
    """
    A metaclass for storing and retrieving Agent/MW instances.
    """
    def __new__(metacls, name, bases, dct):
        # Create a new class with a unique instance store
        cls = super().__new__(metacls, name, bases, dct)
        cls._store = {}  # Instance store specific to each class
        return cls

    def __getitem__(cls, item: str) :
        if item in cls._store:
            return cls._store[item]
        
        raise KeyError(f"No {cls.__name__} with name '{item}' found.")

    def __setitem__(cls, key: str, value) -> None:
        if key in cls._store:
            raise KeyError(f"{cls.__name__} with name '{key}' already exists.")
        cls._store[key] = value

    def __contains__(cls, item: str) -> bool:
        return item in cls._store


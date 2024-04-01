import os

def file_property(filename):
    def getter(self):
        file_path = os.path.join(self.dir_path, filename)
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None

    def setter(self, value):
        file_path = os.path.join(self.dir_path, filename)
        with open(file_path, 'w') as file:
            file.write(value)

    return property(getter, setter)

class FileBackedProperties:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    short_desc = file_property('short_desc.md')
    user_stories = file_property('user_stories.md')
    test_cases = file_property('test_cases.md')
    
 

func = Func.register
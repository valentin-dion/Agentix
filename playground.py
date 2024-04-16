import re
from rich import print

def xml_parser(tag_name):
    def parse(xml_string):
        result = {}
        # Regex to find <tag ...>content</tag>, capturing attributes and content
        tag_pattern = f'<{tag_name}(.*?)>(.*?)</{tag_name}>'
        tags = re.findall(tag_pattern, xml_string, re.DOTALL)
        
        for attrs, content in tags:
            # Extract the name attribute and use it as the key in the result dictionary
            name_match = re.search(r'name="([^"]+)"', attrs)
            if name_match:
                name = name_match.group(1)
                # Create dictionary for this element
                attr_dict = {'content': content.strip()}
                # Extract other attributes
                other_attrs = re.finditer(r'(\w+)="([^"]+)"', attrs)
                for attr in other_attrs:
                    attr_dict[attr.group(1)] = attr.group(2)
                
                # Insert into result using name as the key
                result[name] = attr_dict
        return result
    return parse

# Usage example:
xml_string = '''blabla

<comp name="aa" foo="bar">
   content
</comp>

<comp name="bb" babaz="fri" toto="oui">foo_bar</comp>

lkejlakj'''

parser = xml_parser('comp')
print(parser(xml_string))

from agentix import tool 

@tool
def parser(opening_tag, ending_tag) -> callable:
    """
    Parses text enclosed between specified opening and ending tags.
    
    Args:
        opening_tag (str): The opening tag to look for.
        ending_tag (str): The ending tag to look for.
    
    Returns:
        callable: A function that takes a string and returns a list of parsed segments.
    """
    def parse(text:str):
        
        segments = text.split(opening_tag)
        results = []
        for segment in segments[1:]:
            end_idx = segment.find(ending_tag)
            if end_idx != -1:
                results.append(segment[:end_idx].strip())
        return results
    return parse

import re

@tool
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
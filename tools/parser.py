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

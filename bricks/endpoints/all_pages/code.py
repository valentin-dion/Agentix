from agentix import endpoint
@endpoint
def all_pages():
    from agentix import Page 
    
    return list(Page.keys())

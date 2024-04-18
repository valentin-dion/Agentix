from agentix import tool, Conversation, Message

@tool
def tpl_s(tpl_str:str, **kwargs)-> str:
    for key,value in kwargs.items():
        if not isinstance(value, (str,int,float)):
            continue
        tpl_str = tpl_str.replace('{'+key+'}', str(value))
        
    return tpl_str

@tool
def tpl_c(conv:Conversation, **kwargs) -> Conversation:
    parsed_msgs = [] 
    
    for m in conv.msgs:
        parsed_msgs.append(
            Message(role=m.role,
                    content=tpl_s(m.content,**kwargs))
        )
        
    return Conversation(parsed_msgs)

@tool
def tpl(conv, **kwargs):
    if isinstance(conv, str):
        return tpl_s(conv, **kwargs)
    if isinstance(conv, Conversation):
        return tpl_c(conv, **kwargs)
    
    raise ValueError("Input must be a string or an instance of Conversation.")
    
    
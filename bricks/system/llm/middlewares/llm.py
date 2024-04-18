from agentix import mw 

@mw
def llm(ctx, conv):
    
    conv.should_infer = ctx['hops'] == 0
    return conv

@mw
def gpt3(ctx, conv):
    conv.should_infer = ctx['hops'] == 0
    conv.llm = 'gpt-3.5-turbo'
    return conv    
@mw
def gpt4(ctx, conv):
    conv.should_infer = ctx['hops'] == 0
    conv.llm = 'gpt-4-turbo-preview'
    return conv    

@mw
def last_msg_content(ctx, conv):
    return conv[-1].content   
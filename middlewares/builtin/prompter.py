import os
from openai import OpenAI
from agentix import mw, Conversation, Tool, Message
from rich import print

_DEBUG = os.getenv('AGENTFLOW_DEBUG')

def noop(*a,**k): ...

@mw
def simple_prompter(ctx, input_str) -> Conversation:
    return Tool['tpl'](ctx['agent'].base_prompt + Message('user','{user_input}'), **ctx)
    
@mw
def histo_prompter(ctx, input_str):
    base_prompt = ctx['agent'].base_prompt

    histo = ctx['agent'].histo[-12:]
    ret = Tool['tpl']((base_prompt + histo) + Message('user','{user_input}'), **ctx)
    
    ctx['agent'].append_histo(ret[-1])
    
    return ret
    
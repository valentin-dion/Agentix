import os
from openai import OpenAI
from agentix import tool, Conversation, Tool, Log
from rich import print

_DEBUG = os.getenv('AGENTFLOW_DEBUG')



@tool
def llm(conversation: Conversation, model='gpt-4') -> Conversation:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))




    response = client.chat.completions.create(model=conversation.llm, 
            messages=conversation.openai(), 
            max_tokens=4000,
            temperature=.2, 
            stream=True)

     
    _DEBUG and print('\n\n')
    msg = ''
    for message in response:

        mm = message.choices[0].delta.content
                

        if mm:       
                        
            msg += mm
            #Log['onStream'](msg) 
            print('popo ' + msg)
            _DEBUG and print(f"[red]{mm}",end='')
            

    
                    
    return msg
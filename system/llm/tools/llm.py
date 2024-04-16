import os
from openai import OpenAI
from agentix import tool, Conversation, Tool, Log, Event
from rich import print



@tool
def llm(conversation: Conversation, model='gpt-4') -> Conversation:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    Event['beforeInfer'](conversation)
    print(conversation.openai())
    input('ii')
    
    response = client.chat.completions.create(
            model=conversation.llm, 
            messages=conversation.openai(), 
            max_tokens=4000,
            temperature=.2, 
            stream=True
        )

    msg = ''
    Event['stream_chunk']('\n\n\n__\n')
    for message in response:
        mm = message.choices[0].delta.content   
        if mm:                                
            msg += mm
            Event['stream_update'](msg)
            Event['stream_chunk'](mm)
       
    return msg
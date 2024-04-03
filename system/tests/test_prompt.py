from agentix import Agent

def test_prompt():
    Agent('prompt_test_agent','prompt')
    
    assert 'ok'==Agent['prompt_test_agent']('aa')[1].content
    
    
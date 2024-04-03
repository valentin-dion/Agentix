from agentix import Agent

def test_prompt():
    Agent('prompt_test_agent','prompt')
    
    assert 'ok'==Agent['prompt_test_agent']('aa')[1].content

def test_prompt_histo():
    agent_name = 'prompt_test_histo_agent'
    middleware_name = 'prompt_histo'
    Agent(agent_name, middleware_name)

    initial_conv_length = len(Agent[agent_name].histo.msgs)
    Agent[agent_name]('Test message')
    updated_conv_length = len(Agent[agent_name].histo.msgs)

    assert updated_conv_length == initial_conv_length + 1
    
    
import fire
from rich import print

class AgentixCLI:
    def list(self):
        from agentix import Agent
        for agent in Agent.keys():
            print(f"agent:\t[red]{agent}")
    def create(self, name):
        """Creates a new agent structure."""
        import os
        base_path = os.path.join('./agents', name)
        directories = ['agents', 'middlewares', 'tools', 'prompts', 'tests',]
        for directory in directories:
            os.makedirs(os.path.join(base_path, directory), exist_ok=True)
        # Create agent, middleware, and test files
        agent_file_path = os.path.join(base_path, 'agents', f'{name}.py')
        middleware_file_path = os.path.join(base_path, 'middlewares', f'{name}_loop.py')
        test_file_path = os.path.join(base_path, 'tests', f'test_{name}.py')
        prompt_file_path = os.path.join(base_path, 'prompts', f'{name}.conv')
        
        for fp, content in zip(
            [agent_file_path,
             middleware_file_path,
             test_file_path,
             prompt_file_path],
            [
                f'''from agentix import Agent
Agent('{name}', 'prompt_histo|gpt4|{name}_loop')''',

f'''from agentix import mw, Tool

@mw
def {name}_loop(ctx, conv):
    return conv''',
    '''''',
    f'''system:You are {name}, an AGI
__-__
user:hi
__-__
assistant:How can I help you ma bro ?'''
            ]):
            if os.path.isfile(fp):
                continue
            with open(fp,'w') as f:
                f.write(content)

        print(f"[red b]Agentix:[/]Agent structure for [green b]{name}[/] created successfully.")

    def gradio(self, agent_name):
        """Creates a Gradio interface for an agent chatbot."""
        import gradio as gr
        from agentix import Tool
        from rich import print
        
        print(f'[red] Yeah man [blue]{agent_name}')
        print(Tool['shell'](f'python3 ./scripts/runGradio.py {agent_name}'))


    def run(self, name):
        from agentix import Agent,Log, log 
        @log
        def onStream(msg):
            print(f'\n\n[red]{msg}')
        print(Agent[name](input(f"prompt {name}:")))
def main():
    return fire.Fire(AgentixCLI)

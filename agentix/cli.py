import fire
from rich import print

class AgentixCLI:
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

    def gradio(self):
        """Creates a Gradio interface for an agent chatbot."""
        import gradio as gr
        from agentix import Agent

        def chatbot_interface(input_text):
            # Assuming there's a default agent named 'default_agent' for demonstration.
            # This should be replaced with the actual agent you want to use.
            response = Agent['default_agent'](input_text)
            return response[-1].content  # Assuming the response is a Conversation object

        iface = gr.Interface(fn=chatbot_interface, inputs="text", outputs="text", title="Agentix Chatbot")
        iface.launch()

        print("[green b]Gradio chatbot interface launched successfully.[/]")

    def hello(self):
        """Prints a simple hello message."""
        print("Agentix says hello!")

    def dummy_command(self):
        """A dummy command to demonstrate the CLI."""
        print("This is a dummy command.")

def main():
    return fire.Fire(AgentixCLI)

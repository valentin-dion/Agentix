from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
import fire
from rich import print

class AgentixCLI:
    def list(self):
        from agentix import Agent, MW, Tool, Event, Endpoint
        console = Console()
        console.print(Panel("[bold green]Agentix Components List[/bold green]", expand=False))
        
        agents_column = Columns([f"[red]{agent}" for agent in Agent.keys()], title="Agents", expand=True)
        console.print(agents_column)
        console.print("[bold cyan]────────────────────────────────────────────────[/bold cyan]")
        tools_column = Columns([f"[blue]{tool}" for tool in Tool.keys()], title="Tools", expand=True)
        console.print(tools_column)
        console.print("[bold cyan]────────────────────────────────────────────────[/bold cyan]")
        middlewares_column = Columns([f"[green]{mw}" for mw in MW.keys()], title="Middlewares", expand=True)
        console.print(middlewares_column)
        
        console.print("[b cyan]xxxxxxxxxxxx")
        console.print(Endpoint.repr_all())
        
        @Event.on('tocto')
        def prout(tata):
            print(f'event toto:[green]\t{tata}')
            
        Event['tocto']('gazoubicc') 
        
            
        
            
    def endpoint(self, name):
        '''create a new Endpoint'''  
        import os
        base_path = os.path.join('./endpoints/',name)
        from agentix import Endpoint
        
        EP = Endpoint.factory(name)
        EP.code = EP.code or f"""from agentix import endpoint
@endpoint
def {name}():
    return "I'm {name}"
""" 
              
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
        
    def serve(self):
        from agentix import Endpoint
        from flask import Flask
        from flask_cors import CORS
        app = Flask(__name__)
        CORS(app)
        
        Endpoint.bootstrap(app.route)
        
        app.run(debug=True)
        
    def foo(self):
        print('[red on green]x[green on blue]x[black on red]x'*30)
        from agentix import Page, Endpoint
        Page('Logs').template = '<template><h1>logs</h1></template>'
        Page('Logs').css = '''
h1{
    margin:5vh;
    color:#00ff55;
    }'''
        Page('Logs').js = '//TODO'
        

    
        
    
def main():
    return fire.Fire(AgentixCLI)

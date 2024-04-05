import fire

class AgentixCLI:
    def create(self, name):
        """Creates a new agent structure."""
        import os
        base_path = os.path.join('./agents', name)
        directories = ['agents', 'middlewares', 'tools', 'prompts', 'tests']
        for directory in directories:
            os.makedirs(os.path.join(base_path, directory), exist_ok=True)
        print(f"Agent structure for '{name}' created successfully.")

    def hello(self):
        """Prints a simple hello message."""
        print("Agentix says hello!")

    def dummy_command(self):
        """A dummy command to demonstrate the CLI."""
        print("This is a dummy command.")

def main():
    return fire.Fire(AgentixCLI)

import fire

class AgentixCLI:
    def create(self, name):
        """Creates a new agent structure."""
        import os
        base_path = os.path.join('./agents', name)
        directories = ['agents', 'middlewares', 'tools', 'prompts', 'tests', f'agents/{name}', f'middlewares/{name}_loop', f'tests/test_{name}']
        for directory in directories:
            os.makedirs(os.path.join(base_path, directory), exist_ok=True)
        # Create agent, middleware, and test files
        agent_file_path = os.path.join(base_path, 'agents', f'{name}.py')
        middleware_file_path = os.path.join(base_path, 'middlewares', f'{name}_loop.py')
        test_file_path = os.path.join(base_path, 'tests', f'test_{name}.py')
        with open(agent_file_path, 'w') as af:
            af.write(f"# Agent {name}\n")
        with open(middleware_file_path, 'w') as mf:
            mf.write(f"# Middleware loop for {name}\n")
        with open(test_file_path, 'w') as tf:
            tf.write(f"# Tests for {name}\n")

        print(f"Agent structure for '{name}' created successfully.")

    def hello(self):
        """Prints a simple hello message."""
        print("Agentix says hello!")

    def dummy_command(self):
        """A dummy command to demonstrate the CLI."""
        print("This is a dummy command.")

def main():
    return fire.Fire(AgentixCLI)

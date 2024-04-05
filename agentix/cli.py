import fire

class AgentixCLI:
    def hello(self):
        """Prints a simple hello message."""
        print("Agentix says hello!")

    def dummy_command(self):
        """A dummy command to demonstrate the CLI."""
        print("This is a dummy command.")

if __name__ == '__main__':
    fire.Fire(AgentixCLI)

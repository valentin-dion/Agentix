from fire import Fire
from agentix import Agent

@Fire
class Agentix:
    def run_agent(self, name):
        user_input = input("Enter your input: ")
        print(Agent[name](user_input))



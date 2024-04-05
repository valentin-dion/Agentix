from fire import Fire
from agentix import Agent

from rich import print

@Fire
class Agentix:
    def run(self, name):
        user_input = input("Enter your input: ")
        print(Agent[name](user_input))
        
    def gradio(self, name):
        ...



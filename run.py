from agentix import agent 
import fire
from agentix.wrappers import Agent

def run_agent(name):
    user_input = input("Enter your input: ")
    print(Agent[name](user_input))

if __name__ == '__main__':
    fire.Fire({
        'run_agent': run_agent,
    })

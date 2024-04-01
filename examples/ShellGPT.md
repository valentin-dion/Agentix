# ShellGPT Walkthrough

ShellGPT is a terminal you talk to in natural language. It's an agent that, given an instruction, will interact with the terminal in a feedback loop.

## Step 1 Init the agent

we want our Agent to have a prompt (more on that later), have an history, and run LLM inference with user input

`agents/ShellGPT.py`
```python
from agentix import Agent

Agent('ShellGPT','prompt|histo|user_input|llm|shellGPT_loop')
```

(That's the peak of boilerplate you'll need to implement an Agent)


### Explain middlewares
## Step 2 
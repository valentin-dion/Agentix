# About
Hi, I'm Valentin, I tinker with agentic.
I want to automate myself as a senior software engineer.

hire me (or just chat):v@lentin.fr

Cite me: 
[CITATION.cff](CITATION.cff)

# Agentix

Low boilerplate agentic.

## Motivations
[https://nuxt.com](Nuxt) is my inspiration.

I want to be able to write arbitrary agentic pipelines with the minimum amount of code.

I want the complexity to be hidden when I implement agents.

I want an intuitive formalism to implement agentic pipelines with clear logic flow.

File (and by extension, lib) structures are for humans. I want my framework LLM friendly.

## Limitations of Agentix
* The approach is not made for speed. We want the smartest agents, not the most performant
* Everything runs sequentially
## Outrageous Python
So I use python magic to auto-import my agents, middlewares, tools.
If, somewhere within rightly name directories, a .py file exists and contains:
```python
from agentix import tool

@tool
def say_hello(name:str) -> str:
    return f'hello {name}'
```

Then anywhere else, you can just use it :
```python
from agentix import Tool

print(Tool['say_hello']('world'))
```
## Agentic paradigms
[AgenticParadigms.md](Agentic paragigms)


## Agentix's assumptions
### Agents are functions

**Black box description** (as opposed to *implementation details*):
From the outside, an agent is conceptually a function. It ingests inputs and return outputs of given types.
While this principle is simple and doesn't look like much, it proved unsuspectedly powerful to implement complex control flow over LLM inferences.

**Exemple of control flow with agentFlow**
```python
for task in Agent['taskLister'](user_input):
    Agent['taskExecutor'](task)
```

Here's an actual piece of code I used to implement a long term memory:


```python
for fact in Agent['LTM_fact_extract'](user_input):
    Agent['LTM_fact_store'](fact)

context = Agent['LTM_fact_recall'](user_input)
```


It allows for strong algorithmic decoupling, which in turn makes easy to have very specialist agents.

Akin to a function, an agent can itself be an arbitrarly complexe set of agents. Resulting for a given task in many contexts/conversations.

**Note**: One thing I first thought as a tradeoff: my approach is heavy in LLM calls. In reality, it's balanced by the fact it requires overall less tokens generated than other approachs (when done correctly). Also, some Agents can run with `gpt-3.5-turbo`.

_______________



**experimental takeaway of this approach**
* Increase overall performance
* Multi-LLM architecture (some tasks can be handled by _gpt-3.5-turbo_, ) with gains in both speed and cost.

_____________________


### Agents are stacks of middlewares

Time to get our hands dirty


## Agents as stacks of Middlewares (inside view/implementation details)
**Inside**:
From the inside an agent is a stack of ordered middlewares.
Each middleware should only contain agent core logic.
(Printing, streaming, logging... should not ever be middlewares concern)

An agent is instanciated by a string representing the middlewares that composes it

### Primitive types
`Conversation` is an entity composed of value objects `Message`s.
`MW`, `Tool` and `Agent` are containers (`__getitem__(self, key:str)`), holding respectively: middlewares, tools and agents.
`mw` and `tool` are decorators



A conversation contains flags.
if a middleware returns a conversation with `should_infer` flag to `True`, the conversation is fed to a LLM (specified with a flag, `gpt-4` default) then fed back to the same middleware.
In all other cases, the output of a middleware is fed to the next, and the output of the last middleware is the output of the agent.

____

Giving this execution flow:

![Middlewares](./assets/middlewares.png)

____

(As for a real life illustration, here's what the flow of an LTM agent with only passive memory could look like)

![ltm](./assets/ltm1.png)



### Tree of specialists
#### Single responsibility principle


## Agentix tools
TODO: explain auto-import
TODO: explain tool
TODO: explain agent file structure


## Install
```bash
git clone https://github.com/valentin-dion/Agentix.git
cd Agentix
pip install -e .
```
### run gradio
### create new agent
```bash
agentix create MyAgent
```


## Create your first agents
### ShellGPT

### Components factory
## Debug
## Serve
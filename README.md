# About
Hi, I'm Valentin, I tinker with agentic.

I want to automate myself as a senior software engineer.

This repo is about my Framework `Agentix` and what I'll build with it.

## You can hire me !
My current full time job is to work on this repo until I'm hired as an agentic engineer/researcher.

Want to hire me (or just chat) ? : v@lentin.fr

Cite me (for some reason): 
[CITATION.cff](CITATION.cff)

# What I'm currently working on

[Coing a SWE agent](WIP.md)

# Agentix

Low boilerplate functional agentic.
 
_______________

## TL;WR

For an implementation walktrhough go [here](#here1) then [here](#here2)

________________


## Motivations
My approach has some inspiration from [Nuxt](https://nuxt.com/). If you don't know Nuxt, it's low code, It's an extreme example of "hiding the complexity". You can implement anything and the learning curve is sharp.

What motivates me coding my own framework ?

* I want to hide myself as much complexity as possible when I implement agents.

* I want to be able to write arbitrary agentic pipelines with the minimum amount of code.

* I want an intuitive formalism to implement agentic pipelines with clear control flow.

### Foreshadowing a future version
* File (and by extension, lib) structures are for humans. I want my framework LLM friendly.

## Limitations of Agentix
* The approach is not made for speed. We want the smartest agents, not the most performant
* Everything runs sequentially
* If your project involves **RAG** more than **Agentic**, [DSPy](https://github.com/stanfordnlp/dspy) might be a better fit.
* As of right now, Agentix only handles text (though embeddings and other modalities will be considered in a future version)
* If you're looking for a mature project for prod environments, we're not there yet.

## Python Magics and other smelly code
I use python magics to auto-import my agents, middlewares, tools.
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

## Theory
[Agentic paradigms](AgenticParadigms.md)

[Grounding is all you need](Grounding.md)

## Agentix's assumptions
### Agents are functions
[Agent are functions](AgentsAsFunctions.md)

<!--[Why langchain kind of really suck but you've no idea why (it's not your fault)](WhyLangchain.md)-->

_____________________


### Agents are stacks of middlewares

Time to get our hands dirty

[Agents are stacks of middlewares](StacksOfMW.md)



## Agentix tools
### Magic import
In agentix, agent initialization:
```python
from agentix import Agent

Agent('Bob','prompt_histo|bob_router')
```

needs to be executed, not exported. If the code is ran, the agent will exist and be executable anywhere
```python
from agentix import Agent

user_input = input('your input to Bob')
print(Agent['Bob'](user_input))

```

To be imported, a `.py` file only has to exist somewhere under the directories: `agents`, `tools` or `middlewares`
```
📂MyProject
├📂agents
│ └📄fooBar.py
├📂tools
│ ├📂any
│ │├📂depth
│ ││└📄BarFOO.py
├📂middlewares
│ └📄BazBah.py


```

# <a id="here1"></a>
## Install
```bash
git clone https://github.com/valentin-dion/Agentix.git
cd Agentix
pip install -e .
```
### create new agent
```bash
agentix create MyAgent
```
it will create all the boilerplate you need to create an agent.

AKA this file structure:
```
📂 agents
  📂 MyAgent
    ├ 📂 agents
    │ └ 📄 MyAgent.py
    ├ 📂 middlewares 
    │ └ 📄 MyAgent_loop.py
    ├ 📂 prompts
    │ └ 📄 MyAgent.conv
    ├ 📂 tests
    └ 📂 tools

```

### run agent
```bash
agentix run MyAgent
```
### serve agent with gradio
**TODO**

# <a id="here2"></a>
## Create your first agents
### ShellGPT
an agent that handles the linux shell for you.
(or a linux console you can talk to in natural language)

<!--[ShellGPT Walkthrough using TDD](ShellGPT_TDD.md) (TODO)-->

[ShellGPT Walkthrough](ShellGPT.md) (Easy)

### LTM (WIP)
An conversationnal agent with Long Term Memory (Intermediate)
### Agentic Debugger (TODO)
### Frontend component factory (TODO)
### Agent that codes its own tools (TODO)
### Components factory
## Debug
## Serve
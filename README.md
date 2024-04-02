# About
Hi, I'm Valentin, I tinker with agentic.
My long term goal is to automate myself as a senior software engineer.
Since it has been released, I'm convinced GPT-4 is capable of that, with the right cognitive architecture.
This repository, the framework and the experiments using it (I'll release over time), are my best effort towards that goalpost.

donate: BTC & ETH addresses + tipeee
hire me (or just chat):v@lentin.fr

Citation: 
[CITATION.cff](CITATION.cff)

# Agentix

Low boilerplate agentic, as well as everything else.

## Why
I've been researching agentic behaviors for the last 18 months.
The biggest hurdle was accidental complexity.
I took a pause and tried my best to design the most **Low code** and **Low boilerplate** framework to implement agentic logic.
If we're aiming for self improvement, the framework Agents are written in, should also be the framework that Agents write in.
For that reason, Agentix aims at offering tools to write frontend and web server stuff.

It also aims at implementing any arbitrarely complexe agentic flow with the least amount of code.

## Why is the code weird ?

That's a good question.
To access any logical brick, we, human, rely on the files system.

What may be te best approach for humans may not be for LLMs.

Bricks (functions, entities, endpoints, frontend components) should be accessed semanticaly, not through paths of any kind.




## Theory
### Approaches to agentic
* ** Monolithic agent **
* 
![assets/monolith.webp](assets/monolith.webp)
___________

* ** Swarms **
TODO: talk about swarm of clones vs swarms of specialist

______________

* ** Tree of specialists **
TODO: talk about "Agents as code".
TODO: Talk about maximum specialisation
TODO: Agentic single responsibility principle


* Control flow is code's responsibility
* Agents are functions
* The burden of tool use should be taken care of by algorithm whenever it's possible.
* Low level agents should have as little responsibility as possible (idealy, 1~2 tools per agent, no more than 4).


### Grounding is all you need

### Agents

Here we'll define what `Agent`s are in **Agentix**

From an outside/black box perspective `Agent`s are functions.

From an inside/implementation perspective `Agent`s are stacks of middlewares

#### Agents are functions

From the outside, an agent is conceptually a function. It ingests inputs and return outputs of given types. While this principle is simple and doesn't look like much, it proved unsuspectedly powerful to implement complex control flow over LLM inferences.

Exemple of control flow with agentFlow
```python
for task in Agent['taskLister'](user_input):
    Agent['taskExecutor'](task)
```

It allows for agentic with strong algoritmic decoupling, with in turn, makes easy to have very specialist agents.
For a more concrete example, here's an actual piece of code I used in the implementation of a long term memory:

```python
for fact in Agent['LTM_fact_extract'](user_input):
    Agent['LTM_fact_store'](fact)

context = Agent['LTM_fact_recall'](user_input)
```

Akin to a function, an agent can itself be an arbitrarly complexe set of agents. Resulting for a given task in many contexts/conversations.

**Note**: One thing I first thought as a tradeoff: my approach is heavy in LLM calls. In reality, it's balanced by the fact it requires overall less tokens generated than other approachs (when done correctly). Also, some Agents can run with `gpt-3.5-turbo`.

**experimental takeaway of this approach**
* Implementing complexe agentic flow is ridiculously easy !
* Increase overall performances.
* Multi-LLM architecture (some tasks can be handled by _gpt-3.5-turbo_, ) with gains in both speed and cost.

## Agents as stacks of Middlewares (inside view/implementation details)
**Inside**:
From the inside an agent is a stack of ordered middlewares.
Each middleware should only contain agent core logic.
(Printing, streaming, logging... should not ever be middlewares concern)

An agent is instanciated by a string representing the middlewares that composes it

## Concepts
### Message and Conversation in Agentix

Agentix provides two core classes for handling conversational data: `Message` and `Conversation`.

#### Message
The `Message` class represents a single message within a conversation. Each message has a `role` (e.g., 'user', 'system', 'assistant') indicating the sender of the message, and `content` which is the text of the message itself. This class is fundamental for tracking the flow of dialogue between the user and the system or between different components of the system.

#### Conversation
The `Conversation` class encapsulates a sequence of `Message` instances, representing the full exchange between participants over time. It provides methods for creating conversations from strings or files, manipulating them programmatically, and converting them back to strings or files for storage. This allows Agentix to maintain a history of interactions, which is crucial for context management in complex conversational agents.

These classes are designed to be flexible and easy to use, supporting a wide range of conversational agent implementations.
## Walkthroughs
[ShellGPT Walkthrough](/examples/ShellGPT.md)

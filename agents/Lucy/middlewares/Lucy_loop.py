from agentix import mw, Tool, Agent

@mw
def Lucy_loop(ctx, conv):
    parser = Tool['parser']('```agent','```')
    commands = parser(conv[-1].content)
    if commands:
        command,= commands
        agent, message = command.split(':',1)
        if agent not in Agent:
            return conv.rehop(f"{agent}: I'm not a mature and immplemented agent yet, tell that to user")
        return conv.rehop(Agent[agent](message))   
    return conv
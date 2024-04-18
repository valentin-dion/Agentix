from agentix import mw, Tool

@mw
def ShellGPT_loop(ctx, conv):
    parser = Tool['parser']('```sh','```')
    last_msg = conv[-1].content
    commands = parser(last_msg)
    
    if commands:
        #we should only ever have one
        command, = commands
        command_return = Tool['shell'](command)
        return conv.rehop(
            command_return
        )

    return conv
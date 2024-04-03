from agentix import mw

@mw
def prompt(ctx, input_str): 
    return ctx['agent'].base_prompt
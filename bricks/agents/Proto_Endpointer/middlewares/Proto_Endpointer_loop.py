from agentix import mw, Tool, tool, Endpoint


@mw
def Proto_EP_tpl(ctx, conv):
    return Tool['tpl'](conv, all_endpoints=Endpoint.repr_all())




@mw
def Proto_Endpointer_loop(ctx, conv):
    '''
    Here tools to CRUD Endpoints
    '''
    
    return conv

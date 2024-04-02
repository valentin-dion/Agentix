from agentix import Func, Tool, MW, mw, Exec, Agent, ImplState
from rich import print


@mw
def ask_human(ctx, prompt):
    import os
    from time import sleep 
    
    filePath = os.getcwd() + '/AskHuman.txt'
    with open(filePath,'w') as f:
        f.write(prompt)
        
    while 1:
        with open(filePath, 'r') as f:
            cnt = f.read()
            if cnt.startswith('BABAR:'):
                return cnt[6:]
            sleep(1)
    
    
    

@mw
def cody_router(ctx, funcName):
    ...
    '''
    i 
    '''
    """ 
    1) ou en est on dans l'execution ?"""
    "On part de la function funcName"
    "On regarde si elle a les attrs"
    print('[red on green]xX[blue on red]Xx[pink on blue]Xx'*25)
    print('baladur' in Func)
    print(funcName in Func)
    
    fnc = Func[funcName]
    
    print(fnc)
    print('oui')
    #print(Agent['Human']('ça va ?'))
    #fnc.change_impl_state('decrement')
    print(fnc.impl_state == ImplState.NIL)  
    
    print(f"_________________")
    print(f"We're here to implement [green u i]{funcName}")
    print(f"Here we'll ")
     
     
@mw
def mock_func(ctx, funcName):

    
    print(f"[blue]a[red]a[green]a{ctx=}")
    exec = ctx['exec']
    cur = exec.current_cursor
    func = Func[funcName]
    if func.impl_state >= 2:
        return
    Agent['Cody_define_prop'](func)
    Agent['Cody_write_mock_tests'](func)
    
    #
    while func.impl_state < 2:
        Agent['Cody_mock_solve_test'](func)
        
        
def define_func_props(ctx, funcName):
    ...
    # La on va définir une par une les attributs
    Agent['Cody_define_proto'](ctx, funcName)
@mw
def impl_func():...
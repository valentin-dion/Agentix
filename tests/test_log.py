
import os
import pytest
from agentix import Agent, MW, mw, Tool, tool, Log, log
foo = 0
def test_MW():
    global foo
    Log['does_not_exist']('blabla')
    foo = 1
    @log
    def test_log(what):
        global foo
        foo = what
        
    assert foo == 1 
    Log['test_log'](2)
    #test_log(2)
    assert foo==2  
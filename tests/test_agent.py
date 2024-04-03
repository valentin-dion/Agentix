
import os
import pytest
from agentix import Agent, MW, mw, Tool, tool

def test_MW():
    @mw
    def test_mw1(ctx, conv):
        return "ok"
    
    assert MW['test_mw1']({},'') == 'ok'
    
    
def test_agent():
    @mw
    def test_mul2(ctx, conv):
        return conv * 2
    
    @mw
    def test_add_poop(ctx, conv):
        return f"{conv}poop"
    
    Agent('test_agent','test_mul2|test_add_poop')
    assert Agent['test_agent'](2) == "4poop"
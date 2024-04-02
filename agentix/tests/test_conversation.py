import pytest
from agentix.entities import Conversation, Message

def test_conversation_init():
    msgs = [Message("user", "Hello"), Message("system", "Hi there!")]
    conv = Conversation(msgs)
    assert len(conv.msgs) == 2
    assert conv.msgs[0].role == "user"
    assert conv.msgs[0].content == "Hello"
    assert conv.msgs[1].role == "system"
    assert conv.msgs[1].content == "Hi there!"

def test_conversation_add_message():
    conv = Conversation([Message("user", "Hello")])
    conv += Message("system", "Hi there!")
    assert len(conv.msgs) == 2
    assert conv.msgs[1].role == "system"
    assert conv.msgs[1].content == "Hi there!"

def test_conversation_to_dict():
    msgs = [Message("user", "Hello"), Message("system", "Hi there!"), Message("assistant", "How can I assist?")]
    conv = Conversation(msgs)
    expected_output = [
        {'role': 'user', 'content': 'Hello'},
        {'role': 'system', 'content': 'Hi there!'},
        {'role': 'assistant', 'content': 'How can I assist?'}
    ]
    assert conv.to_dict() == expected_output

def test_conversation_from_str():
    conv_str = "user:Hello\n__-__\nsystem:Hi there!"
    conv = Conversation.from_str(conv_str)
    assert len(conv.msgs) == 2
    assert conv.msgs[0].role == "user"
    assert conv.msgs[0].content == "Hello"
    assert conv.msgs[1].role == "system"
    assert conv.msgs[1].content == "Hi there!"

def test_conversation_to_str():
    msgs = [Message("user", "Hello"), Message("system", "Hi there!")]
    conv = Conversation(msgs)
    expected_str = "user:Hello\n__-__\nsystem:Hi there!"
    assert conv.to_str() == expected_str


import os
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
    assert expected_str in conv.to_str() 
    
def test_conversation_flag_persistence():
    msgs = [Message("user", "Testing flags")]
    conv = Conversation(msgs)
    conv.should_infer = True  # Set the flag to True
    temp_file_path = "temp_conv_test.conv"
    conv.to_file(temp_file_path)  # Save to a file
    conv_reloaded = Conversation.from_file(temp_file_path)  # Reload from the file
    assert conv_reloaded.should_infer == True  # Check if the flag is still True
    os.remove(temp_file_path)  # Clean up the temporary file

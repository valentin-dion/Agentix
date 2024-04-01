# Message and Conversation Documentation

## Message
The `Message` class is designed to encapsulate a single message within a conversation. Each message has two main attributes: `role` and `content`.

- `role`: A string indicating the sender of the message. Common roles include 'user', 'system', and 'assistant'.
- `content`: The actual text content of the message.

Messages are the building blocks of conversations in Agentix, allowing for detailed tracking and manipulation of dialogues.

## Conversation
The `Conversation` class represents a sequence of messages, effectively modeling a full conversation. It provides functionality to create, manipulate, and store conversations.

Key methods include:

- `from_file(path: str)`: Class method to create a Conversation instance from a file containing a serialized conversation.
- `from_str(conv_str: str)`: Class method to create a Conversation instance from a string representation of a conversation.
- `to_str()`: Converts the Conversation instance back into a string representation.
- `to_file(path: str)`: Saves the Conversation instance to a file.
- `openai()`: Converts the Conversation into a format suitable for OpenAI API requests.

Conversations can be manipulated programmatically, allowing for dynamic interaction flows. They support addition of new messages or other conversations, enabling complex dialogue management.

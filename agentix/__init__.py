from .magicimport import dynamic_import
from .wrappers import Tool, Agent, tool, mw, MW, Func, func
from .entities import Message, Conversation
from .utils import logger
from .utils.exec import Event, Exec

dynamic_import('middlewares')
dynamic_import('tools')
dynamic_import('funcs')
dynamic_import('agents')
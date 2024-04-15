import queue
import threading
from agentix.wrappers.event import Event
from time import sleep
import sys
from rich import print
from agentix.wrappers.event import Event

agent_name = sys.argv[1]

import gradio as gr

from agentix import tool, Agent

stream_queues = []
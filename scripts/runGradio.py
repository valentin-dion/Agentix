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

@Event.on('streamUpdate')
def handle_stream_update(data):
    """Event handler for streaming updates."""
    stream_queues[0].put(data)




def start_stream():
    stream_queues.append(queue.Queue())




def stream_message(message, histo):
    """Generator function for the frontend library to consume the stream."""
    def launch(m):
        Agent[agent_name](m)
        sleep(0.4)
        Event['streamUpdate']('ENDOFSTUFF')
    th = threading.Thread(target=launch, args=(message,))
    Event['before_message_processing'](message)  # Trigger before processing event


    start_stream()
    th.start()

    while True:
        while not len(stream_queues):
            sleep(0.1)
            print('.', end='')
        data = stream_queues[0].get()  # This will block until data is available


        if data == 'ENDOFSTUFF':
            break
        yield data
        stream_queues[0].task_done()
    while len(stream_queues):
        stream_queues.pop()

    th.join()

print(f'launching [red b u]{agent_name}')
print(gr.ChatInterface(stream_message).launch(share=True, debug=True))

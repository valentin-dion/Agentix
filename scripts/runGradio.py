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


agent_name = sys.argv[1] if len(sys.argv) > 1 else 'default_agent'
stream_queues = []

@Event.on('stream_update')
def handle_stream_update(message):
    for q in stream_queues:
        q.put(message)

def stream_message(message):
    q = queue.Queue()
    stream_queues.append(q)
    def agent_thread():
        Agent[agent_name](message)
    threading.Thread(target=agent_thread).start()
    while True:
        output = q.get()
        if output == 'END':
            break
        yield output
    stream_queues.remove(q)

def setup_gradio_interface():
    iface = gr.Interface(
        fn=stream_message,
        inputs=gr.inputs.Textbox(lines=2, placeholder="Type something..."),
        outputs=gr.outputs.Textbox(),
        allow_flagging="never",
        theme="default",
    )
    return iface

if __name__ == "__main__":
    iface = setup_gradio_interface()
    iface.launch()

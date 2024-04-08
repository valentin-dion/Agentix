import queue
import threading
from time import sleep

import gradio as gr

from agentflow import tool, Agent

stream_queues = []


def start_stream():
    stream_queues.append(queue.Queue())


@tool
def on_stream(data):
    """Callback function for the backend library to put data into the stream."""
    stream_queues[0].put(data)


def stream_message(message, histo):
    """Generator function for the frontend library to consume the stream."""
    def launch(m):
        on_stream(Agent['shell'](m))
        on_stream('ENDOFSTUFF')
    th = threading.Thread(target=launch, args=(message,))

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



print(gr.ChatInterface(stream_message).launch(share=True, debug=True))

import queue1
import zmq
import sys
import time
import math

context = zmq.Context()
socket = context.socket(zmq.SUB)

port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

socket.connect("tcp://localhost:%s" % port)
topicfilter = "A"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)


animate = queue1.Frame_Animator(1)

SINK_RUN_TIME = 30
SOURCE_RUN_TIME = 30
VAL_TO_CAPTURE = 1
counter = 0

while True:
    topic = socket.recv_string()
    data = socket.recv_string()

    VAL_TO_CAPTURE = (1/SINK_RUN_TIME) / (1/SOURCE_RUN_TIME)
    VAL_TO_CAPTURE *= 1.05
    VAL_TO_CAPTURE = math.ceil(VAL_TO_CAPTURE)

    counter += 1

    if counter >= VAL_TO_CAPTURE:
        counter = 0
        t = time.time()
        animate.update(data)
        elapsed = time.time() - t
        SINK_RUN_TIME = 1 / elapsed
        print(VAL_TO_CAPTURE)
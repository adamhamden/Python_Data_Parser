import time
import zmq
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
# Allow clients to connect before sending data
time.sleep(1)
socket.send_string("Hello")
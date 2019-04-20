import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)


port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

# We can connect to several endpoints if we desire, and receive from all.
socket.connect("tcp://localhost:%s" % port)

# We must declare the socket as of type SUBSCRIBER, and pass a prefix filter.
# Here, the filter is the empty string, wich means we receive all messages.
# We may subscribe to several filters, thus receiving from all.


topicfilter = "A"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

while True:
    topic = socket.recv_string()
    data = socket.recv_string()
    print (data)
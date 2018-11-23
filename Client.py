import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5584")

Topic = "1"
Topic = Topic.decode('ascii')

socket.setsockopt_string(zmq.SUBSCRIBE, Topic)

while True:
    data = socket.recv_string()
    Topic, DeviceData = data.split()

    print(DeviceData)
    time.sleep(1)

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5584")

while True:
    Topic = 1
    DeviceData = "0,0,0,0,00,00,00,01"
    socket.send_string("%i %s" % (Topic,DeviceData))

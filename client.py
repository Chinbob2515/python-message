import simpleprotocol

socket = simpleprotocol.SimpleProtocol(port=8080)

if socket.get().code:
    socket.send(1, 0, ["That sounds good!"])
else:
    socket.send(1, 1, ["Oh dear, that's not right..."])

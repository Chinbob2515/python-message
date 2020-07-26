import simpleprotocol

server = simpleprotocol.SimpleServer(port=8080)

while True:
    handler = server.accept()
    handler.send(0)
    print(handler.get())
    handler = server.accept()
    handler.send(1)
    print(handler.get())

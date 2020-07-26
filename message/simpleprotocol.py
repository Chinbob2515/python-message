import .socketwrapper
import .message

LOG = False

class SimpleServer():

    def __init__(self, port):
        self.port = port
        self.socket = socketwrapper.ServerSocket(port=port)

    def accept(self):
        return SimpleSocket(self.socket.getClientObject())

class SimpleProtocol():

    def __init__(self, port):
        self.socket = socketwrapper.ClientSocket(port=port)
        self.message = message.Message(socket=self.socket)

    def __init__(self, socket):
        self.socket = socket
        self.message = message.Message(socket=self.socket)

    def send(self, *args, **kwargs):
        self.message.send(*args, **kwargs)

    def get(self, *args, **kwargs):
        self.message.get(*args, **kwargs)

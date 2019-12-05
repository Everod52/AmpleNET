import socket


class Server:
    def __init__(self, name, host, port):
        self.id = name
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))

    def listen(self, servers=5):
        self.sock.listen(servers)

    def connect(self, s):
        self.sock.connect((s.host, s.port))

    def accept(self):
        return self.sock.accept()

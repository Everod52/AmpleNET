import os
from socket import socket, AF_INET, SOCK_DGRAM


class Client:

    def __init__(self, name, host, port):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.name = name

    def send_mode(self):
        while True:
            data = input(self.name+": " + "Enter message to send or type 'exit': ")
            self.sock.sendto(data.encode(), self.addr)
            if data == "exit":
                break

    def close(self):
        self.sock.close()
        os._exit(0)

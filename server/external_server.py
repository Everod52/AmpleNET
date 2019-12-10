import os
import socket


class ExternalServer:

    def __init__(self, name, port):
        self.id = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host_name = socket.gethostname()

        self.host = socket.gethostbyname(host_name)
        self.port = port
        self.buf = 1024
        self.adr = (self.host, self.port)
        self.sock.bind(self.adr)

    def start_recv(self):
        print("Waiting to receive messages...")
        while True:
            (data, addr) = self.sock.recvfrom(self.buf)
            print("Received message: " + str(data))
            if data == "exit":
                print("client left")
                break

    def close(self):
        self.sock.close()
        os._exit(0)

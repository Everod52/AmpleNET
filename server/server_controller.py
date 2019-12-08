import logging

from server.server import Server
from random import randint
from socket import gethostname, gethostbyname


logging.basicConfig(filename='log.log', level=logging.DEBUG, filemode='w',
                    format='[%(asctime)s - %(name)s - %(levelname)s]: %(message)s')


class ServerController:
    def __init__(self, servers=None):
        self.servers = servers if servers else {}

    def create_server(self, name, host, port):
        s = Server(name, host, port)
        self.servers[name] = {
            'server': s,
            'connection': None,
            'address': None
        }

    def create_default(self, name):
        self.create_server(name, gethostbyname(gethostname()), randint(2000, 50000))

    def connect_server(self, s1, s2):
        server1 = self.servers.get(s1, None)
        server2 = self.servers.get(s2, None)

        if server1 and server2:
            server1 = server1['server']
            server2 = server2['server']
            server1.listen()
            try:
                server2.connect(server1)
            except InterruptedError as e:
                print("Error: Connection was interrupted by another signal: %s", e)
                logging.error("Error: Connection was interrupted by another signal: %s", e)
            conn, addr = server1.accept()
            print("Connection from %s was successfully established with %s" % (server1, server2))
            logging.info("Connection from %s was successfully established with %s", server1, server2)
            self.servers[s1]['connection'] = conn
            self.servers[s1]['address'] = addr

        else:
            print("Server ids are invalid")
            logging.warning("Server ids are invalid")
            print("Error: no connection can be established!")
            logging.error("No connection could be established!")

    def send_message(self, s1, s2, content):
        server1 = self.servers.get(s1, None)
        server2 = self.servers.get(s2, None)

        if server1['connection']:
            sender = server1['connection']
            receiver = server2['server'].sock
        else:
            sender = server1['server'].sock
            receiver = server2['connection']

        sender.send(bytes(content[1:len(content) - 1], "utf-8"))
        data = receiver.recv(1024).decode('utf-8')
        print("Message sent from %s to %s : %s" %
              (server1['server'], server2['server'], data))
        logging.info("Message sent from %s to %s : %s",
                         server1['server'], server2['server'],  data)

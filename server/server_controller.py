from server.server import Server


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

    def connect_server(self, s1, s2):
        server1 = self.servers.get(s1, None)
        server2 = self.servers.get(s2, None)

        if server1 and server2:
            server1 = server1['server']
            server2 = server2['server']
            server1.listen()
            server2.connect(server1)
            conn, addr = server1.accept()
            print("Connection from %s " % server1 + "(%s ,%s) " % server1.sock.getsockname()
                  + "established with %s " % server2 + "(%s ,%s)" % addr)
            self.servers[s1]['connection'] = conn
            self.servers[s1]['address'] = addr
            self.servers[s2]['connection'] = server1.sock
            self.servers[s2]['address'] = server1.sock.getsockname()
        else:
            print("Server ids invalid")
            print("Error: no connection can be established!")

    def send_message(self, s1, s2, content):
        server1 = self.servers.get(s1, None)
        server2 = self.servers.get(s2, None)

        target = server1['connection']
        receiver = server2['server'].sock

        target.send(bytes(content, "utf-8"))
        data = receiver.recv(1024).decode('utf-8')
        print("Message sent from %s " % server1['server'] +
              "to %s " % server2['server'] + ': ', data)



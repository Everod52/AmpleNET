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
            self.servers[s1]['connection'] = conn
            self.servers[s1]['address'] = addr
            if not self.servers[s2]['connection'] and not self.servers[s2]['address']:
                self.servers[s2]['connection'] = conn
                self.servers[s2]['address'] = addr
            else:
                print("Error: server 2 is already connected.")
        else:
            print("Server ids invalid")
            print("Error: no connection can be established!")

from ploudos import ploudos

session = ploudos.login("PloudosAPITest", "12345678") #replace with your PloudOS username / password

servers = session.get_servers_with_name("test")
server = servers[0]
print(server.serverName)
print(server.get_console())

server.start()

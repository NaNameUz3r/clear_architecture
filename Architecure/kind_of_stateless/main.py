from apiServer.server_side import ServerAPI
from apiServer.client_side import Client

commands = ["move 100", "turn -90", "set soap", "start", "move 50", "stop"]

server = ServerAPI(workers_to_spawn=10)
client = Client(server=server)
client.run(commands=commands)

from source_logic import robot_pure as rp
from messages import RobotMessage
from server_side import ServerAPI
from uuid import uuid4


class Client:
    def __init__(self, server: ServerAPI):
        self.server = server
        self.state = rp.RobotState(0.0, 0.0, 0, rp.WATER)
        self.id = uuid4()

    def run(self, commands):
        for command in commands:
            self.state = self.server.process_command(
                RobotMessage(self.state, command=command, client_id=self.id)
            )

        print(self.state.x)

# import source_logic.robot_pure as rp
import robot_pure as rp
from typing import Callable


class ServerApi:
    def __init__(
        self,
        mapper: Callable,
    ) -> None:
        self.mapper = mapper
        self.transfer = rp.transfer_to_cleaner
        self.current_state = rp.RobotState(0.0, 0.0, 0, rp.WATER)

    def interpret_command(self, command: str) -> rp.RobotState:
        command_parts = command.split(" ")
        command_keyword = command_parts[0]

        callback = self.mapper(command_keyword)
        match command_keyword:
            case "move":
                self.current_state = callback(
                    self.transfer,
                    int(command_parts[1]),
                    self.current_state,
                )
            case "turn":
                self.current_state = callback(
                    self.transfer,
                    int(command_parts[1]),
                    self.current_state,
                )
            case "set":
                self.current_state = callback(
                    self.transfer,
                    command_parts[1],
                    self.current_state,
                )
            case "start":
                self.current_state = callback(
                    self.transfer,
                    self.current_state,
                )
            case "stop":
                self.current_state = callback(
                    self.transfer,
                    self.current_state,
                )
        return self.current_state

    def __call__(self, command: str) -> rp.RobotState:
        return self.interpret_command(command)


def function_mapper(command: str) -> Callable | None:
    callback = Callable
    match command:
        case "move":
            callback = rp.move
        case "turn":
            callback = rp.turn
        case "set":
            callback = rp.set_state
        case "start":
            callback = rp.start
        case "stop":
            callback = rp.stop
        case _:
            return None
    return callback


API = ServerApi(function_mapper)

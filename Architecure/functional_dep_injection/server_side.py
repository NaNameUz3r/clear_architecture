# import source_logic.robot_pure as rp
import robot_pure as rp
from typing import Callable


class ServerApi:
    def __init__(
        self,
        make_move: Callable,
        make_turn: Callable,
        set_mode: Callable,
        start_cleaning: Callable,
        stop_robot: Callable,
        transfer: Callable,
    ) -> None:
        self.make_move = make_move
        self.make_turn = make_turn
        self.set_mode = set_mode
        self.start_cleaning = start_cleaning
        self.stop_robot = stop_robot
        self.transfer = transfer
        self.current_state = rp.RobotState(0.0, 0.0, 0, rp.WATER)

    def interpret_command(self, command: str) -> rp.RobotState:
        command_parts = command.split(" ")
        command_keyword = command_parts[0]

        match command_keyword:
            case "move":
                self.current_state = self.make_move(
                    self.transfer,
                    int(command_parts[1]),
                    self.current_state,
                )
            case "turn":
                self.current_state = self.make_turn(
                    self.transfer,
                    int(command_parts[1]),
                    self.current_state,
                )
            case "set":
                self.current_state = self.set_mode(
                    self.transfer,
                    command_parts[1],
                    self.current_state,
                )
            case "start":
                self.current_state = self.start_cleaning(
                    self.transfer,
                    self.current_state,
                )
            case "stop":
                self.current_state = self.stop_robot(
                    self.transfer,
                    self.current_state,
                )
        return self.current_state

    def __call__(self, command: str) -> rp.RobotState:
        return self.interpret_command(command)


API = ServerApi(
    make_move=rp.move,
    make_turn=rp.turn,
    set_mode=rp.set_state,
    start_cleaning=rp.start,
    stop_robot=rp.stop,
    transfer=rp.transfer_to_cleaner,
)

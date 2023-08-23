from typing import Optional, Tuple, Literal, get_args
from utils.exceptions import InvalidCommandException
import math


legal_modes = Literal["water", "soap", "brush"]


class RobotCleaner:
    def __init__(
        self,
        initial_position: Optional[Tuple[int, int]] = (0, 0),
        initial_mode: Optional[legal_modes] = "water",
        initial_angle: Optional[int] = 0,
        is_active: Optional[bool] = True,
    ) -> None:
        self.current_position = initial_position
        self.current_mode = initial_mode
        self.current_angle = initial_angle
        self.is_active = is_active
        self.valid_commands = ["move", "turn", "set", "start", "stop"]
        self.commands_with_args = ["move", "turn", "set"]

    def is_command_valid(self, command: str):
        #TODO: Exceptions should return generic messages, now it is only "Ivalid command"
        if len(command) == 0:
            raise InvalidCommandException
        command_parts = command.split()
        command_keyword = command_parts[0]
        if len(command_parts) > 2 or command_keyword not in self.valid_commands:
            raise InvalidCommandException

        if command_keyword in self.commands_with_args and len(command_parts) < 2:
            raise InvalidCommandException

        if command_keyword == "set" and len(command_parts) > 1:
            new_mode = command_parts[1]
            if new_mode not in get_args(legal_modes):
                raise InvalidCommandException(f"Invalid clean mode: {new_mode}")

    def interpret_command(self, command: str):
        commands_map = {
            "move": self.__move,
            "turn": self.__turn,
            "set": self.__set_mode,
            "start": self.__perform_cleaning,
            "stop": self.__shutdown,
        }

        command_parts = command.split()
        command_keyword = command_parts[0]

        if command_keyword in commands_map:
            method = commands_map[command_keyword]
            arguments = command_parts[1:]

        command_result = method(*arguments)
        return command_result

    def __move(self, distance: str) -> None:
        distance = int(distance)
        # FIXME: it is not nice to round coordinates no 1, for example robot stay
        # in the same place if we pass "move 1" to it.
        x_offset = int(distance * math.cos(math.radians(self.current_angle)))
        y_offset = int(distance * math.sin(math.radians(self.current_angle)))

        self.current_position = (
            self.current_position[0] + x_offset,
            self.current_position[1] + y_offset,
        )

        return f"POS : {self.current_position}"

    def __turn(self, angle: str) -> None:
        angle = int(angle)
        self.current_angle = (self.current_angle + angle) % 360
        return f"ANGLE : {self.current_angle}"

    def __set_mode(self, new_mode: legal_modes) -> None:
        self.current_mode = new_mode
        return f"STATE : {self.current_mode}"

    def __perform_cleaning(self) -> None:
        return f"START WITH {self.current_mode}"

    def __shutdown(self) -> None:
        self.is_active = False
        return "STOP"

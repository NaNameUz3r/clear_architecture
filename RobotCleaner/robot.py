from typing import Optional, Tuple
from utils.exceptions import InvalidCommandException
import math

class ClearMode():
    def __init__(
        self,
    ) -> None:
        self.legal_modes = ("water", "soap", "brush")
class ClearWater(ClearMode):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.mode = "water"

class ClearSoap(ClearMode):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.mode = "soap"

class ClearBrush(ClearMode):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.mode = "brush"


class RobotCleaner:
    def __init__(
        self,
        initial_position: Optional[Tuple[int, int]] = (0, 0),
        initial_mode: Optional[ClearMode] = ClearWater(),
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
        if len(command) == 0:
            raise InvalidCommandException(message="Empty command")
        command_parts = command.split()
        command_keyword = command_parts[0]
        if len(command_parts) > 2 or command_keyword not in self.valid_commands:
            raise InvalidCommandException(message="""Invalid command, or to many arguments, check refer help""")

        if command_keyword in self.commands_with_args and len(command_parts) < 2:
            raise InvalidCommandException(message=f"Command {command_keyword} require additional argument")

        if command_keyword == "set" and len(command_parts) > 1:
            new_mode = command_parts[1]
            if new_mode not in self.current_mode.legal_modes:
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
        # FIXME: it is not ok to convert coordinates to int, because robot stay
        # in place if we pass "move 1", when it "faces" not parallel with axises
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

    def __set_mode(self, new_mode: str):
        match new_mode:
            case "water":
                self.current_mode = ClearWater()
            case "soap":
                self.current_mode = ClearSoap()
            case "brush":
                self.current_mode = ClearBrush()
        return f"STATE : {self.current_mode.mode}"

    def __perform_cleaning(self) -> None:
        return f"START WITH {self.current_mode.mode}"

    def __shutdown(self) -> None:
        self.is_active = False
        return "STOP"

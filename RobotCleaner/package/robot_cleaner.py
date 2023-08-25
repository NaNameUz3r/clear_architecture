from typing import Optional, Tuple
from .base_robot import BaseRobot
from dsl_interpreter.cleaner_interpreter import CleanerInterpreter
from controllers.cleaner_controller import CleanerController

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


class RobotCleaner(BaseRobot):
    def __init__(
        self,
        dsl_interpreter: CleanerInterpreter,
        action_controller: CleanerController,
        initial_position: Optional[Tuple[int, int]] = (0, 0),
        initial_mode: Optional[ClearMode] = ClearWater(),
        initial_angle: Optional[int] = 0,
        is_active: Optional[bool] = True,
    ) -> None:
        self.interpreter = dsl_interpreter
        self.controller = action_controller
        self.current_position = initial_position
        self.current_mode = initial_mode
        self.current_angle = initial_angle
        self.is_active = is_active

    def interpret_command(self, command: str):

        run = self.interpreter.interpret(command=command)

        method = getattr(self, run.method)
        if run.arguments:
            return method(*run.arguments)
        return method()

    def _turn(self, angle: str) -> None:
        angle = int(angle)
        self.current_angle = (self.current_angle + angle) % 360
        return f"ANGLE : {self.current_angle}"

    def _set_mode(self, new_mode: str):
        match new_mode:
            case "water":
                self.current_mode = ClearWater()
            case "soap":
                self.current_mode = ClearSoap()
            case "brush":
                self.current_mode = ClearBrush()
        return f"STATE : {self.current_mode.mode}"

    def _perform_action(self) -> None:
        return f"START WITH {self.current_mode.mode}"

    def _shutdown(self) -> None:
        self.is_active = False
        return "STOP"

"""
    BaseRobot abstract data type specification.
    CONSTRUCTOR
        __init__(self,
            initial_position: Optional[Tuple[int, int]] = (0, 0),
            initial_mode: Optional[ClearMode] = ClearWater(),
            initial_angle: Optional[int] = 0,
            is_active: Optional[bool] = True) -> None:
        Initializes the instance of BaseRobot with initial parameters.

    COMMANDS
        is_command_valid(self, command: str)
            Validate if the given command is valid.

        interpret_command(self, command: str)
            Interpret and execute the given command.

        move(self, distance: str) -> None
            Move the robot by the specified distance.

        turn(self, angle: str) -> None
            Turn the robot by the specified angle.

        set_mode(self, new_mode: str)
            Set the cleaning mode of the robot.

        perform_cleaning(self) -> None
            Start the cleaning operation using the current mode.

        shutdown(self) -> None
            Shutdown the robot.
"""

from typing import Optional, Tuple, Any
from dsl_interpreter.base_interpreter import BaseInterpreter
from controllers.base_controller import ActionController
from .adt_robot import BaseAbstractRobot
import math

class BaseRobot(BaseAbstractRobot):
    def __init__(
        self,
        dsl_interpreter: BaseInterpreter,
        action_controller: ActionController,
        initial_position: Optional[Tuple[int, int]] = (0, 0),
        initial_angle: Optional[int] = 0,
        is_active: Optional[bool] = True,
    ) -> None:
        self.current_position = initial_position
        self.current_angle = initial_angle
        self.is_active = is_active
        self.interpreter = dsl_interpreter
        self.current_mode = Optional[Any] = None

    def interpret_command(self, command: str) -> None:
        pass

    def _move(self, distance: str) -> str:
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

    def _turn(self, angle: str) -> str:
        angle = int(angle)
        self.current_angle = (self.current_angle + angle) % 360
        return f"ANGLE : {self.current_angle}"

    def _set_mode(self, new_mode: str) -> Any:
        pass

    def _perform_action(self) -> Any:
        pass

    def _shutdown(self) -> None:
        self.is_active = False
        return "STOP"

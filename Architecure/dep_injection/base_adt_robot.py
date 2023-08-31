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
            Set the cleaning mode of the robot to valid integer code:
                WATER: int = 1
                SOAP: int = 2
                BRUSH: int = 3

        perform_cleaning(self) -> None
            Start the cleaning operation using the current mode.

        shutdown(self) -> None
            Shutdown the robot.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseAbstractRobot(ABC):
    @abstractmethod
    def __init__(self, n):
        self.n = n
        self.WATER: int = 1
        self.SOAP: int = 2
        self.BRUSH: int = 3

    @abstractmethod
    def interpret_command(self, command: object) -> Any:
        """
        Pre-conditions:
            self.is_active == True
            self.dsl_interpreter initialized
        Post-condition:
            self.dsl_interpreter processed input command and perform correct action
            or raised exception.
        """
        pass

    @abstractmethod
    def _move(self, distance: object) -> Any:
        """
        Pre-conditions:
            self.is_active == True
        Post-condition:
            self.current_position have changed to new position.
        """
        pass

    @abstractmethod
    def _turn(self, angle: object) -> Any:
        """
        Pre-conditions:
            self.is_active == True
        Post-condition:
            self.current_angle have changed to new radian direction.
        """
        pass

    @abstractmethod
    def _set_mode(self, new_mode: str) -> Any:
        """
        Pre-conditions:
            subclass have self.current_mode field instantiated.
            self.is_active == True

        Post-condition:
            self.current_mode have changed to new mode value of valid values.
        """
        pass

    @abstractmethod
    def _perform_action(self) -> Any:
        """
        Pre-conditions:
            subclass have self.action_controller class instantiated.
            self.is_active == True

        Post-condition:
            self.action_controller performs action regarding of self.current_mode.
        """
        pass

    @abstractmethod
    def _shutdown(self) -> None:
        """
        Pre-conditions:
            self.is_active == True

        Post-condition:
            self.is_active set to False
        """
        pass

from typing import Optional, Tuple, Literal
import math


legal_modes = Literal["water", "soap", "brush"]


class RobotCleaner:
    def __init__(self,
                 initial_position: Optional[Tuple[int, int]] = (0, 0),
                 initial_mode: Optional[legal_modes] = "water",
                 initial_angle: Optional[int] = 0,
                 is_active: Optional[bool] = True) -> None:

        self.current_position = initial_position
        self.current_mode = initial_mode
        self.current_angle = initial_angle
        self.is_active = is_active

    def move(self, distance: int) -> None:
        x_offset = int(distance * math.cos(math.radians(self.current_angle)))
        y_offset = int(distance * math.sin(math.radians(self.current_angle)))

        self.current_position = (self.current_position[0] + x_offset,
                                 self.current_position[1] + y_offset)

        return f'POS : {self.current_position}'

    def turn(self, angle: int) -> None:
        self.current_angle = (self.current_angle + angle) % 360
        return f'ANGLE : {self.current_angle}'

    def set_mode(self, new_mode: legal_modes) -> None:
        self.current_mode = new_mode
        return f'STATE : {self.current_mode}'

    def perform_cleaning(self) -> None:
        return f'START WITH {self.current_mode}'

    def shutdown(self) -> None:
        self.is_active = False
        return 'STOP'

from source_logic.robot_pure import RobotState
from uuid import UUID


class BaseRobotMessage:
    def __init__(self, input_state: RobotState, command: str) -> None:
        self.state = input_state
        self.command = command


class RobotMessage(BaseRobotMessage):
    def __init__(
        self, input_state: RobotState, command: str, client_id: UUID | None
    ) -> None:
        super().__init__(input_state, command)
        self.client_id = client_id

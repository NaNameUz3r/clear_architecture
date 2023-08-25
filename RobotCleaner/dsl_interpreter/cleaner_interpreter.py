from .base_interpreter import BaseInterpreter
from typing import Optional, Any
from utils.exceptions import InvalidCommandException

class CleanerCommand():
    def __init__(
        self,
        method: Any,
        arguments: Optional[list[Any]]
    ) -> None:
        self.method = method
        self.arguments = arguments


class CleanerInterpreter(BaseInterpreter):
    def __init__(self) -> None:
        self.valid_commands = ("move", "turn", "set", "start", "stop")
        self.commands_with_args = ["move", "turn", "set"]
    def interpret(self, command: str) -> CleanerCommand:
        try:
            self._is_command_valid(command=command)
        except InvalidCommandException:
            return

        commands_map = {
            "move": "_move",
            "turn": "_turn",
            "set": "_set_mode",
            "start": "_perform_action",
            "stop": "_shutdown",
        }

        command_parts = command.split()
        command_keyword = command_parts[0]

        if command_keyword in commands_map:
            method = commands_map[command_keyword]
            arguments = command_parts[1:]

        return CleanerCommand(method=method,
                              arguments=arguments)

    def _is_command_valid(self, command: str):
        if len(command) == 0:
            raise InvalidCommandException(message="Empty command")
        command_parts = command.split()
        command_keyword = command_parts[0]
        if len(command_parts) > 2 or command_keyword not in self.valid_commands:
            raise InvalidCommandException(message="""Invalid command, or to many arguments, check refer help""")

        if command_keyword in self.commands_with_args and len(command_parts) < 2:
            raise InvalidCommandException(message=f"Command {command_keyword} require additional argument")

        # if command_keyword == "set" and len(command_parts) > 1:
        #     new_mode = command_parts[1]
        #     if new_mode not in self.current_mode.legal_modes:
        #         raise InvalidCommandException(f"Invalid clean mode: {new_mode}")
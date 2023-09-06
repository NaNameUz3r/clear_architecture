import robot_pure as rp


class ServerApi:
    def __init__(self) -> None:
        self.state_stream_container = []
        self.state_stream_container.append(rp.RobotState(0.0, 0.0, 0, rp.WATER))

    def __call__(self, stream):
        split_stream = stream.split(" ")
        for part in split_stream:
            self.interpret_stream(command=part)

    def _pop_from_stream(self):
        popped_item = self.state_stream_container[-1]
        self.state_stream_container.pop()
        return popped_item

    def interpret_stream(self, command):
        match command:
            case "move":
                command_argument, process_state = (
                    self._pop_from_stream(),
                    self._pop_from_stream(),
                )
                self.state_stream_container.append(
                    rp.move(
                        rp.transfer_to_cleaner,
                        int(command_argument),
                        process_state,
                    )
                )
            case "turn":
                command_argument, process_state = (
                    self._pop_from_stream(),
                    self._pop_from_stream(),
                )
                self.state_stream_container.append(
                    rp.turn(
                        rp.transfer_to_cleaner,
                        int(command_argument),
                        process_state,
                    )
                )
            case "set":
                command_argument, process_state = (
                    self._pop_from_stream(),
                    self._pop_from_stream(),
                )
                self.state_stream_container.append(
                    rp.set_state(
                        rp.transfer_to_cleaner,
                        command_argument,
                        process_state,
                    )
                )
            case "start":
                process_state = self._pop_from_stream()
                self.state_stream_container.append(
                    rp.start(
                        rp.transfer_to_cleaner,
                        process_state,
                    )
                )
            case "stop":
                process_state = self._pop_from_stream()
                self.state_stream_container.append(
                    rp.stop(
                        rp.transfer_to_cleaner,
                        process_state,
                    )
                )
            case _:
                self.state_stream_container.append(command)

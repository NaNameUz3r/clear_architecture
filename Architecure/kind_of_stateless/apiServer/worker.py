from source_logic import robot_pure as rp
import threading
from .messages import RobotMessage
import queue as q


class WorkerThread(threading.Thread):
    def __init__(self, input_queue: q.Queue, output_queue: q.Queue):
        threading.Thread.__init__(self=self)
        self.to_process_queue = input_queue
        self.processed_queue = output_queue

    def run(self):
        while True:
            message = self.to_process_queue.get()
            robot_state = message.state
            command_parts = message.command.split()
            command_keyword, command_arg = command_parts[0], command_parts[1]
            match command_keyword:
                case "move":
                    robot_state = rp.move(
                        transfer=rp.transfer_to_cleaner,
                        dist=int(command_arg[1]),
                        state=robot_state,
                    )
                case "turn":
                    robot_state = rp.turn(
                        transfer=rp.transfer_to_cleaner,
                        turn_angle=int(command_arg[1]),
                        state=robot_state,
                    )
                case "set":
                    robot_state = rp.set_state(
                        transfer=rp.transfer_to_cleaner,
                        new_internal_state=command_arg[1],
                        state=robot_state,
                    )
                case "start":
                    robot_state = rp.start(
                        transfer=rp.transfer_to_cleaner, state=robot_state
                    )
                case "stop":
                    robot_state = rp.stop(
                        transfer=rp.transfer_to_cleaner, state=robot_state
                    )
                case _:
                    continue

            # TODO: Need to filter and cleanup such messages from queue
            processed_state = RobotMessage(
                input_state=robot_state,
                command="END PROCESSING",
                client_id=None,
            )
            self.processed_queue.put(item=processed_state)
            self.to_process_queue.task_done()

from source_logic import robot_pure as rp
import queue as q
from .worker import WorkerThread
from .messages import RobotMessage

TO_PROCESS_QUEUE = q.Queue()
PROCESSED_QUEUE = q.Queue()


class ServerAPI:
    def __init__(self, workers_to_spawn=3):
        self.to_process_queue = q.Queue()
        self.processed_queue = q.Queue()

        for _ in range(workers_to_spawn):
            thread = WorkerThread(
                input_queue=self.to_process_queue, output_queue=self.processed_queue
            )
            thread.setDaemon(daemonic=True)
            thread.start()

    def process_command(self, command: RobotMessage):
        self.to_process_queue.put(item=command)
        new_state = self.processed_queue.get()
        self.processed_queue.task_done()
        return new_state

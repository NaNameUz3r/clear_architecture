from robot import RobotCleaner
from utils.exceptions import InvalidCommandException

class InputReconciler():
    def __init__(
        self,
        robot_to_control: RobotCleaner
    ) -> None:
        self.controlled_robot = robot_to_control

    def start_loop(self) -> str:
        print("Enter commands: ")
        try:
            while True:
                input_command = input("> ")
                try:
                    self.controlled_robot.is_command_valid(command=input_command)
                except InvalidCommandException as e:
                    print(e.message)
                    continue

                print(self.controlled_robot.interpret_command(command=input_command))
        except KeyboardInterrupt:
            print(self.controlled_robot.interpret_command("stop"))
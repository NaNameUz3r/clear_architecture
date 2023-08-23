from typing import NoReturn
from robot import RobotCleaner
from utils.exceptions import InvalidCommandException


def main() -> NoReturn:
    robot_instance = RobotCleaner()


    print("Enter commands: ")
    while True:
        input_command = input("> ")
        try:
            robot_instance.is_command_valid(command=input_command)
        except InvalidCommandException:
            print("Invalid command.")
            continue

        print(robot_instance.interpret_command(command=input_command))

if __name__ == "__main__":
    main()
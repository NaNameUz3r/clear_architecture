from typing import NoReturn
from robot import RobotCleaner
from controllers.input_controller import InputReconciler


def main() -> NoReturn:
    robot = RobotCleaner()
    reconciler = InputReconciler(robot_to_control=robot)
    reconciler.start_loop()


if __name__ == "__main__":
    main()

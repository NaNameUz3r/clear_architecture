from package.robot_cleaner import RobotCleaner
from controllers.input_controller import InputReconciler
from dsl_interpreter.cleaner_interpreter import CleanerInterpreter
from controllers.cleaner_controller import CleanerController


def main():
    action_controller = CleanerController()
    interpreter = CleanerInterpreter()
    robot = RobotCleaner(
        dsl_interpreter=interpreter, action_controller=action_controller
    )
    reconciler = InputReconciler(robot_to_control=robot)
    reconciler.start_loop()


if __name__ == "__main__":
    main()

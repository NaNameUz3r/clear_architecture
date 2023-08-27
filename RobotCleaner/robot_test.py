import unittest
from .package.robot_cleaner import RobotCleaner

class TestRobotCleaner(unittest.TestCase):

    def test_init(self) -> None:
        robot = RobotCleaner()
        self.assertEqual(robot.current_position, (0, 0))
        self.assertEqual(robot.current_mode, "water")
        self.assertEqual(robot.current_angle, 0)
        self.assertTrue(robot.is_active)

    def test_move(self) -> None:
        robot = RobotCleaner()
        response = robot.interpret_command("move 10")
        self.assertEqual(robot.current_position, (10, 0))
        self.assertEqual(response, "POS : (10, 0)")

    def test_turn(self) -> None:
        robot = RobotCleaner()
        response = robot.interpret_command("turn 90")
        self.assertEqual(robot.current_angle, 90)
        self.assertEqual(response, "ANGLE : 90")

    def test_turn_and_move(self) -> None:
        robot = RobotCleaner()
        robot.interpret_command("turn 90")
        self.assertEqual(robot.current_angle, 90)
        response = robot.interpret_command("move 5")
        self.assertEqual(robot.current_position, (0, 5))
        self.assertEqual(response, "POS : (0, 5)")

    def test_set_mode(self) -> None:
        robot = RobotCleaner()
        response = robot.interpret_command("set soap")
        self.assertEqual(robot.current_mode, "soap")
        self.assertEqual(response, "STATE : soap")

    def test_perform_cleaning(self) -> None:
        robot = RobotCleaner()
        response = robot.interpret_command("start")
        self.assertEqual(response, "START WITH water")

    def test_shutdown(self) -> None:
        robot = RobotCleaner()
        response = robot.interpret_command("stop")
        self.assertFalse(robot.is_active)
        self.assertEqual(response, "STOP")

if __name__ == '__main__':
    unittest.main()
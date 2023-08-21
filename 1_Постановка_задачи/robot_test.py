import unittest
from robot import RobotCleaner

class TestRobotCleaner(unittest.TestCase):

    def test_init(self):
        robot = RobotCleaner()
        self.assertEqual(robot.current_position, (0, 0))
        self.assertEqual(robot.current_mode, "water")
        self.assertEqual(robot.current_angle, 0)
        self.assertTrue(robot.is_active)

    def test_move(self):
        robot = RobotCleaner()
        response = robot.move(10)
        self.assertEqual(robot.current_position, (10, 0))
        self.assertEqual(response, "POS : (10, 0)")

    def test_turn(self):
        robot = RobotCleaner()
        response = robot.turn(90)
        self.assertEqual(robot.current_angle, 90)
        self.assertEqual(response, "ANGLE : 90")

    def test_turn_and_move(self):
        robot = RobotCleaner()
        robot.turn(90)
        self.assertEqual(robot.current_angle, 90)
        response = robot.move(5)
        self.assertEqual(robot.current_position, (0, 5))
        self.assertEqual(response, "POS : (0, 5)")

    def test_set_mode(self):
        robot = RobotCleaner()
        response = robot.set_mode("soap")
        self.assertEqual(robot.current_mode, "soap")
        self.assertEqual(response, "STATE : soap")

    def test_perform_cleaning(self):
        robot = RobotCleaner()
        response = robot.perform_cleaning()
        self.assertEqual(response, "START WITH water")

    def test_shutdown(self):
        robot = RobotCleaner()
        response = robot.shutdown()
        self.assertFalse(robot.is_active)
        self.assertEqual(response, "STOP")

if __name__ == '__main__':
    unittest.main()
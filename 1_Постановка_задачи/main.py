from robot import RobotCleaner

robot_instance = RobotCleaner()

print("Enter commands: ")
while True:
    input_command = input("> ")

    match input_command.split():
        case ["move", distance]:
            print(robot_instance.move(int(distance)))
        case ["turn", angle]:
            print(robot_instance.turn(int(angle)))
        case ["set", mode]:
            print(robot_instance.set_mode(mode))
        case ["start"]:
            print(robot_instance.perform_cleaning())
        case ["stop"]:
            print(robot_instance.shutdown())
            break
        case _:
            print (f"Command '{input_command}' invalid")

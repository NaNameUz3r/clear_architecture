from robot_pure import make, transfer_to_cleaner, RobotState

def robot_cleaner_api(commands):
    state = RobotState(0,0,0, None)
    state = make(transfer=transfer_to_cleaner, code=commands, state=state)

if __name__ == "__main__":
    commands = [
        'move 100',
        'turn -90',
        'set soap',
        'start',
        'move 50',
        'stop'
    ]
    robot_cleaner_api(commands=commands)
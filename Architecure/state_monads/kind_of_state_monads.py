import math
from collections import namedtuple
from enum import Enum
from typing import List

RobotState = namedtuple(typename="RobotState", field_names="x y angle state")


class CleanerStates(Enum):
    WATER = 1
    SOAP = 2
    BRUSH = 3


def unit(x):
    return (x, [])


def bind(T, f):
    res = f(T[0])
    return (res[0], T[1] + res[1])


def move(distance):
    return lambda state: (
        RobotState(
            state.x + distance * math.cos(state.angle * (math.pi / 180.0)),
            state.y + distance * math.sin(state.angle * (math.pi / 180.0)),
            state.angle,
            state.state,
        ),
        [f"POS({state.x}, {state.y})"],
    )


def turn(turn_angle):
    return lambda state: (
        RobotState(state.x, state.y, state.angle + turn_angle, state.state),
        [f"ANGLE, {state.angle}"],
    )


def set_state(new_internal_state):
    def inner_mutation(state):
        match new_internal_state:
            case "water":
                self_state = CleanerStates.WATER.name
            case "soap":
                self_state = CleanerStates.SOAP.name
            case "brush":
                self_state = CleanerStates.BRUSH.name
            case _:
                return state
        return (
            RobotState(state.x, state.y, state.angle, self_state),
            [f"STATE, {self_state}"],
        )

    return inner_mutation


def start():
    return lambda state: (state, [f"START WITH, {state.state}"])


def stop():
    return lambda state: (state, ["STOP"])


def interpret_commands(
    commands: List[str],
    initial_state: RobotState,
):
    current_state = unit(initial_state)

    for command in commands:
        tokens = command.split()
        if len(tokens) == 0:
            continue

        action = tokens[0]
        args = tokens[1:]

        match action:
            case "move":
                distance_to_move = float(args[0])
                current_state = bind(current_state, move(distance_to_move))
            case "turn":
                angle = float(args[0])
                current_state = bind(current_state, turn(angle))
            case "set":
                mode = args[0]
                current_state = bind(current_state, set_state(mode))
            case "start":
                current_state = bind(current_state, start())
            case "stop":
                current_state = bind(current_state, stop())

    return current_state


initial_state = RobotState(
    x=0,
    y=0,
    angle=0,
    state=CleanerStates.WATER.name,
)
commands = [
    "move 100",
    "turn -90",
    "set soap",
    "start",
    "move 50",
    "stop",
]
final_state, actions = interpret_commands(commands, initial_state)

print(actions)
print("Final State:", final_state)

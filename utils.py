import sys
from enum import Enum

UNDEFINED_F_VALUE = -100
INFINITY = sys.maxsize - 100


class TODO:
    def __init__(self, msg=""):
        raise Exception("{\n\tTODO: " + msg + "\n}")


class AlgorithmType(Enum):
    DLS = 1
    A_STAR = 2
    IDA_STAR = 3
    BIDIRECTIONAL_A_STAR = 4
    MAX_ENUM_VALUE = 4  # TODO: please keep this updated to the maximum available

    def __init__(self, a):
        self._value_ = a


class HeuristicFunctionExplanations:
    # instantiate this class if you want an explanation for heuristics:
    def __init__(self):
        print("-----------------------------------------------------------------------------")
        print("Heuristic Functions:\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("1: The amount of cars infront of the red car.\t\t\t\t\t\t\t\t|")
        print("2: The amount of cars that cover the third row.\t\t\t\t\t\t\t\t|")
        print("3: DLS.\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        print("4: The amount of cars that cover the third row, infront of the red car.\t\t|")
        print("-----------------------------------------------------------------------------")
        print("Algorithms to Run:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
        for current_type in AlgorithmType:
            current_type_as_string = "{}".format(current_type)
            current_type_as_string = current_type_as_string.replace("AlgorithmType.", "")
            tabs_to_append = ""
            to_print = "{}: {}".format(current_type._value_, current_type_as_string)
            num_of_spaces_to_add = 19 - int((len(to_print)/4))
            for i in range(0, num_of_spaces_to_add):
                tabs_to_append += "\t"
            to_print = to_print + tabs_to_append + "|"
            print(to_print)
        print("-----------------------------------------------------------------------------")
        print("Running...")


def str_to_int(msg: str):
    return int(float(msg))


def display_colored_text(color, text):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text
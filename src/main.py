from simple_data_type.SimpleDataTypes import SimpleDataTypes
from strings.Strings import Strings
from infrastructure.SystemIO import SystemIO


def run_simple_data_types():
    simple_data_type = SimpleDataTypes(SystemIO())
    simple_data_type.exercise_two()
    simple_data_type.exercise_tree()
    simple_data_type.exercise_four()
    simple_data_type.exercise_five()
    simple_data_type.exercise_six()
    simple_data_type.exercise_seven()
    simple_data_type.exercise_eight()
    simple_data_type.exercise_nine()
    simple_data_type.exercise_ten()
    simple_data_type.exercise_eleven()
    simple_data_type.exercise_twelve()


def run_strings():
    strings = Strings(SystemIO())
    strings.exercise_one()
    strings.exercise_two()
    strings.exercise_tree()
    strings.exercise_four()
    strings.exercise_five()
    strings.exercise_six()


if __name__ == '__main__':
    run_simple_data_types()
    run_strings()

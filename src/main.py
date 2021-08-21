from simple_data_type.SimpleDataTypes import SimpleDataTypes
from infrastructure.SystemIO import SystemIO
from src.strings.Strings import Strings


def run_simple_data_types():
    simple_data_type = SimpleDataTypes(SystemIO())
    # editar a partir de acá
    simple_data_type.exercise_one()
    # simple_data_type.exercise_two()


def run_strings():
    strings = Strings(SystemIO())
    # editar a partir de acá
    strings.exercise_one()
    # strings.exercise_two()


if __name__ == '__main__':
    run_strings()

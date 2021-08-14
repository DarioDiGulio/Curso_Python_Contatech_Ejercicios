from simple_data_type.SimpleDataTypes import SimpleDataTypes
from infrastructure.SystemIO import SystemIO


def run_simple_data_types():
    simple_data_type = SimpleDataTypes(SystemIO())
    simple_data_type.exercise_one()


if __name__ == '__main__':
    run_simple_data_types()

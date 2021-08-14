from simple_data_type.SimpleDataTypes import SimpleDataTypes
from infrastructure.SystemIO import SystemIO


def run_simple_data_types():
    simple_data_type = SimpleDataTypes(SystemIO())
    # editar a partir de acá
    simple_data_type.exercise_one()
    # simple_data_type.exercise_two()


if __name__ == '__main__':
    run_simple_data_types()

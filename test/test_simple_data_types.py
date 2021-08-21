from unittest import TestCase
import unittest
from src.simple_data_type.SimpleDataTypes import SimpleDataTypes
from IOStub import IOStub


class TestSimpleDataTypes(TestCase):

    def setUp(self) -> None:
        self.simple_data_types = SimpleDataTypes(IOStub())
        self.io = self.simple_data_types.io

    def tearDown(self) -> None:
        self.io = IOStub()

    def test_exercise_one(self):
        self.simple_data_types.exercise_one()

        self.assertTrue('hola mundo' in self.io.output_text.lower())

    def test_exercise_two(self):
        self.simple_data_types.exercise_two()

        self.assertTrue('hola mundo' in self.io.output_text.lower())

    def test_exercise_tree(self):
        self.io.input_text = 'Contatech'

        self.simple_data_types.exercise_tree()

        self.assertTrue('hola contatech' in self.io.output_text.lower())

    def test_exercise_four(self):
        self.simple_data_types.exercise_four()

        self.assertTrue('0.25' in str(self.io.output_text))

    def test_exercise_five(self):
        self.io.input_text = '10,5'

        self.simple_data_types.exercise_five()

        self.assertTrue('50' in self.io.output_text)

    def test_exercise_six(self):
        self.io.input_text = '5'

        self.simple_data_types.exercise_six()

        self.assertTrue('15' in str(self.io.output_text))

    def test_exercise_seven(self):
        self.io.input_text = '70,1.65'

        self.simple_data_types.exercise_seven()

        self.assertTrue('25.71' in self.io.output_text)

    def test_exercise_eight(self):
        self.io.input_text = '4,2'

        self.simple_data_types.exercise_eight()

        self.assertTrue('2' in self.io.output_text)
        self.assertTrue('0' in self.io.output_text)

    def test_exercise_nine(self):
        self.io.input_text = '1000,10,5'

        self.simple_data_types.exercise_nine()

        self.assertTrue('1610.51' in self.io.output_text)

    def test_exercise_ten(self):
        self.io.input_text = '150,200'

        self.simple_data_types.exercise_ten()

        self.assertTrue('31800' in self.io.output_text)

    def test_exercise_eleven(self):
        self.io.input_text = '150'

        self.simple_data_types.exercise_eleven()

        output = str(self.io.output_text)
        self.assertTrue('156.0' in output)
        self.assertTrue('162.24' in output)
        self.assertTrue('168.73' in output)

    def test_exercise_twelve(self):
        self.io.input_text = '100'

        self.simple_data_types.exercise_twelve()

        output = str(self.io.output_text)
        self.assertTrue('3.49' in output)
        self.assertTrue('60' in output)
        self.assertTrue('139.6' in output)


if __name__ == '__main__':
    unittest.main()

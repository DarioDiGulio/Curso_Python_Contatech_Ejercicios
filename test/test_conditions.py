import unittest
from parameterized import parameterized

from IOStub import IOStub
from src.conditions.Conditions import Conditions


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.conditions = Conditions(IOStub())
        self.io = self.conditions.io

    def tearDown(self) -> None:
        self.io = IOStub()

    @parameterized.expand([
        ["17", "No sos mayor de edad."],
        ["18", "Sos mayor de edad."],
        ["19", "Sos mayor de edad."],
    ])
    def test_exercise_one(self, age, result):
        self.io.input_text = age

        self.conditions.exercise_one()

        self.assertEqual(result, self.io.output_text)

    @parameterized.expand([
        ["asd1234", "No coincide."],
        ["contraseña", "Coincide."],
        ["CONTRASEÑA", "Coincide."],
        ["COntrASeñA", "Coincide."],
    ])
    def test_exercise_two(self, user_input, result):
        self.io.input_text = user_input

        self.conditions.exercise_two()

        self.assertEqual(result, self.io.output_text)

    @parameterized.expand([
        ["5", "0", "¡Error! No se puede dividir por 0."],
        ["20", "2", "El resultado de la división es 10."],
        ["15", "3", "El resultado de la división es 5."],
        ["15", "2", "El resultado de la división es 7."],
    ])
    def test_exercise_tree(self, dividend, divider, result):
        self.io.input_text = f'{dividend},{divider}'

        self.conditions.exercise_tree()

        self.assertEqual(result, self.io.output_text)

    @parameterized.expand([
        ["6", "El número 6 es par."],
        ["223", "El número 223 es impar."],
    ])
    def test_exercise_four(self, number, result):
        self.io.input_text = number

        self.conditions.exercise_four()

        self.assertEqual(result, self.io.output_text)

    @parameterized.expand([
        ["6", "10000", "No tenés que cotizar."],
        ["24", "50", "No tenés que cotizar."],
        ["18", "1000", "Tenés que cotizar."],
        ["20", "1000", "Tenés que cotizar."],
    ])
    def test_exercise_five(self, age, capital, result):
        self.io.input_text = f'{age},{capital}'

        self.conditions.exercise_five()

        self.assertEqual(result, self.io.output_text)

    @parameterized.expand([
        ["F", "Carmen", "Tu grupo es A."],
        ["F", "Laura", "Tu grupo es A."],
        ["M", "Marcos", "Tu grupo es A."],
        ["M", "Saúl", "Tu grupo es A."],
        ["M", "Dardo", "Tu grupo es B."],
        ["M", "Leandro", "Tu grupo es B."],
        ["F", "Sofía", "Tu grupo es B."],
        ["F", "María", "Tu grupo es B."],
    ])
    def test_exercise_six(self, gender, name, result):
        self.io.input_text = f'{gender},{name}'

        self.conditions.exercise_six()

        self.assertEqual(result, self.io.output_text, f'El sexo es {gender} y el nombre es {name}')


if __name__ == '__main__':
    unittest.main()

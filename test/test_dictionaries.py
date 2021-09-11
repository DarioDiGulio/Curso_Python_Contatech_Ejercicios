import unittest
from unittest import TestCase
from parameterized import parameterized

from IOStub import IOStub
from collectiones.Dictionaries import Dictionaries


class MyTestCase(TestCase):

    def setUp(self) -> None:
        self.dictionaries = Dictionaries(IOStub())
        self.io = self.dictionaries.io

    def tearDown(self) -> None:
        self.io = IOStub()

    @parameterized.expand([
        ["Dólar", "$"],
        ["Euro", "€"],
        ["Yen", "¥"],
        ["Real", "La divisa no está en el diccionario."],
        ["Sol", "La divisa no está en el diccionario."]
    ])
    def test_exercise_one(self, user_input: str, exercise_output: str):
        self.io.input_text = user_input

        self.dictionaries.exercise_one()

        self.assertEqual(self.io.output_text, exercise_output)

    def test_exercise_two(self):
        self.io.input_text = "Juan,25,Calle falsa 123,123123123"

        self.dictionaries.exercise_two()

        self.assertEqual(
            self.io.output_text,
            "Juan tiene 25 años, vive en Calle falsa 123 y su número de teléfono es 123123123"
        )

    @parameterized.expand([
        ["Plátano", 10, "10.0 kilos de Plátano valen $13.5"],
        ["Manzana", 10, "10.0 kilos de Manzana valen $8.0"],
        ["Naranja", 10, "10.0 kilos de Naranja valen $7.0"],
        ["Durazno", 10, "Lo siento, la fruta Durazno no está disponible."],
        ["Sandía", 10, "Lo siento, la fruta Sandía no está disponible."]
    ])
    def test_exercise_tree(self, fruta: str, cantidad: float, exercise_output: str):
        self.io.input_text = f'{fruta},{cantidad}'

        self.dictionaries.exercise_tree()

        self.assertEqual(exercise_output, self.io.output_text)

    @parameterized.expand([
        ["12/12/1912", "12 de diciembre de 1912"],
        ["12/11/1912", "12 de noviembre de 1912"],
        ["12/10/1912", "12 de octubre de 1912"]
    ])
    def test_exercise_four(self, input_date: str, output: str):
        self.io.input_text = input_date

        self.dictionaries.exercise_four()

        self.assertEqual(output, self.io.output_text.lower())

    def test_exercise_five(self):
        self.dictionaries.exercise_five()
        print(self.io.output_text)
        self.assertEqual("Matemáticas tiene 6 créditos" in self.io.output_text, True,
                         f"Debería ser Matemáticas tiene 6 créditos y fue {self.io.output_text}"
                         )
        self.assertEqual("Física tiene 4 créditos" in self.io.output_text, True,
                         f"Debería ser Física tiene 4 créditos y fue {self.io.output_text}"
                         )
        self.assertEqual("Química tiene 5 créditos" in self.io.output_text, True,
                         f"Debería ser Química tiene 5 créditos y fue {self.io.output_text}"
                         )
        self.assertEqual("Número total de créditos del curso: 15" in self.io.output_text, True,
                         f"Número total de créditos del curso: 15 y fue {self.io.output_text}"
                         )

    def test_exercise_six(self):
        pass


if __name__ == '__main__':
    unittest.main()

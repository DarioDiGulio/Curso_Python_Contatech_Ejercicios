import unittest
from parameterized import parameterized

from collectiones.ListsAndTuples import ListsAndTuples
from test.IOStub import IOStub


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.lists_and_tuples = ListsAndTuples(IOStub())
        self.io = self.lists_and_tuples.io

    def tearDown(self) -> None:
        self.io = IOStub()

    def test_exercise_one(self):
        self.lists_and_tuples.exercise_one()

        self.assertEqual(self.io.output_text, ["Matemáticas", "Física", "Química", "Historia", "Lengua"])

    def test_exercise_two(self):
        self.lists_and_tuples.exercise_two()

        self.assertTrue("Yo estudio Matemáticas" in self.io.output_text)
        self.assertTrue("Yo estudio Física" in self.io.output_text)
        self.assertTrue("Yo estudio Química" in self.io.output_text)
        self.assertTrue("Yo estudio Historia" in self.io.output_text)
        self.assertTrue("Yo estudio Lengua" in self.io.output_text)

    def test_exercise_tree(self):
        self.io.input_text = "1,2,3,4,5"

        self.lists_and_tuples.exercise_tree()

        self.assertTrue("En Matemáticas has sacado 1" in self.io.output_text)
        self.assertTrue("En Física has sacado 2" in self.io.output_text)
        self.assertTrue("En Química has sacado 3" in self.io.output_text)
        self.assertTrue("En Historia has sacado 4" in self.io.output_text)
        self.assertTrue("En Lengua has sacado 5" in self.io.output_text)

    def test_exercise_four(self):
        self.io.input_text = "46,25,32,15,9,21"

        self.lists_and_tuples.exercise_four()

        self.assertEqual(self.io.output_text, "Los números ganadores son [9, 15, 21, 25, 32, 46]")

    def test_exercise_five(self):
        self.lists_and_tuples.exercise_five()

        self.assertEqual(self.io.output_text, "10,\n9,\n8,\n7,\n6,\n5,\n4,\n3,\n2,\n1,")

    def test_exercise_six(self):
        self.io.input_text = "4,6,8,9,1"

        self.lists_and_tuples.exercise_six()

        result_list = ["Matemáticas", "Lengua"]
        self.assertTrue(f"Tienes que repetir {str(result_list)}" in self.io.output_text)

    def test_exercise_seven(self):
        self.lists_and_tuples.exercise_seven()

        self.assertFalse('c' in self.io.output_text)
        self.assertFalse('f' in self.io.output_text)
        self.assertFalse('i' in self.io.output_text)
        self.assertFalse('l' in self.io.output_text)
        self.assertFalse('ñ' in self.io.output_text)
        self.assertFalse('q' in self.io.output_text)
        self.assertFalse('t' in self.io.output_text)
        self.assertFalse('w' in self.io.output_text)

    @parameterized.expand([
        ["arara", 1],
        ["mayor", 0],
        ["anana", 1],
        ["casa", 0],
    ])
    def test_exercise_eight(self, word, result):
        self.io.input_text = word

        self.lists_and_tuples.exercise_eight()

        if result == 1:
            self.assertFalse("No" in self.io.output_text)
        else:
            self.assertTrue("No" in self.io.output_text)

    def test_exercise_nine(self):
        self.io.input_text = "casa"

        self.lists_and_tuples.exercise_nine()

        self.assertTrue("2" in self.io.output_text)

    def test_exercise_ten(self):
        self.lists_and_tuples.exercise_ten()

        self.assertTrue("mínimo es 8" in self.io.output_text)
        self.assertTrue("máximo es 80" in self.io.output_text)

    def test_exercise_eleven(self):
        self.lists_and_tuples.exercise_eleven()

        self.assertTrue("5" in self.io.output_text)

    def test_exercise_twelve(self):
        self.io.input_text = "1-2-3-4-5"

        self.lists_and_tuples.exercise_twelve()

        self.assertTrue("3.0" in self.io.output_text, self.io.output_text)
        self.assertTrue("1.4142135623730951" in self.io.output_text)


if __name__ == '__main__':
    unittest.main()


from unittest import TestCase
import unittest
from IOStub import IOStub
from src.strings.Strings import Strings


class TestStrings(TestCase):

    def setUp(self) -> None:
        self.strings = Strings(IOStub())
        self.io = self.strings.io

    def tearDown(self) -> None:
        self.io = IOStub()

    def test_exercise_one(self):
        # Given
        self.io.input_text = 'contatech,5'
        # When
        self.strings.exercise_one()
        # Then
        self.assertEqual("contatech\ncontatech\ncontatech\ncontatech\ncontatech\n", self.io.output_text)

    def test_exercise_two(self):
        self.io.input_text = 'Conta Tech'

        self.strings.exercise_two()

        self.assertTrue("conta tech" in self.io.output_text)
        self.assertTrue("CONTA TECH" in self.io.output_text)
        self.assertTrue("Conta Tech" in self.io.output_text)

    def test_exercise_tree(self):
        self.io.input_text = "Contatech"

        self.strings.exercise_tree()

        self.assertTrue("CONTATECH" in self.io.output_text)
        self.assertTrue("9" in self.io.output_text)

    def test_exercise_four(self):
        self.io.input_text = '+54-1111111111-12'

        self.strings.exercise_four()

        self.assertEqual('1111111111', self.io.output_text)

    def test_exercise_five(self):
        self.io.input_text = 'Tecnología para económicas'

        self.strings.exercise_five()

        self.assertEqual('sacimónoce arap aígolonceT', self.io.output_text)

    def test_exercise_six(self):
        self.io.input_text = 'Tecnología para económicas,a'

        self.strings.exercise_six()

        self.assertEqual('TecnologíA pArA económicAs', self.io.output_text)

    def test_exercise_seven(self):
        self.io.input_text = 'info@contatech.ar'

        self.strings.exercise_seven()

        self.assertEqual('info@ceu.es', self.io.output_text)

    def test_exercise_eight(self):
        self.io.input_text = '150.20'

        self.strings.exercise_eight()

        self.assertTrue('150 pesos' in self.io.output_text.lower())
        self.assertTrue('20 centavos' in self.io.output_text.lower())

    def test_exercise_nine(self):
        self.io.input_text = '12/12/2012'

        self.strings.exercise_nine()

        self.assertTrue('día 12' in self.io.output_text.lower())
        self.assertTrue('mes 12' in self.io.output_text.lower())
        self.assertTrue('año 2012' in self.io.output_text.lower())


if __name__ == '__main__':
    unittest.main()

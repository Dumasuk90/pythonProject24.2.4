import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 6) == 12

    def test_division(self):
        assert self.calc.division(self, 5, 10) == 0.5

    def test_subtraction(self):
        assert self.calc.subtraction(self, 46, 50) == -4

    def test_adding(self):
        assert self.calc.adding(self, 12, 67) == 79


    def teardown(self):
        print('Выполнение метода Teardown')
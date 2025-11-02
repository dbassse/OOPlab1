import os
import sys
from typing import Any

from lab1oop.task_package_2.zad2 import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


class TestFraction:
    def test_initialization_default(self) -> None:
        frac = Fraction()
        assert frac.integer == 0
        assert frac.fractional == 0
        assert frac.value == 0.0

    def test_initialization_with_values(self) -> None:
        frac = Fraction(1, 8)
        assert frac.integer == 1
        assert frac.fractional == 8
        assert frac.value == 1.8

    def test_value_property(self) -> None:
        frac = Fraction(12, 34)
        assert frac.value == 12.34

    def test_addition_with_number(self) -> None:
        frac = Fraction(1, 5)
        result = frac + 2.0
        assert result == 3.5

    def test_addition_with_fraction(self) -> None:
        frac1 = Fraction(1, 5)
        frac2 = Fraction(2, 3)
        result = frac1 + frac2
        assert result == 3.8

    def test_subtraction(self) -> None:
        frac = Fraction(5, 5)
        assert frac - 2.0 == 3.5
        assert frac - Fraction(1, 2) == 4.3

    def test_multiplication(self) -> None:
        frac = Fraction(2, 5)
        assert frac * 2 == 5.0
        assert frac * Fraction(2, 0) == 5.0

    def test_comparison_operators(self) -> None:
        frac = Fraction(1, 5)

        assert frac < 2.0
        assert frac < Fraction(2, 0)

        assert frac > 0.5
        assert frac > Fraction(0, 9)

        assert frac <= 1.5
        assert frac <= Fraction(1, 5)

        assert frac >= 1.5
        assert frac >= Fraction(1, 5)

    def test_equality(self) -> None:
        frac1 = Fraction(1, 5)
        frac2 = Fraction(1, 5)
        frac3 = Fraction(2, 3)

        assert frac1 == frac2
        assert frac1 == 1.5
        assert frac1 != frac3
        assert frac1 != 2.0

    def test_display(self, capsys: Any) -> None:
        frac = Fraction(1, 8)
        frac.display()
        captured = capsys.readouterr()
        assert "1.8" in captured.out

    def test_string_representation(self) -> None:
        frac = Fraction(1, 8)
        assert "1.8" in str(frac)


class TestFractionEdgeCases:
    def test_large_numbers(self) -> None:
        frac = Fraction(999, 999)
        assert frac.value == 999.999

    def test_zero_fractional(self) -> None:
        frac = Fraction(5, 0)
        assert frac.value == 5.0

    def test_single_digit_fractional(self) -> None:
        frac = Fraction(0, 5)
        assert frac.value == 0.5

    def test_multiple_digits_fractional(self) -> None:
        frac = Fraction(1, 234)
        assert frac.value == 1.234

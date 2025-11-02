import math
import os
import sys
from typing import Any

import pytest

from lab1oop.task_package_1.zad1 import Pair

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


class TestPair:
    def test_initialization_default(self) -> None:
        pair = Pair()
        assert pair.first == 0.0
        assert pair.second == 0.0

    def test_initialization_with_values(self) -> None:
        pair = Pair(3.5, 4.2)
        assert pair.first == 3.5
        assert pair.second == 4.2

    def test_initialization_with_ints(self) -> None:
        pair = Pair(3, 4)
        assert pair.first == 3.0
        assert pair.second == 4.0

    def test_initialization_invalid(self) -> None:
        with pytest.raises(ValueError):
            Pair("invalid", "values")  # type: ignore

    def test_distance_calculation(self) -> None:
        pair = Pair(3.0, 4.0)
        expected_distance = 5.0  # 3-4-5 triangle
        assert math.isclose(pair.distance(), expected_distance)

    def test_distance_zero(self) -> None:
        pair = Pair(0.0, 0.0)
        assert pair.distance() == 0.0

    def test_make_pair(self) -> None:
        pair = Pair(1.0, 2.0)
        pair.make_pair(5.5, 6.6)
        assert pair.first == 5.5
        assert pair.second == 6.6

    def test_display(self, capsys: Any) -> None:
        pair = Pair(1.5, 2.5)
        pair.display()
        captured = capsys.readouterr()
        assert "(1.5, 2.5)" in captured.out


class TestPairEdgeCases:
    def test_negative_coordinates(self) -> None:
        pair = Pair(-3.0, -4.0)
        assert pair.distance() == 5.0

    def test_large_numbers(self) -> None:
        pair = Pair(1000.0, 1000.0)
        expected = math.sqrt(2_000_000)
        assert math.isclose(pair.distance(), expected)

    def test_float_precision(self) -> None:
        pair = Pair(0.1, 0.2)
        result = pair.distance()
        expected = math.sqrt(0.01 + 0.04)
        assert math.isclose(result, expected)

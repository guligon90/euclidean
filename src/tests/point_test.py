from typing import List
from enum import Enum
import pytest

from src.point import Point, TNumber


class EOperation(Enum):
    SUMMATION = "summation",
    SUBSTRACTION = "subtraction",
    SCALAR_PRODUCT = "scalar_product",
    EQUALITY = "equality",


@pytest.mark.parametrize("inputs,operation,expected", [
    [
        [Point(1, 2), Point(3, 4)],
        EOperation.SUMMATION.value,
        Point(4, 6)
    ],
    [
        [Point(0, 3), Point(-1, 5)],
        EOperation.SUBSTRACTION.value,
        Point(1, -2),
    ],
    [
        [-2, Point(3, -7)],
        EOperation.SCALAR_PRODUCT.value,
        Point(-6, 14),
    ],
])
def test_operation_between_inputs(inputs: List[Point], operation: str, expected: Point):
    operation_map = {
        EOperation.SUMMATION.value: lambda p1, p2: p1 + p2,
        EOperation.SUBSTRACTION.value: lambda p1, p2: p1 - p2,
        EOperation.SCALAR_PRODUCT.value: lambda k, p: k * p,
    }

    operator = operation_map.get(operation)

    assert operator != None, "invalid operation between inputs"

    a, b = inputs
    result = operator(a, b)

    assert result.x == expected.x, f"X coordinate is not {expected.x}"
    assert result.y == expected.y, f"Y coordinate is not {expected.y}"


@pytest.mark.parametrize("inputs,expected", [
    [
        [Point(1, 2), Point(3, 4)],
        False,
    ],
    [
        [Point(0, 1), Point(0, 1)],
        True,
    ],
])
def test_equality_between_points(inputs, expected):
    p1, p2 = inputs
    result = p1 == p2

    assert result == expected, f"equality failed between {p1} and {p2}"

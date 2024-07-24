from __future__ import annotations
from math import sqrt

__all__ = [
    "TNumber",
    "Point"
]


TNumber = float | int


class Point:
    def __init__(self, x: TNumber, y: TNumber) -> Point:
        self.x = x
        self.y = y
        self.length = self.length()

    def length(self) -> TNumber:
        return sqrt(self * self)

    def __add__(self, p: Point) -> Point:
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: Point) -> Point:
        return Point(self.x - p.x, self.y - p.y)

    def __eq__(self, p: Point) -> bool:
        return self.x == p.x and self.y == p.y

    def __rmul__(self, k: TNumber) -> Point:
        return Point(k * self.x, k * self.y)

    def __mul__(self, p: Point) -> TNumber:
        return self.x*p.x + self.y*p.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

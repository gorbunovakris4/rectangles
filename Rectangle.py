from __future__ import annotations


class Rectangle:
    def __init__(self, x: float, y: float):
        self._x = max(x, y)
        self._y = min(x, y)

    def __lt__(self, other: Rectangle) -> bool:
        return (self._y, self._x) < (other._y, other._x)

    def len(self):
        return self._x

    def height(self):
        return self._y

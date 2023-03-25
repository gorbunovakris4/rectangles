from Rectangle import Rectangle
from Selection import Selection
from typing import List, Dict, Tuple


class Field:
    def __init__(self, w, h):
        self._w = w
        self._h = h
        self._rectangles: Dict[Tuple[int, int, int], Rectangle] = {}
        self._rest_rectangles = []
        self._selector = Selection(w)

    def locate_rectangles(self, rectangles):
        self._rest_rectangles = rectangles.copy()
        h = 0
        c = 1
        while len(self._rest_rectangles) > 0:
            rect, rest = self._selector.choose(self._rest_rectangles)
            w = 0
            max_h = 0
            for r in rect:
                max_h = max(max_h, r.height())
            if h + max_h > self._h:
                h = 0
                c += 1
            for r in rect:
                self._rectangles[(h, w, c)] = r
                w += r.len()
            h += max_h
            self._rest_rectangles = rest.copy()

    def __repr__(self):
        field = [[0] * self._h for _ in range(self._w)]
        for key, value in self._rectangles.items():
            x, y = key[0], key[1]
            for i in range(x, x + value.len()):
                for j in range(y, y + value.height()):
                    field[i][j] += 1
        res = ""
        for i in range(self._w):
            for j in range(self._h):
                if field[i][j] == 0:
                    res += '_'
                else:
                    res += str(field[i][j])
                res += ' '
            res += '\n'
        return res

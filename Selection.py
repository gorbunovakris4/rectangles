from typing import List
from Rectangle import Rectangle


class Selection:

    def __init__(self, w):
        self._w = w
        self._ans = []
        self._rest = []
        self._rectangles = []

    def select(self, rectangles: List[Rectangle]) -> List[List[int]]:
        n = len(rectangles)
        din = [[0] * (self._w + 1) for _ in range(n + 1)]
        for i in range(1, 1 + n):
            for w in range(1, self._w + 1):
                din[i][w] = din[i - 1][w]
                if rectangles[i - 1].len() <= w:
                    din[i][w] = max(din[i][w], din[i - 1][w - rectangles[i - 1].len()] + rectangles[i - 1].len())
        return din

    def selected(self, din: List[List[int]], k: int, s: int):
        if din[k][s] == 0:
            for i in range(k):
                self._rest.append(self._rectangles[i])
            return
        if din[k - 1][s] == din[k][s]:
            self.selected(din, k - 1, s)
            self._rest.append(self._rectangles[k - 1])
        else:
            self.selected(din, k - 1, s - self._rectangles[k - 1].len())
            self._ans.append(self._rectangles[k - 1])

    def choose(self, rectangles: List[Rectangle]):
        self._ans = []
        self._rest = []
        self._rectangles = rectangles
        self.selected(self.select(rectangles), len(rectangles), self._w)
        return self._ans, self._rest

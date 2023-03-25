import pytest
from Selection import Selection
from Rectangle import Rectangle


def test_selection():
    selection = Selection(10)
    res, rest = selection.choose([Rectangle(1, 1), Rectangle(4, 4), Rectangle(8, 8)])
    assert len(res) == 2
    assert res[0].len() + res[1].len() == 9
    assert len(rest) == 1


def test_selection2():
    selection = Selection(20)
    res, rest = selection.choose([Rectangle(5, 5), Rectangle(7, 7), Rectangle(12, 12), Rectangle(18, 18)])
    assert len(res) == 2
    assert res[0].len() + res[1].len() == 19
    assert len(rest) == 2

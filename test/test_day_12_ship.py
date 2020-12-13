# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_12_ship import loadExerciseDataFrom
from aoc.day_12_ship import main
from aoc.day_12_ship import resolvePuzzle01Using
from aoc.day_12_ship import resolvePuzzle02Using

import pytest


# +++ constants +++

TEST_SHIP_FILE_NAME = 'resources/test/ship-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_SHIP_FILE_NAME)


def test_resolvePuzzle01Using():
    answer = resolvePuzzle01Using(_data, _tokens)

    assert answer == 25


def test_resolvePuzzle02Using():
    answer, \
    v = resolvePuzzle02Using(_data, _tokens)

    assert answer == 286
    assert v.x == -72
    assert v.y == 214


def test_main():
    assert main(TEST_SHIP_FILE_NAME) == (25, 286)


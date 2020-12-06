# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.%t% import loadExerciseDataFrom
from aoc.%t% import main

import pytest


# +++ constants +++

TEST_%T%_FILE_NAME = 'resources/test/%t%-test-data.txt'


# +++ tests +++

_exerciseData = None  # a collection


def test_loadExerciseDataFrom():
    global _exerciseData

    _exerciseData = loadExerciseDataFrom(TEST_%T%_FILE_NAME)
    assert False


def test_main():
    assert main(TEST_%T%_FILE_NAME) == (False, False)


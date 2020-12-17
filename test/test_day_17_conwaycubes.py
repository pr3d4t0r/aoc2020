# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_17_conwaycubes import loadExerciseDataFrom
from aoc.day_17_conwaycubes import main
from aoc.day_17_conwaycubes import resolvePuzzle01Using
from aoc.day_17_conwaycubes import resolvePuzzle02Using

import pytest


# +++ constants +++

TEST_DAY_17_CONWAYCUBES_FILE_NAME = 'resources/test/day_17_conwaycubes-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_DAY_17_CONWAYCUBES_FILE_NAME)


def test_resolvePuzzle01Using():
    answer = resolvePuzzle01Using(_data, _tokens, shape = 15)

    assert 112 == answer


def test_resolvePuzzle02Using():
    global _data, _tokens

    _data, _tokens = loadExerciseDataFrom(TEST_DAY_17_CONWAYCUBES_FILE_NAME)
    answer = resolvePuzzle02Using(_data, _tokens, unitTest = True)

    assert answer == 848


def test_main():
    global _data, _tokens

    _data, _tokens = loadExerciseDataFrom(TEST_DAY_17_CONWAYCUBES_FILE_NAME)

    assert main(TEST_DAY_17_CONWAYCUBES_FILE_NAME, unitTest = True) == (112, 848)


# TODO: --- remove before final check-in ---

# test_resolvePuzzle01Using()
# test_resolvePuzzle02Using()
test_main()


# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.%t% import loadExerciseDataFrom
from aoc.%t% import main
from aoc.%t% import resolvePuzzle01Using
from aoc.%t% import resolvePuzzle02Using

import pytest


# +++ constants +++

TEST_%T%_FILE_NAME = 'resources/test/%t%-test-data.txt'


# +++ tests +++

_data = None  # a collection
_tokens = None


def test_loadExerciseDataFrom():
    global _data

    _data, tokens = loadExerciseDataFrom(TEST_%T%_FILE_NAME)

    assert len(_data)
    assert len(_tokens)


def test_resolvePuzzle01Using():
    x = resolvePuzzle01Using(_data)

    assert x == -1


def test_resolvePuzzle02Using():
    x = resolvePuzzle02Using(_data)

    assert x == -1


def test_main():
    assert main(TEST_%T%_FILE_NAME) == (-1, -1)


# TODO: --- remove before final check-in ---

# test_loadExerciseDataFrom()
# test_resolvePuzzle01Using()
# test_resolvePuzzle02Using()
# test_main()


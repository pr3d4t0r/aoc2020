# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.bus import loadExerciseDataFrom
from aoc.bus import main
from aoc.bus import resolvePuzzle01Using
from aoc.bus import resolvePuzzle02Using

import pytest


# +++ constants +++

TEST_BUS_FILE_NAME = 'resources/test/bus-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_BUS_FILE_NAME)


def test_resolvePuzzle01Using():
    answer = resolvePuzzle01Using(_data, _tokens)

    assert answer == 295


def test_resolvePuzzle02Using():
    busSchedule = [busID for busID in _data[1].split(',')]

    answer = resolvePuzzle02Using(busSchedule)
    assert answer == 1068781 


def test_main():
    assert main(TEST_BUS_FILE_NAME) == (295, 1068781)


# TODO: --- remove before final check-in ---

# test_resolvePuzzle01Using()
# test_resolvePuzzle02Using()
# test_main()


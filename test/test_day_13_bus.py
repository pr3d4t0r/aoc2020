# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_13_bus import loadExerciseDataFrom
from aoc.day_13_bus import main
from aoc.day_13_bus import resolvePuzzle01Using
from aoc.day_13_bus import resolvePuzzle02Using

import pytest


# +++ constants +++

TEST_BUS_FILE_NAME = 'resources/test/day_13_bus-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_BUS_FILE_NAME)


def test_resolvePuzzle01Using():
    earliestDeparture = int(_data[0])
    busSchedule = [int(busID) for busID in _data[1].split(',') if busID != 'x']

    answer, departureWait = resolvePuzzle01Using(earliestDeparture, busSchedule)

    assert answer == 295
    assert departureWait == 5


def test_resolvePuzzle02Using():
    busSchedule = [int(busID) if busID != 'x' else -1 for busID in _data[1].split(',')]

    answer = resolvePuzzle02Using(busSchedule)
    assert answer == 1068781 


def test_main():
    assert main(TEST_BUS_FILE_NAME) == (295, 1068781)


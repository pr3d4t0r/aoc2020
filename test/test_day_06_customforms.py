# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.day_06_customforms import loadExerciseDataFrom
from aoc.day_06_customforms import main
from aoc.day_06_customforms import confirmedMixedAnswers
from aoc.day_06_customforms import confirmedGroupAnswers

import pytest


# +++ constants +++

TEST_CUSTOMFORMS_FILE_NAME = 'resources/test/customforms-test-data.txt'


# +++ tests +++

_groupData = None


def test_loadExerciseDataFrom():
    global _groupData

    _groupData = loadExerciseDataFrom(TEST_CUSTOMFORMS_FILE_NAME)

    assert isinstance(_groupData, list)
    assert _groupData[1] == 'a\nb\nc'
    assert _groupData[2] == 'ab\nac'


def test_confirmedMixedAnswers():
    assert confirmedMixedAnswers(_groupData) == 11


def test_confirmedGroupAnswers():
    assert confirmedGroupAnswers(_groupData) == 6


def test_main():
    assert main(TEST_CUSTOMFORMS_FILE_NAME) == (11, 6)


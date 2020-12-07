# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.baggage import loadExerciseDataFrom
from aoc.baggage import main
from aoc.baggage import resolvePuzzle01Using
from aoc.baggage import resolvePuzzle02Using
from aoc.baggage import __extractFrom

import pytest


# +++ constants +++

TEST_BAGGAGE_FILE_NAME = 'resources/test/baggage-test-data.txt'
TEST_RAW_DATA = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.',
]


# +++ tests +++

_data = None  # a collection


def test_loadExerciseDataFrom():
    global _data

    _data = loadExerciseDataFrom(TEST_BAGGAGE_FILE_NAME)

    assert _data[0] == TEST_RAW_DATA[0]
    assert len(_data) == len(TEST_RAW_DATA)


def test___extractFrom():
    test0 = 'dark orange bag'
    test1 = 'dotted black bag'
    assert __extractFrom(TEST_RAW_DATA[1])
    assert __extractFrom(TEST_RAW_DATA[8])


def test_resolvePuzzle01Using():
    x = resolvePuzzle01Using(_data)

    assert x == -1


def test_resolvePuzzle02Using():
    x = resolvePuzzle02Using(_data)

    assert x == -1


def test_main():
    assert main(TEST_BAGGAGE_FILE_NAME) == (-1, -1)


# TODO: --- remove before final check-in ---

test_loadExerciseDataFrom()
# test___extractFrom()
test_resolvePuzzle01Using()
# test_resolvePuzzle02Using()
# test_main()


# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.baggage import TARGET_BAG_TYPE
from aoc.baggage import _defineRulesFrom
from aoc.baggage import _resolveInnerBagsWith
from aoc.baggage import loadExerciseDataFrom
from aoc.baggage import main
from aoc.baggage import resolvePuzzle01Using
from aoc.baggage import resolvePuzzle02Using

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

_data = None
_rules = None


def test_loadExerciseDataFrom():
    global _data

    _data = loadExerciseDataFrom(TEST_BAGGAGE_FILE_NAME)

    assert _data[0] == TEST_RAW_DATA[0]
    assert len(_data) == len(TEST_RAW_DATA)


def test__defineRulesFrom():
    rules = _defineRulesFrom(_data)

    assert len(rules) == 9
    assert 'shiny gold' in rules
    assert 'vibrant plum' in rules['shiny gold']


def test_resolvePuzzle01Using():
    global _rules

    answer, \
    _rules = resolvePuzzle01Using(_data)

    assert answer == 4


def test__resolveInnerBagsIn():
    result = _resolveInnerBagsWith(_rules, TARGET_BAG_TYPE)

    assert result


def test_resolvePuzzle02Using():
    result = resolvePuzzle02Using(_data)

    assert 32 == result


def test_main():
    assert main(TEST_BAGGAGE_FILE_NAME) == (4, 32)


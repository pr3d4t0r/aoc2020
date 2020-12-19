# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_19_validmsgs import _parseRuleFrom
from aoc.day_19_validmsgs import _process
from aoc.day_19_validmsgs import _rulesAndMessagesFrom
from aoc.day_19_validmsgs import loadExerciseDataFrom
from aoc.day_19_validmsgs import main
from aoc.day_19_validmsgs import resolvePuzzle01Using
from aoc.day_19_validmsgs import resolvePuzzle02Using


# +++ constants +++

TEST_COMPLETE = ['',]
TEST_DAY_19_VALIDMSGS_FILE_NAME = 'resources/test/day_19_validmsgs-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_DAY_19_VALIDMSGS_FILE_NAME)

_rules = {
    0: '4 1 5',
    1: '2 3 | 3 2',
    2: '4 4 | 5 5',
    3: '4 5 | 5 4',
    4: 'a',
    5: 'b',
}


def test__parseRuleFrom():
    assert (0, [[4, 1, 5,]]) == _parseRuleFrom('0: 4 1 5')
    assert (3, [[4, 5,], [5, 4,]],) == _parseRuleFrom('3: 4 5 | 5 4')
    assert (4, 'a') == _parseRuleFrom('4: "a"')


def test__rulesAndMessagesFrom():
    rules, messages = _rulesAndMessagesFrom(_data)

    assert 6 == len(rules)
    assert [[4, 1, 5,]] == rules[0]
    assert 'b' == rules[5]

    assert 5 == len(messages)
    assert all(isinstance(m, str) for m in messages)


_rules, _messages = _rulesAndMessagesFrom(_data)

def test__process():
    assert TEST_COMPLETE == _process('ababbb', 0, _rules)
    assert TEST_COMPLETE != _process('aaababbb', 0, _rules)


def test_resolvePuzzle01Using():
    answer, _, _, = resolvePuzzle01Using(_data, _tokens)

    assert answer == 2


def test_resolvePuzzle02Using():
    answer = resolvePuzzle02Using(_rules, _messages)

    assert answer == 2


def test_main():
    assert main(TEST_DAY_19_VALIDMSGS_FILE_NAME) == (2, 2,)


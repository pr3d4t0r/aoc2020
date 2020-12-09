# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.xmascypher import loadExerciseDataFrom
from aoc.xmascypher import main
from aoc.xmascypher import resolvePuzzle01Using
from aoc.xmascypher import resolvePuzzle02Using

import pytest


# +++ constants +++

TEST_XMASCYPHER_FILE_NAME = 'resources/test/xmascypher-test-data.txt'
TEST_PREAMBLE_LENGTH = 5


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_XMASCYPHER_FILE_NAME)


def test_resolvePuzzle01Using():
    global _data 

    answer, _data = resolvePuzzle01Using(_data, _tokens, TEST_PREAMBLE_LENGTH)

    assert answer == 127


def test_resolvePuzzle02Using():
    global _data

    x, \
    _data = resolvePuzzle01Using(_data, _tokens, TEST_PREAMBLE_LENGTH)
    answer = resolvePuzzle02Using(_data, _tokens, TEST_PREAMBLE_LENGTH, x)

    assert answer == 62


def test_main():
    assert main(TEST_XMASCYPHER_FILE_NAME, preambleLength = TEST_PREAMBLE_LENGTH) == (127, 62)


# TODO: --- remove before final check-in ---

# test_resolvePuzzle01Using()
test_resolvePuzzle02Using()
# test_main()


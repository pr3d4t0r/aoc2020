# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.adapters import loadExerciseDataFrom
from aoc.adapters import main
from aoc.adapters import resolvePuzzle01Using
from aoc.adapters import resolvePuzzle02Using


# +++ constants +++

TEST_ADAPTERS_FILE_NAME = 'resources/test/adapters-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_ADAPTERS_FILE_NAME)

_chain = None


def test_resolvePuzzle01Using():
    global _chain

    answer, _chain = resolvePuzzle01Using(_data, _tokens)

    assert answer == 220


def test_resolvePuzzle02Using():
    answer = resolvePuzzle02Using(_chain)

    assert answer == 19208


def test_main():
    assert main(TEST_ADAPTERS_FILE_NAME) == (220, 19208)


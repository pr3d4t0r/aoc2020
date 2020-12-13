# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_08_gamecomp import loadExerciseDataFrom
from aoc.day_08_gamecomp import main
from aoc.day_08_gamecomp import resolvePuzzle01Using
from aoc.day_08_gamecomp import resolvePuzzle02Using


# +++ constants +++

TEST_GAMECOMP_FILE_NAME = 'resources/test/gamecomp-test-data.txt'


# +++ tests +++

_data = None  # a collection
_tokens = None


def test_loadExerciseDataFrom():
    global _data

    _data, _tokens = loadExerciseDataFrom(TEST_GAMECOMP_FILE_NAME) # TODO

    assert len(_data)
    assert len(_tokens)


def test_resolvePuzzle01Using():
    acc = resolvePuzzle01Using(_data)

    assert acc == 5


def test_resolvePuzzle02Using():
    acc = resolvePuzzle02Using(_data)

    assert acc == 8


def test_main():
    assert main(TEST_GAMECOMP_FILE_NAME) == (5, 8)


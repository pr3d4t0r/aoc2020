# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_15_numsgame import loadExerciseDataFrom
from aoc.day_15_numsgame import main
from aoc.day_15_numsgame import resolvePuzzle01Using
# from aoc.day_15_numsgame import resolvePuzzle02Using


# +++ constants +++

TEST_DAY_15_NUMSGAME_FILE_NAME = 'resources/test/day_15_numsgame-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_DAY_15_NUMSGAME_FILE_NAME)


def test_resolvePuzzle01Using():
    answer = resolvePuzzle01Using(_data, _tokens)

    assert answer == 436


# def test_resolvePuzzle02Using():
#     answer = resolvePuzzle02Using(_data, _tokens)
# 
#     assert answer == 175594


def test_main():
    assert main(TEST_DAY_15_NUMSGAME_FILE_NAME, unitTest = True) == (436, -1)


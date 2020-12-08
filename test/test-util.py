# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import die
from util import loadExerciseDataFrom
from util import mainStart


# --- constants ---

TEST_EXERCISE_DATA_LOAD_FILE_NAME = './resources/test/gamecomp-test-data.txt'


# +++ tests +++

def test_die():
    die('bogus', 0, unitTest = True)
    pass


def test_mainStart():
    assert mainStart('bogus-name.txt', 1) == 'bogus-name.txt'


def test_loadExerciseDataFrom():
    _data, _tokens = loadExerciseDataFrom(TEST_EXERCISE_DATA_LOAD_FILE_NAME)

    assert len(_data)
    assert len(_tokens)
    assert isinstance(_data, list)
    assert isinstance(_tokens, list)


test_loadExerciseDataFrom()


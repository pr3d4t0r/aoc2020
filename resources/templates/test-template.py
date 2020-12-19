# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.%t% import main
from aoc.%t% import resolvePuzzle01Using
from aoc.%t% import resolvePuzzle02Using
from util import loadExerciseDataAsTextRecordsFrom
from util import loadExerciseDataFrom
from util import loadRawExerciseTextFrom


# +++ constants +++

TEST_%T%_FILE_NAME = 'resources/test/%t%-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_%T%_FILE_NAME)

_rawText = loadRawExerciseTextFrom(TEST_%T%_FILE_NAME)

_textRecords = loadExerciseDataAsTextRecordsFrom(TEST_%T%_FILE_NAME)


def test_resolvePuzzle01Using():
    answer = resolvePuzzle01Using(_data, _tokens, _rawText, _textRecords)

    assert answer == -1


def test_resolvePuzzle02Using():
    answer = resolvePuzzle02Using(_data, _tokens, _rawText, _textRecords)

    assert answer == -1


def test_main():
    assert main(TEST_%T%_FILE_NAME) == (-1, -1)


# TODO: --- remove before final check-in ---

# test_resolvePuzzle01Using()
# test_resolvePuzzle02Using()
# test_main()


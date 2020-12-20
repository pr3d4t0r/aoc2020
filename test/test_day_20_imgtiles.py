# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from bitarray import bitarray

from aoc.day_20_imgtiles import main
from aoc.day_20_imgtiles import resolvePuzzle01Using
from aoc.day_20_imgtiles import _tileFromRecord
from aoc.day_20_imgtiles import resolvePuzzle02Using
from aoc.day_20_imgtiles import _edgesOf
from util import loadExerciseDataAsTextRecordsFrom
from util import loadExerciseDataFrom
from util import loadRawExerciseTextFrom


# +++ constants +++

SAMPLE_TILE = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###
"""

TEST_DAY_20_IMGTILES_FILE_NAME = 'resources/test/day_20_imgtiles-test-data.txt'


# +++ tests +++


_data, _tokens = loadExerciseDataFrom(TEST_DAY_20_IMGTILES_FILE_NAME)

_rawText = loadRawExerciseTextFrom(TEST_DAY_20_IMGTILES_FILE_NAME)

_textRecords = loadExerciseDataAsTextRecordsFrom(TEST_DAY_20_IMGTILES_FILE_NAME)


def test__edgesOf():
    tile = SAMPLE_TILE.split(':\n')[1]
    northEdge = bitarray('0011010010')
    westEdge = bitarray('0111110010')

    edges = _edgesOf(tile)

    assert northEdge == edges.north
    assert westEdge == edges.west


def test__tileFromRecord():
    northEdge = bitarray('0011010010')
    westEdge = bitarray('0111110010')

    tileID, tile, edges = _tileFromRecord(SAMPLE_TILE)

    assert 2311 == tileID
    assert '#' == tile[8]
    assert northEdge == edges.north
    assert westEdge == edges.west


def test_resolvePuzzle01Using():
    answer = resolvePuzzle01Using(_data, _tokens, _rawText, _textRecords)

    assert answer == -1


def test_resolvePuzzle02Using():
    answer = resolvePuzzle02Using(_data, _tokens, _rawText, _textRecords)

    assert answer == -1


def test_main():
    assert main(TEST_DAY_20_IMGTILES_FILE_NAME) == (-1, -1)


# TODO: --- remove before final check-in ---

test__edgesOf()
test__tileFromRecord()
test_resolvePuzzle01Using()
# test_resolvePuzzle02Using()
# test_main()


# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.boardingpass import _colFrom
from aoc.boardingpass import _rowFrom
from aoc.boardingpass import _seatInfo
from aoc.boardingpass import findHighestIDIn
from aoc.boardingpass import loadBoardingPassesFrom
from aoc.boardingpass import main


# +++ constants +++

TEST_BOARDINGPASS_FILE_NAME = 'resources/test/boardingpass-test-data.txt'
TEST_BOARDINGPASS_ENTRY = 'FBFBBFFRLR'


# +++ tests +++

_boardingPasses = None

def test_loadBoardingPassesFrom():
    global _boardingPasses

    _boardingPasses = loadBoardingPassesFrom(TEST_BOARDINGPASS_FILE_NAME)
    
    assert _boardingPasses[0] == TEST_BOARDINGPASS_ENTRY


def test__rowFrom():
    assert _rowFrom(_boardingPasses[0]) == 44
    assert _rowFrom(_boardingPasses[1]) == 70
    assert _rowFrom(_boardingPasses[2]) == 14
    assert _rowFrom(_boardingPasses[3]) == 102


def test__colFrom():
    assert _colFrom(_boardingPasses[0]) == 5
    assert _colFrom(_boardingPasses[1]) == 7
    assert _colFrom(_boardingPasses[2]) == 7
    assert _colFrom(_boardingPasses[3]) == 4


def test__seatInfo():
    assert _seatInfo(_boardingPasses[0]) == (44, 5, 357, )
    assert _seatInfo(_boardingPasses[1]) == (70, 7, 567, )
    assert _seatInfo(_boardingPasses[2]) == (14, 7, 119, )
    assert _seatInfo(_boardingPasses[3]) == (102, 4, 820, )


def test_findHighestIDIn():
    maxID, seatIDs = findHighestIDIn(_boardingPasses)

    assert maxID == 820
    assert isinstance(seatIDs, list)


def test_main():
    maxID, _ = main(TEST_BOARDINGPASS_FILE_NAME)

    assert maxID == 820


# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.seats import loadExerciseDataFrom
from aoc.seats import main
from aoc.seats import resolvePuzzle01Using
from aoc.seats import resolvePuzzle02Using
from aoc.seats import _getAdjacentPositionsTo
from aoc.seats import _applyRule1To
from aoc.seats import _applyRule2To
from aoc.seats import _assertNoChangeIn
# from aoc.seats import _getLoSPositions
# from aoc.seats import _findSeatPositionsFrom

import copy

import pytest


# +++ constants +++

TEST_SEATS_FILE_NAME = 'resources/test/seats-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_SEATS_FILE_NAME)


def test__getAdjacentPositionsTo():
    positions = _getAdjacentPositionsTo(0, 0, 5, 4)
    assert positions == [ (0, 1), (1, 0), (1, 1), ]

    positions = _getAdjacentPositionsTo(4, 1, 5, 4)
    assert positions == [ (3, 0), (3, 1), (3, 2), (4, 0), (4, 2), ]
    
    positions = _getAdjacentPositionsTo(2, 2, 5, 4)
    assert positions == [ (1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3), ]

    positions = _getAdjacentPositionsTo(4, 3, 5, 4)
    assert positions == [ (3, 2), (3, 3), (4, 2), ]

    positions = _getAdjacentPositionsTo(4, 0, 5, 4)
    assert positions == [ (3, 0), (3, 1), (4, 1), ]


def test__applyRule1To():
    seats = copy.deepcopy(_data)

    assert _applyRule1To((0, 0), [ (0, 1), (1, 0), (1, 1), ], seats)

    seats[1] = 'L#LLLLL.LL'
    assert not _applyRule1To((0, 0), [ (0, 1), (1, 0), (1, 1), ], seats)


def test__applyRule2To():
    seats = copy.deepcopy(_data)

    assert not _applyRule2To((0, 0), [ (0, 1), (1, 0), (1, 1), ], seats)

    seats[1] = 'L#LLLLL.LL'
    assert not _applyRule2To((0, 0), [ (0, 1), (1, 0), (1, 1), ], seats)

    seats[0] = '#.LL.LL.LL'
    seats[1] = 'L##LLLL.LL'
    seats[2] = '#.L.L..L..'
    assert not _applyRule2To((1, 1), [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ], seats)

    seats[0] = '#.#L.LL.LL'
    seats[1] = 'L##LLLL.LL'
    seats[2] = '#.#.L..L..'
    assert _applyRule2To((1, 1), [ (0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2) ], seats)

    seats[0] = '#.##.##.##'
    seats[1] = '#######.##'
    seats[2] = '#.#.#..#..'
    assert _applyRule2To((2, 1), [  (2, 0), (3, 0), (4, 0),
                                    (2, 1), (3, 1), (4, 1), 
                                    (2, 2), (3, 2), (4, 2), ], seats)


def test__assertNoChangeIn():
    now = [ 'LLL', '###', 'L.L', ]
    future = copy.deepcopy(now)

    assert _assertNoChangeIn(now, future)


def test_resolvePuzzle01Using():
    answer, _ = resolvePuzzle01Using(_data, _tokens)

    assert answer == 37


# def test__getLoSPositions():
#     positions = _getLoSPositions(4, 4, 10, 9)
#     assert len(positions) == 33
#     assert (4, 2) == positions[8]
#     assert (9, 4) == positions[32]
#     assert (1, 7) == positions[21]
#     
#     positions = _getLoSPositions(9, 7, 10, 9)
#     assert len(positions) == 25
#     assert (7, 7) == positions[6]
#     assert (4, 2) == positions[16]
#     assert (0, 7) == positions[24]
# 
#     positions = _getLoSPositions(9, 7, 10, 9)
#     assert len(positions) == 25
#     assert (3, 0) == positions[6]
#     assert (7, 7) == positions[16]
#     assert (9, 0) == positions[24]
# 
# 
# def test__findSeatPositionsFrom():
#     seats = [
#                 '##L##',
#                 'LLL#L',
#                 '#..LL',
#                 'L##.L', ]
# 
#     positions = _findSeatPositionsFrom(0, 0, seats)
#     seatStates = [seats[position.y][position.x] for position in positions]
# 
#     assert 8 == len(positions)
#     assert '.' not in positions
#     assert seats[positions[7].y][positions[7].x] == '#'
#     assert seats[positions[3].y][positions[3].x] == 'L'
# 
#     positions = _findSeatPositionsFrom(3, 2, seats)
#     seatStates = [seats[position.y][position.x] for position in positions]
#     for position in positions:
#         print(position)
#     l = len(positions)
# 
#     assert '.' not in positions
# 
# 
# 
def test_resolvePuzzle02Using():
    answer, _ = resolvePuzzle02Using(_data, _tokens)

    assert answer == 26


def test_main():
    assert main(TEST_SEATS_FILE_NAME) == (37, 26)

# TODO: --- remove before final check-in ---

# test__getAdjacentPositionsTo()
# test__applyRule1To()
# test__applyRule2To()
# test_resolvePuzzle01Using()
# test__getLoSPositions()
# test__findSeatPositionsFrom()
# test_resolvePuzzle02Using()
# test_main()


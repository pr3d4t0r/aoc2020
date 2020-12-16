# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_16_tickets import loadExerciseDataFrom
from aoc.day_16_tickets import main
from aoc.day_16_tickets import resolvePuzzle01Using
from aoc.day_16_tickets import resolvePuzzle02Using
from aoc.day_16_tickets import _extractValueRangesFrom

import pytest


# +++ constants +++

TEST_DAY_16_TICKETS_FILE_NAME_A = 'resources/test/day_16_tickets-test-data-a.txt'
TEST_DAY_16_TICKETS_FILE_NAME_B = 'resources/test/day_16_tickets-test-data-b.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_DAY_16_TICKETS_FILE_NAME_A)


def test__extractValueRangesFrom():
    testData = '1-3 or 5-7'

    ranges = _extractValueRangesFrom(testData)
    
    assert [(1, 3,), (5, 7), ] == ranges



def test_resolvePuzzle01Using():
    global _data

    answer, ticketRanges, ticket, nearby, validTickets, invalidTickets = resolvePuzzle01Using(_data, _tokens)

    assert len(ticketRanges) == 3 and isinstance(ticketRanges, dict)
    assert len(ticket) == 3 and isinstance(ticket, list)
    assert len(nearby) == 12 and isinstance(nearby, list)
    assert len(validTickets) > 0 and isinstance(validTickets, list)
    assert 71 == answer

    _data = (ticketRanges, ticket, validTickets)


def test_resolvePuzzle02Using():
    global _data, _tokens

    _data, _tokens = loadExerciseDataFrom(TEST_DAY_16_TICKETS_FILE_NAME_B)
    fieldSignature = 'ro' # row - test partial

    _, ticketRanges, ticket, nearby, validTickets, invalidTickets = resolvePuzzle01Using(_data, _tokens)

    answer = resolvePuzzle02Using(ticketRanges, ticket, validTickets, fieldSignature)

    assert answer == 14


def test_main():
    assert main(TEST_DAY_16_TICKETS_FILE_NAME_A, 'ro', True) == (71, -1)


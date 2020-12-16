# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:

# Read:  itertools, more-itertools https://martinheinz.dev/blog/16
#        ref: https://pymotw.com/3/itertools/index.html
#        ref: https://realpython.com/python-itertools/
#        API ref: https://docs.python.org/3/library/itertools.html
#        API ref: https://more-itertools.readthedocs.io/en/latest/index.html


# TODO: Use itertools instead of invalidTickets
# from itertools import filterfalse

from more_itertools import split_at as splitAt

from util import loadExerciseDataFrom
from util import mainStart


# +++ constants +++


# *** functions ***


def _extractValueRangesFrom(data):
    ranges = list()
    for rangeDatum in splitAt(data.split(), lambda x: x == 'or'):
        n = rangeDatum[0].split('-')
        ranges.append((int(n[0]), int(n[1]), ))

    return ranges



def resolvePuzzle01Using(data, tokens):
    state = 0 # 0 == value ranges; 1 myTicket; 2 nearby tickets
    ticketRanges = dict()
    ticket = None
    nearby = list()
    allTickets = list()
    for seq, item in enumerate(data):
        if item:
            if state == 0 and item:
                ticketRanges[item[:item.index(':')]] = _extractValueRangesFrom(item[item.index(':')+1:].strip())
            elif state == 1:
                if 'your ticket' in item:
                    continue
                myTicket = [int(x) for x in item.split(',')]
            elif state == 2:
                if 'nearby tickets' in item:
                    continue
                ticketInfo = tuple([int(x) for x in item.split(',')])
                allTickets.append(ticketInfo)
                for t in ticketInfo:
                    nearby.append(int(t))
        else:
            state += 1


    validSeats = list()
    for ticketRange in ticketRanges.values():
        for t in ticketRange:
            for seat in range(t[0], t[1]+1):
                validSeats.append(seat)

    validSeats = set(validSeats)

    invalidTickets = list()

    for seat in nearby:
        if seat not in validSeats:
            invalidTickets.append(seat)

    validTickets = list()
    for ticket in allTickets:
        if any(value in invalidTickets for value in ticket):
            continue
        validTickets.append(ticket)

    return sum(invalidTickets), ticketRanges, myTicket, nearby, validTickets, invalidTickets


def resolvePuzzle02Using(ticketRanges, ticket, validTickets, fieldSignature):
    # TODO:  optimize to use itertools and more_itertools
    maxValidFields = len(ticketRanges)
    matchedNames = list()
    answer = 1
    processed = 0

    print('validTickets = %d' % len(validTickets))
    for validTicket in validTickets:
        matchedFields = 0
        for field in validTicket:
            for fieldName, value in ticketRanges.items():
                for valueRange in value:
                    matchedFields += sum([field in (v for v in range(valueRange[0], valueRange[1]+1))])

        if matchedFields == maxValidFields:
            break
        print('matchedFields: %d' % matchedFields)
        processed += 1
        if not processed % 10:
            print('    processed: %d' % processed)

    for field in validTicket:
        for fieldName, value in ticketRanges.items():
            for valueRange in value:
                if field in (v for v in range(valueRange[0], valueRange[1]+1)):
                    matchedNames.append(fieldName)

    keys = [ key for key in matchedNames if fieldSignature in key ]

    for vKey in keys:
        ptr = matchedNames.index(vKey)
        answer *= ticket[ptr]

    return answer



def main(fileName:str = None, fieldSignature = 'departure', unitTest = False):
    fileName = mainStart(fileName, 16)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1, ticketRanges, ticket, nearby, validTickets, invalidTickets = resolvePuzzle01Using(data, tokens)
    print('answer 1: %d' % answer1)
    answer2 = -1 if unitTest else resolvePuzzle02Using(ticketRanges, ticket, validTickets, fieldSignature)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


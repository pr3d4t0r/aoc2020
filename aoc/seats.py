# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart

import collections
import copy


SeatingLocation = collections.namedtuple('SeatingLocation', ['x', 'y'])


# +++ constants +++


# *** functions ***

def _getAdjacentPositionsTo(x, y, maxX, maxY):
    xStart = x-1 if (x-1 > 0) else 0
    xStop = x+2 if (x+1 < maxX) else x+1
    yStart = y-1 if (y-1 > 0) else 0
    yStop = y+2 if (y+1 < maxY) else y+1
    positions = list()

    for h in range(xStart, xStop):
        for v in range(yStart, yStop):
            if (h, v) == (x, y): continue
            positions.append((h, v), )

    return positions


def _applyRule1To(l, adjacent, seats):
    result = False
    location = SeatingLocation(l[0], l[1])

    if seats[location.y][location.x] in [ '.', '#', ]:
        return False

    for t in adjacent:
        testLocation = SeatingLocation(t[0], t[1])

        if seats[testLocation.y][testLocation.x] in [ '.', 'L', ]:
            result = True
        else:
            result = False
            break

    return result


def _applyRule2To(l, adjacent, seats):
    occupied = 0
    location = SeatingLocation(l[0], l[1])

    if seats[location.y][location.x] in [ '.', 'L', ]:
        return 0

    for t in adjacent:
        testLocation = SeatingLocation(t[0], t[1])

        seatState = seats[testLocation.y][testLocation.x]

        if seatState == '.': continue

        occupied += (seatState == '#')

    return occupied >= 4


def _assertNoChangeIn(now, future):
    result = False

    t = all(row in future for row in now)

    return t

    
def resolvePuzzle01Using(data, tokens):
    allSeated = False
    occupied = 0
    seatsNow = copy.deepcopy(data)
    seatsFuture = copy.deepcopy(data)

    totalRounds = 1
    while not allSeated:
        for y, item in enumerate(data):
            for x, _ in enumerate(item):
                if seatsNow[y][x] == '.': continue
                if _applyRule1To([x, y], _getAdjacentPositionsTo(x, y, len(item), len(data)), seatsNow):
                    row = list(seatsFuture[y])
                    row[x] = '#'
                    seatsFuture[y] = ''.join(row)
                if _applyRule2To([x, y], _getAdjacentPositionsTo(x, y, len(item), len(data)), seatsNow):
                    row = list(seatsFuture[y])
                    row[x] = 'L'
                    seatsFuture[y] = ''.join(row)
        
        allSeated = all(row in seatsFuture for row in seatsNow)
        totalRounds += 1

        if not allSeated:
            seatsNow = copy.deepcopy(seatsFuture)


    occupied = sum(seat.count('#') for seat in seatsFuture)

    return occupied, totalRounds


def _getLoSPositions(x, y, xMax, yMax):
    # LoS == Line of Sight
    xW = xE = x
    yN = yS = y
    positions = list()

    while xW in range(xMax) or xE in range(xMax) or yN in range(yMax) or yS in range(yMax):
        xW -= 1
        yN -= 1
        xE += 1
        yS += 1

        if xW == x and yN == y:
            continue

        if yN in range(yMax):
            positions.append(SeatingLocation(x, yN))
        if xE in range(xMax) and yN in range(yMax):
            positions.append(SeatingLocation(xE, yN))
        if xE in range(xMax):
            positions.append(SeatingLocation(xE, y))
        if xE in range(xMax) and yS in range(yMax):
            positions.append(SeatingLocation(xE, yS))
        if yS in range(yMax):
            positions.append(SeatingLocation(x, yS))
        if xW in range(xMax) and yS in range(yMax):
            positions.append(SeatingLocation(xW, yS))
        if xW in range(xMax):
            positions.append(SeatingLocation(xW, y))
        if xW in range(xMax) and yN in range(yMax):
            positions.append(SeatingLocation(xW, yN))

    return positions


def _findSeatPositionsFrom(x, y, seats):
    totalPositions = _getLoSPositions(x, y, len(seats[0]), len(seats))
    seatPositions = list()

    for position in totalPositions:
        if seats[position.y][position.x] != '.':
            seatPositions.append(position)

    return seatPositions


def resolvePuzzle02Using(data, tokens):
    for p in _getLoSPositions(3, 2, 5, 4):
        print(p)

    exit(0)
    allSeated = False
    seatsNow = copy.deepcopy(data)
    seatsFuture = copy.deepcopy(data)

    totalRounds = 1
    while not allSeated:
        for y, item in enumerate(data):
            for x, _ in enumerate(item):
                state = seatsNow[y][x]
                if state == '.': continue
                if state == 'L':
                    visibleSeatPositions = _findSeatPositionsFrom(x, y, seatsNow)

    return -1



def main(fileName:str = None):
    fileName = mainStart(fileName, 11)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1, totalRounds = resolvePuzzle01Using(data, tokens)
    answer2 = resolvePuzzle02Using(data, tokens)

    print('answer 1: %d in %d rounds' % (answer1, totalRounds))
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


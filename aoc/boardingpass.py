# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import mainStart


# +++ constants +++

MAX_COL = 7
MAX_ROW = 127


# *** functions ***

def loadBoardingPassesFrom(fileName):
    return [ b for b in open(fileName, 'r').read().split('\n') if len(b) ]


def _binSearchIn(data, head):
    tail   = 0
    ptr    = 0
    mid    = 0

    while tail < head:
        mid = int((head+tail)/2)
        if data[ptr] == 'F' or data[ptr] == 'L':
            head = mid
        else:
            tail = mid+1
        ptr += 1

    return head


def _rowFrom(boardingPass):
    return _binSearchIn(boardingPass[:7], MAX_ROW)


def _colFrom(boardingPass):
    return _binSearchIn(boardingPass[-3:], MAX_COL)


def _seatInfo(boardingPass):
    """
    Returns a tuple:
    
        - row
        - column
        - ID
    """
    row = _rowFrom(boardingPass)
    col = _colFrom(boardingPass)
    
    return row, col, 8*row+col


def findHighestIDIn(boardingPasses):
    maxID = -1
    seatIDs = list()

    for boardingPass in boardingPasses:
        _, _, seatID = _seatInfo(boardingPass)
        seatIDs.append(seatID)
        if seatID > maxID:
            maxID = seatID

    return maxID, sorted(seatIDs)


def resolveSeat(seatIDs):
    offset = seatIDs[0]
    for currentID in range(seatIDs[0], len(seatIDs)):
        seatID = seatIDs[currentID-offset]
        if currentID != seatID:
            return currentID


def main(fileName = None):
    fileName = mainStart(fileName, 5)
    boardingPasses = loadBoardingPassesFrom(fileName)

    maxID, \
    seatIDs = findHighestIDIn(boardingPasses)
    mySeatID = resolveSeat(seatIDs) if len(seatIDs) > 100 else 0 # for unit tests; see day 5 spec for reason

    print('maxID = %d' % maxID)
    print('My seat = %d' % mySeatID)

    return maxID, mySeatID


# --- main ---

if '__main__' == __name__:
    main()


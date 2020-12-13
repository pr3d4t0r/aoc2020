# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart

import collections


CardinalPoints = collections.namedtuple('CardinalPoints', [ 'E', 'N', 'W', 'S', ])
Vector = collections.namedtuple('Vector', [ 'x', 'y', ])

# +++ constants +++

CARDINAL_POINTS = CardinalPoints(0, 90, 180, 270)
INITIAL_WAYPOINT = Vector(1, 10)


# *** functions ***

def _moveX(heading, value):
    if heading == CARDINAL_POINTS.N or heading == CARDINAL_POINTS.S:
        return 0

    return value if heading == CARDINAL_POINTS.E else -value


def _moveY(heading, value):
    if heading == CARDINAL_POINTS.E or heading == CARDINAL_POINTS.W:
        return 0

    return value if heading == CARDINAL_POINTS.N else -value


def resolvePuzzle01Using(data, tokens):
    x = 0
    y = 0
    heading = 0
    distance = 0

    for seq, item in enumerate(data):
        command = item[0]
        value   = int(item[1:])

        if command == 'F':
            x += _moveX(heading, value)
            y += _moveY(heading, value)
        elif command in ['N', 'S']:
            y += value if command == 'N' else -value
        elif command in ['E', 'W']:
            x += value if command == 'E' else -value
        elif command == 'L':
            heading = (heading+value) % 360
        elif command == 'R':
            heading = abs((heading-value) % 360)
            
    distance = abs(x)+abs(y)

    return distance


def resolvePuzzle02Using(data, tokens):
    v = Vector(0, 0)
    waypoint = INITIAL_WAYPOINT
    distance = -1

    for seq, item in enumerate(data):
        command = item[0]
        value   = int(item[1:])

        if command == 'F':
            v = Vector(waypoint.x*value+v.x, waypoint.y*value+v.y)
        elif command == 'N':
            waypoint = Vector(waypoint.x+value, waypoint.y)
        elif command == 'S':
            waypoint = Vector(waypoint.x-value, waypoint.y)
        elif command == 'E':
            waypoint = Vector(waypoint.x, waypoint.y+value)
        elif command == 'W':
            waypoint = Vector(waypoint.x, waypoint.y-value)

        elif command in [ 'R', 'L' ] and value == 180:
                waypoint = Vector(-waypoint.x, -waypoint.y)

        elif command in ['R', 'L', ]:
            if command == 'L':
                value = 360-value
            if  value == 90:
                waypoint = Vector(-waypoint.y, waypoint.x)
            elif value == 270:
                waypoint = Vector(waypoint.y, -waypoint.x)

    distance = sum(abs(c) for c in v)

    return distance, v


def main(fileName:str = None):
    fileName = mainStart(fileName, 12)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1    = resolvePuzzle01Using(data, tokens)
    answer2, _ = resolvePuzzle02Using(data, tokens)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


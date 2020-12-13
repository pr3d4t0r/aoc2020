# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:

# Map:
#     ..##.........##.........##.........##.........##.........##.......  --->
#     #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#     .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#     ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#     .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#     ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
#     .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#     .#........#.#........X.#........#.#........#.#........#.#........#
#     #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#     #...##....##...##....##...#X....##...##....##...##....##...##....#
#     .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#
#              1         2         3^
#     12345678901234567890123456789012345
#     ..##.......


from bitarray import bitarray # type: ignore

from util import mainStart

import math


# *** constants ***

TREES_TRAVERSALS = [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2), ]
X_STEP = 8
Y_STEP = 1


# *** functions ***

def loadMapFrom(fileName):
    treesMap  = [bitarray(x.replace('.', '0').replace('#', '1').replace('\n', '')) for x in open(fileName, 'r').readlines()]
    geoExpand = int(((X_STEP+1)*len(treesMap))/len(treesMap[0]))

    for ref in range(len(treesMap)):
        treesMap[ref] = geoExpand*treesMap[ref]

    return treesMap


def calculateImpactsFrom(treesMap, xStep = X_STEP, yStep = Y_STEP):
    x = 0
    y = 0
    impacts = 0

    for row in range(len(treesMap)):
        x = row*xStep
        y = row*yStep
        try:
            impacts += treesMap[y][x]
        except:
            pass

    return impacts


def calculateAllImpactsUsing(treesMap, traversals):
    """
    tressMap   - obvious
    traversals - A list of tuples with right, down traversal steps
    """
    impactsList = [calculateImpactsFrom(treesMap, traversal[0], traversal[1]) for traversal in traversals]

    return math.prod(impactsList)


def main(fileName = None):
    fileName = mainStart(fileName, 3)
    treesMap = loadMapFrom(fileName)

    treeImpacts = calculateImpactsFrom(treesMap, 3, 1)
    treeImpactsAll = calculateAllImpactsUsing(treesMap, TREES_TRAVERSALS)

    print('Tree impacts = %d' % treeImpacts)
    print('Tree impacts multiple traversals = %d' % treeImpactsAll)

    return treeImpacts, treeImpactsAll


# --- main ---

if '__main__' == __name__:
    main()


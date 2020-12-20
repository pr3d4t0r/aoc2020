# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:

# Read:  itertools, more-itertools https://martinheinz.dev/blog/16
#        ref: https://pymotw.com/3/itertools/index.html
#        ref: https://realpython.com/python-itertools/
#        API ref: https://docs.python.org/3/library/itertools.html
#        API ref: https://more-itertools.readthedocs.io/en/latest/index.html


from collections import namedtuple

from bitarray import bitarray # type: ignore

from util import loadExerciseDataAsTextRecordsFrom
from util import loadExerciseDataFrom
from util import loadRawExerciseTextFrom
from util import mainStart


TileEdges = namedtuple('TileEdges', ['north', 'east', 'south', 'west', ])


# +++ constants +++


# *** functions ***

def _edgesOf(tileAsText):
    tile = tileAsText.strip().split('\n')

    n = bitarray([feature == '#' for feature in tile[0] ])
    s = bitarray([feature == '#' for feature in tile[len(tile)-1]])
    e = bitarray([tile[ptr][len(tile)-1] == '#' for ptr in range(len(tile))])
    w = bitarray([tile[ptr][0] == '#' for ptr in range(len(tile))])

    return TileEdges(n, e, s, w)
        

def _tileFromRecord(record):
    tileID = int(record.split(':')[0].replace('Tile ', ''))
    tile = record.split(':\n')[1]
    edges = _edgesOf(tile)

    return tileID, tile, edges


def resolvePuzzle01Using(data, tokens, rawText, textRecords):
    tiles = dict()

    for seq, record in enumerate(textRecords):
        tileID, tile, edges = _tileFromRecord(record)
        tiles[tileID] = { 'tile': tile, 'edges': edges, }

    e = tiles[2311]['edges']

    return -1


def resolvePuzzle02Using(data, tokens, rawText, textRecords):
    return -1


def main(fileName:str = None):
    fileName = mainStart(fileName, 2)

    data, tokens = loadExerciseDataFrom(fileName)
    rawText = loadRawExerciseTextFrom(fileName)
    textRecords = loadExerciseDataAsTextRecordsFrom(fileName)

    # ------------------------------------------
    # Answer 1
    # ------------------------------------------
    answer1 = resolvePuzzle01Using(data, tokens, rawText, textRecords)
    answer2 = resolvePuzzle02Using(data, tokens, rawText, textRecords)

    print('answer 1: %d, answer 2: %d' % (answer1, answer2))

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


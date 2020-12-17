# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:

# Read:  itertools, more-itertools https://martinheinz.dev/blog/16
#        ref: https://pymotw.com/3/itertools/index.html
#        ref: https://realpython.com/python-itertools/
#        API ref: https://docs.python.org/3/library/itertools.html
#        API ref: https://more-itertools.readthedocs.io/en/latest/index.html


from scipy.ndimage import convolve

from util import loadExerciseDataFrom
from util import mainStart

import numpy as np


# +++ constants +++


# *** functions ***

def resolvePuzzle01Using(data, tokens, maxCycles = 6, dimensions = 3, shape = 20):
    dSlice = np.ones(tuple(3 for d in range(dimensions)))
    dSlice[tuple(1 for d in range(dimensions))] = 0
    data = np.array([[cube == '#' for cube in row] for row in tokens])

    activeCubesSpace = np.zeros((*(13 for d in range(dimensions - 2)), shape, shape), dtype=int)
    activeCubesSpace[tuple(maxCycles for d in range(dimensions - 2))] = np.pad(data, maxCycles)

    for cycle in range(maxCycles):
        neighbors = convolve(activeCubesSpace, dSlice, mode='constant', cval = 0)
        activeCubesSpace = np.where((neighbors == 3) | (activeCubesSpace & (neighbors==2)), 1, 0)

    return activeCubesSpace.sum()


def resolvePuzzle02Using(data, tokens, unitTest = False):
    shapeArg = 15 if unitTest else 20

    return resolvePuzzle01Using(data, tokens, maxCycles = 6, dimensions = 4, shape = shapeArg)



def main(fileName:str = None, unitTest = False):
    fileName = mainStart(fileName, 17)
    shape = 15 if unitTest else 20

    data, tokens = loadExerciseDataFrom(fileName)

    # ------------------------------------------
    # Answer 1
    # ------------------------------------------
    answer1 = resolvePuzzle01Using(data, tokens, 6, 3, shape)
    print('answer 1: %d' % answer1)

    # ------------------------------------------
    # Answer 2
    # ------------------------------------------
    answer2 = resolvePuzzle02Using(data, tokens, unitTest)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


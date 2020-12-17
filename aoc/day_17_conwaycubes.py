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

def resolvePuzzle01Using(data, tokens, maxCycles = 6, dimensions = 3, shape = 20, unitTest = False):
    data = np.array([[cube == '#' for cube in row] for row in data])
    shape = 15 if unitTest else 20
    

    KERNEL = np.ones(tuple(3 for _ in range(dimensions)))
    KERNEL[tuple(1 for _ in range(dimensions))] = 0

    # universe = np.zeros((*(13 for _ in range(n - 2)), 20, 20), dtype=int)
    # p1 -> universe = np.zeros((*(13 for _ in range(dimensions - 2)), 20, 20), dtype=int)
    # >> try >> universe = np.zeros((*(13 for _ in range(dimensions - 2)), 26, 26), dtype=int)
    # p2 -> universe = np.zeros((*(13 for _ in range(dimensions - 2)), 15, 15), dtype=int)
    universe = np.zeros((*(13 for _ in range(dimensions - 2)), shape, shape), dtype=int)
    universe[tuple(maxCycles for _ in range(dimensions - 2))] = np.pad(data, maxCycles)

    for _ in range(maxCycles):
        neighbors = convolve(universe, KERNEL, mode="constant")
        universe = np.where((neighbors == 3) | (universe & (neighbors==2)), 1, 0)

    return universe.sum()


def resolvePuzzle02Using(data, tokens, unitTest = False):
    shapeArg = 15 if unitTest else 20

    return resolvePuzzle01Using(data, tokens, maxCycles = 6, dimensions = 4, shape = shapeArg)



def main(fileName:str = None, unitTest = False):
    fileName = mainStart(fileName, 17)

    data, tokens = loadExerciseDataFrom(fileName)

    # ------------------------------------------
    # Answer 1
    # ------------------------------------------
    answer1 = resolvePuzzle01Using(data, tokens, 6, 3, 20, unitTest)
    print('answer 1: %d' % answer1)

    # ------------------------------------------
    # Answer 2
    # ------------------------------------------
    data, tokens = loadExerciseDataFrom(fileName)
    answer2 = resolvePuzzle02Using(data, tokens, unitTest)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from typing import Any
from typing import List
from util import mainStart


# +++ constants +++


# *** functions ***

def loadExerciseDataFrom(fileName: str) -> list:
    open(fileName, 'r').close()

    data:List[Any] = list()

    return data


def resolvePuzzle01Using(data):
    return -1


def resolvePuzzle02Using(data):
    return -1



def main(fileName:str = None):
    fileName = mainStart(fileName, %d%)

    data = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzle01Using(data)
    answer2 = resolvePuzzle02Using(data)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart


# +++ constants +++


# *** functions ***

def resolvePuzzle01Using(data, tokens):
    # TODO: remove this before pull request
    # ---- cut here ----
    for seq, item in enumerate(data):
        print('%04d | %s' % (seq, item))
    print()
    # ---- cut here ----

    return -1


def resolvePuzzle02Using(data, tokens):
    return -1



def main(fileName:str = None):
    fileName = mainStart(fileName, %d%)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzle01Using(data, tokens)
    answer2 = resolvePuzzle02Using(data, tokens)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


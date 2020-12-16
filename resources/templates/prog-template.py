# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:

# Read:  itertools, more-itertools https://martinheinz.dev/blog/16
#        ref: https://pymotw.com/3/itertools/index.html
#        ref: https://realpython.com/python-itertools/
#        API ref: https://docs.python.org/3/library/itertools.html
#        API ref: https://more-itertools.readthedocs.io/en/latest/index.html


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

    # ------------------------------------------
    # Answer 1
    # ------------------------------------------
    answer1 = resolvePuzzle01Using(data, tokens)
    print('answer 1: %d' % answer1)

    # ------------------------------------------
    # Answer 2
    # ------------------------------------------
    answer2 = resolvePuzzle02Using(data, tokens)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


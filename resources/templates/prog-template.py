# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:

# Read:  itertools, more-itertools https://martinheinz.dev/blog/16
#        ref: https://pymotw.com/3/itertools/index.html
#        ref: https://realpython.com/python-itertools/
#        API ref: https://docs.python.org/3/library/itertools.html
#        API ref: https://more-itertools.readthedocs.io/en/latest/index.html


from util import RECORD_SEPARATOR
from util import loadExerciseDataAsTextRecordsFrom
from util import loadExerciseDataFrom
from util import loadRawExerciseTextFrom
from util import mainStart


# +++ constants +++


# *** functions ***

def resolvePuzzle01Using(data, tokens, rawText, textRecords):
    # ---- proces data, tokens ---
    for seq, item in enumerate(data):
        print('%04d | %s' % (seq, item))
    print()
    # ---- proces data, tokens ---

    # ---- process rawText ---
    for line in rawText.split('\n'):
        pass
    # ---- process rawText ---

    # ---- process textRecords ---
    for seq, record in enumerate(textRecords):
        print('record %02d = %s' % (seq, record))

    return -1


def resolvePuzzle02Using(data, tokens, rawText, textRecords):
    return -1



def main(fileName:str = None):
    fileName = mainStart(fileName, %d%)

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


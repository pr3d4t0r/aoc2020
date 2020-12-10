# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart

from collections import Counter
from functools import lru_cache


# +++ constants +++


# *** functions ***

def resolvePuzzle01Using(data, tokens):
    chain = list()

    data = sorted([ int(datum) for datum in data ])
    joltRating = 0
    ref = 0
    joltDifferences = Counter()
    
    while data:
        maxJolt = joltRating+3
        if data[0] > joltRating and data[0] <= maxJolt+3:
            adapterJolt = data.pop(0)
            chain.append(adapterJolt)
            joltDifferences[adapterJolt-ref] += 1
            ref = adapterJolt

        joltRating += 1

    joltDifferences[3] += 1

    return joltDifferences[3]*joltDifferences[1], chain


def resolvePuzzle02Using(chain):
    maxJolt = max(chain)

    @lru_cache
    def findArrangements(adapterJolt, maxJolt):
        count = 0

        if adapterJolt >= maxJolt:
            return 1

        for ptr in range(1, 4):
            if adapterJolt+ptr in chain:
                count += findArrangements(adapterJolt+ptr, maxJolt)
            else:
                continue

        return count

    return findArrangements(0, maxJolt)



def main(fileName:str = None):
    fileName = mainStart(fileName, 10)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1,\
    chain = resolvePuzzle01Using(data, tokens)

    answer2 = resolvePuzzle02Using(chain)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


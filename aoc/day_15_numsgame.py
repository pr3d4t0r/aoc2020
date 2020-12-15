# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart

import collections


# +++ constants +++


# *** functions ***

def resolvePuzzle01Using(data, tokens, limit = 2020):
    series = collections.defaultdict(list)
    tokens = tokens[0].split(',')
    for seq, datum in enumerate(tokens):
        series[int(datum)].append(seq+1)
        
    turn = len(series)
    lastNum = int(tokens[-1])
    nextNum = int(tokens[-1])
    while turn < limit:
        if nextNum not in series:
            nextNum = 0
        else:
            nextNum = series[lastNum][len(series[lastNum])-1]-series[lastNum][len(series[lastNum])-2]

        turn += 1
        lastNum = nextNum
        series[nextNum].append(turn)

    return nextNum


def resolvePuzzle02Using(data, tokens):
    # TODO:  Resolve using Van Eck's sequence next time.  See:
    #        https://oeis.org/A181391
    #
    #        There appear to be no clever tricks to avoid the brute force
    #        attempt in this implementation.

    return resolvePuzzle01Using(data, tokens, 30000000)



def main(fileName:str = None, unitTest = False):
    fileName = mainStart(fileName, 15)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzle01Using(data, tokens)
    answer2 = -1 if unitTest else resolvePuzzle02Using(data, tokens)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


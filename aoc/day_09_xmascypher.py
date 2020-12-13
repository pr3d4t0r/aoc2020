# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart


# +++ constants +++

PREAMBLE_LENGTH = 25


# *** functions ***

def validateIn(x, data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            s = data[i]+data[j]
            
            if x == s:
                return True

    return False


def resolvePuzzle01Using(data, tokens, preambleLength):
    data = [ int(datum) for datum in data ]

    for seq, item in enumerate(data):
        if seq > preambleLength:
            if not validateIn(item, data[seq-preambleLength:seq]):
                break

    return item, data


# ------------------------------------------------------------------------------
# I went for a hard break out of the inner loop at first, decided
# to fix it later but leave this one up.  In the rush to submit as early as
# possible I went for the hard break instead of a clean exit.
# ------------------------------------------------------------------------------
# def resolvePuzzle02Using(data, tokens, preambleLength, vulnerability):
#     limit = data.index(vulnerability)
#     weakness = -1
#     tail = 0
# 
#     try:
#         while tail < limit:
#             for head in range(tail+2, limit):
#                 y = data[tail:head]
#                 testValue = sum(data[tail:head])
#                 if testValue == vulnerability:
#                     raise Exception
#                 if testValue > vulnerability:
#                     break
# 
#             tail += 1
#     except:
#         weakness = min(data[tail:head])+max(data[tail:head])
# 
#     return weakness
# 
# 
# 
def resolvePuzzle02Using(data, tokens, preambleLength, vulnerability):
    limit = data.index(vulnerability)
    weakness = -1
    tail = 0

    while tail < limit:
        for head in range(tail+2, limit):
            testValue = sum(data[tail:head])
            if testValue == vulnerability:
                weakness = min(data[tail:head])+max(data[tail:head])
                tail = limit
                break
            if testValue > vulnerability:
                break

        tail += 1

    return weakness


def main(fileName:str = None, preambleLength = PREAMBLE_LENGTH):
    fileName = mainStart(fileName, 9)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1, \
    data = resolvePuzzle01Using(data, tokens, preambleLength)
    answer2 = resolvePuzzle02Using(data, tokens, preambleLength, answer1)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


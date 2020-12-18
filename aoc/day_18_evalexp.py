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

def _tokenizeExpression(expr):
    return expr.replace('(', '( ').replace(')', ' )').split()


def _evaluateExpression(terms):
    # Saved for puzzle #2?
    # opStack = list()
    outputQueue = list()

    ptr = 0
    while ptr < len(terms):
        term = terms[ptr]
        if term.isnumeric():
            outputQueue.append(int(term))
        elif term in ('+', '*'):
            outputQueue.append(term)
        elif term == '(':
            v, r = _evaluateExpression(terms[ptr+1:])
            outputQueue.append(v)
            ptr += r
        elif term == ')':
            ptr += 1
            break

        ptr += 1
            
    while outputQueue:
        t = outputQueue.pop(0)
        if isinstance(t, int):
            result = t
        elif t == '+':
            result += outputQueue.pop(0)
        elif t == '*':
            result *= outputQueue.pop(0)

    return result, ptr


def resolvePuzzle01Using(data, tokens):
    total = 0
    for seq, item in enumerate(data):
        result, _ = _evaluateExpression(_tokenizeExpression(item))
        total += result

    return total


def resolvePuzzle02Using(data, tokens):
    return -1



def main(fileName:str = None):
    fileName = mainStart(fileName, 18)

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


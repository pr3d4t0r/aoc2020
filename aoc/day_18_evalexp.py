# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart


# +++ constants +++

OPERATIONS = {
    '+': (lambda x, y: x+y),
    '*': (lambda x, y: x*y),
}


# *** functions ***

def _tokenizeExpression(expr):
    return expr.replace('(', '( ').replace(')', ' )').split()


def _evaluateExpression(terms, precedenceFlag = True):
    opStack = list()
    outputQueue = list()

    ptr = 0
    while ptr < len(terms):
        term = terms[ptr]
        if term.isnumeric():
            outputQueue.append(int(term))
        elif term in OPERATIONS:
            if precedenceFlag:
                while opStack and opStack[-1] > term:
                    outputQueue.append(opStack.pop())
                opStack.append(term)
            else:
                # Use the opStack?
                outputQueue.append(term)
        elif term == '(':
            v, r = _evaluateExpression(terms[ptr+1:], precedenceFlag)
            outputQueue.append(v)
            ptr += r
        elif term == ')':
            ptr += 1
            break

        ptr += 1

    while(opStack): outputQueue.append(opStack.pop())

    if precedenceFlag:
        for term in outputQueue:
            opStack.append(OPERATIONS[term](opStack.pop(), opStack.pop()) if term in OPERATIONS else term)

        result = opStack.pop()
    else:
        while outputQueue:
            t = outputQueue.pop(0)
            result = t if isinstance(t, int) else OPERATIONS[t](result, outputQueue.pop(0))

    return result, ptr


def resolvePuzzleUsing(data, tokens, precedenceFlag):
    total = 0
    for seq, item in enumerate(data):
        result, _ = _evaluateExpression(_tokenizeExpression(item), precedenceFlag)
        total += result

    return total


def main(fileName:str = None):
    fileName = mainStart(fileName, 18)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzleUsing(data, tokens, False)
    print('answer 1: %d' % answer1)

    answer2 = resolvePuzzleUsing(data, tokens, True)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


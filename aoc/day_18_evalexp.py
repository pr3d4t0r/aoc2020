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


def _evaluateExpression(terms):
    # https://en.wikipedia.org/wiki/Shunting-yard_algorithm

    opStack = list()
    outputQueue = list()

    ptr = 0
    while ptr < len(terms):
        term = terms[ptr]
        if term.isnumeric():
            outputQueue.append(int(term))
        elif term in OPERATIONS:
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
        # Linear is faster since the output queue is also linear.
        t = outputQueue.pop(0)
        if isinstance(t, int):
            result = t
        elif t == '+':
            result += outputQueue.pop(0)
        elif t == '*':
            result *= outputQueue.pop(0)

    return result, ptr



def _evaluateExpressionReversePrecedence(terms):
    """
       In this exercise, + has greater precedence than *.  That's why the
       expressions look weird.
    """
    opStack = list()
    outputQueue = list()

    ptr = 0
    while ptr < len(terms):
        term = terms[ptr]
        if term.isnumeric():
            outputQueue.append(int(term))
        elif term in OPERATIONS:
            while opStack and opStack[-1] > term:
                outputQueue.append(opStack.pop())
            opStack.append(term)
        elif term == '(':
            v, r = _evaluateExpressionReversePrecedence(terms[ptr+1:])
            outputQueue.append(v)
            ptr += r  # Use the opStack instead of the counter.
        elif term == ')':
            ptr += 1
            break

        ptr += 1

    while(opStack):
        outputQueue.append(opStack.pop())
            
    for term in outputQueue:
        if term in OPERATIONS:
            operand1 = opStack.pop()
            operand0 = opStack.pop()
            result = OPERATIONS[term](operand0, operand1)
            opStack.append(result)
        else:
            opStack.append(term)

    result = opStack.pop()

    return result, ptr


def resolvePuzzle01Using(data, tokens):
    total = 0
    for seq, item in enumerate(data):
        result, _ = _evaluateExpression(_tokenizeExpression(item))
        total += result

    return total


def resolvePuzzle02Using(data, tokens):
    total = 0
    for seq, item in enumerate(data):
        result, _ = _evaluateExpressionReversePrecedence(_tokenizeExpression(item))
        total += result

    return total


def main(fileName:str = None):
    fileName = mainStart(fileName, 18)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzle01Using(data, tokens)
    print('answer 1: %d' % answer1)

    answer2 = resolvePuzzle02Using(data, tokens)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()


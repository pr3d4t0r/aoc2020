# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import mainStart

import copy
import fileinput


# +++ constants +++


# *** functions ***

def loadExerciseDataFrom(fileName: str) -> list:
    data = [ line.strip() for line in fileinput.input(fileName) ]

    tokens = list()

    for line in data:
        tokens.extend(line.split())

    return data, tokens


def run(program):
    acc = 0
    instructionPtr = 0
    visited = [ 0 for n in program ]
    while instructionPtr < len(program):
        instruction = program[instructionPtr].split()
        opCode = instruction[0]
        opCodeerand = int(instruction[1].replace('+', ''))
        visited[instructionPtr] += 1
        if 2 in visited:
            break
        if opCode == 'acc':
            acc += opCodeerand
            instructionPtr  += 1
        elif opCode == 'jmp':
            instructionPtr += opCodeerand
        elif opCode == 'nop':
            instructionPtr += 1

    return instructionPtr, acc
    

def resolvePuzzle01Using(data):
    _, acc = run(data)

    return acc


def resolvePuzzle02Using(data):
    ip = -1
    for ref in range(len(data)):
        prog = copy.deepcopy(data)
        instruction = prog[ref].split()
        execute = True
        if 'nop' == instruction[0] and 0 != int(instruction[1]):
            prog[ref] = prog[ref].replace('nop', 'jmp')
        elif 'jmp' == instruction[0]:
            prog[ref] = prog[ref].replace('jmp', 'nop')
        else:
            execute = False

        if execute:
            ip, acc = run(prog)

        if ip >= len(data):
            return acc



def main(fileName:str = None):
    fileName = mainStart(fileName, 8)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzle01Using(data)
    answer2 = resolvePuzzle02Using(data)

    print()
    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()

